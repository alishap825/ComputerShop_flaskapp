from flask import Blueprint, session, request
from .models import db
from .enums import BasketAction
from pprint import PrettyPrinter
from .admin import create_data
from .utils import make_session_product_details, get_product_from_basket, update_basket_price

rest = Blueprint('rest', __name__)


@rest.route('/createData', methods=['GET'])
def create_admin_data():
    try:
        create_data(db)
        return {'message':'Created'}, 201
    except Exception as e:
        print(e)
        return {'message': 'Data already exists'}, 406


# Rest Endpoint that consumes data in json format and updates the basket
@rest.route('/addToBasket', methods=['POST'])
def add_to_basket():
    product_id = request.json.get('productId') or None
    quantity = request.json.get('quantity') or None
    print('Edit basket request received for productId:' + str(product_id) + ' and quantity:' + str(quantity))
    print("Received request JSON:")
    PrettyPrinter().pprint(request.json)
    print("Current basket: ")
    PrettyPrinter().pprint(session['basket'] if 'basket' in session.keys() else None)

    if request.json.get('action') == BasketAction.ADD_TO_BASKET.value:
        print("Adding product to basket...")
        session_product_details = make_session_product_details(product_id, quantity)
        # Session is Immutable
        # therefore existing data cannot be changed
        # new assignment has to be made
        new_list = session['basket']
        new_list.append(session_product_details)
        session['basket'] = new_list

    if request.json.get('action') == BasketAction.REMOVE_FROM_BASKET.value:
        print("Removing product from basket...")
        product = get_product_from_basket(product_id)
        # Session is Immutable
        # therefore existing data cannot be changed
        # new assignment has to be made
        new_list = session['basket']
        new_list.remove(product)
        session['basket'] = new_list

    update_basket_price()
    print("Updated basket: ")
    PrettyPrinter().pprint(session['basket'])
    return "Added to basket", 200
