from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Every item needs a price.")
    parser.add_argument('store_id', type=int, required=True, help="Every item needs a store id.")

    @jwt_required()
    def get(self, name):
        items = ItemModel.find_by_name(name)
        if items:
            return [item.json() for item in items], 200
        return {'message': 'Item not found'}, 404

    def post(self, name):

        data = Item.parser.parse_args()

        items = ItemModel.find_by_name(name)

        if items:
            for item in items:
                if item.store_id == data["store_id"]:
                    return {'message': f'An item with the {name} already exists in the store.'}, 409

        new_item = ItemModel(name, data["price"], data["store_id"])

        try:
            # item.insert()
            new_item.save_to_db()
        except:
            return {"message": "Insertion failed."}, 500

        return new_item.json(), 201

    def delete(self, name):
        items = ItemModel.find_by_name(name)
        if items:
            for item in items:
                item.delete_from_db()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name = ?"
        # cursor.execute(query, (name,))
        #
        # connection.commit()
        # connection.close()
        #
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        items = ItemModel.find_by_name(name)

        if items is None:
            item = ItemModel(name, **data)
            item.save_to_db()
        else:
            for item in items:
                if item.store_id == data['store_id']:
                    item.price = data['price']
                    break

        item.save_to_db()
        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
