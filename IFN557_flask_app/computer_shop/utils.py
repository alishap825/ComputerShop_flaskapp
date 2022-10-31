import uuid

from flask import session
from .models import Product, Brand, Order, OrderDetails
from .enums import ProductCategory


def get_paginated_products_for_category(category: ProductCategory, page_number, per_page_limit):
    return Product.query.filter_by(
            category=category.value
        ).order_by(
            Product._id.desc()
        ).paginate(
            page=page_number, per_page=per_page_limit
        )


def get_paginated_products_for_brand(brand, page_number, per_page_limit):
    brands = Brand.query.filter(Brand.name.like('{0}%'.format(brand))).order_by(Brand._id.desc()).all()

    if not brands:
        return []
    return Product.query.filter_by(
        brand_id=brands[0]._id
        ).order_by(
            Product._id.desc()
        ).paginate(
            page=page_number, per_page=per_page_limit
        )


def make_session_product_details(product_id, quantity):
    product = None
    _existing = False
    if 'basket' not in session.keys() or session['basket'] is None:
        session['basket'] = []
        product = Product.query.filter_by(_id=product_id).first()
    elif 'basket' in session.keys() and session['basket'] is not None:
        product = get_product_from_basket(product_id)
        if product is not None:
            _existing = True
            session['basket'].remove(product)
    if not _existing:
        product = Product.query.filter_by(_id=product_id).first()
    return {
        'product_id': product_id,
        'product_details': product.get('product_details'),
        'quantity': int(quantity) + int(product.get('quantity')),
    } if _existing else {
        'product_id': product_id,
        'product_details': product.json(),
        'quantity': quantity,
    }


def get_product_from_basket(product_id):
    for p in session['basket']:
        if p.get('product_id') == product_id:
            return p
    return None


def update_basket_price():
    session['basketPrice'] = 0
    session['basketQuantity'] = 0
    if session['basket'] is None or not len(session['basket']):
        return 0
    for product in session['basket']:
        product_price = product.get('product_details').get('discount_price')
        product_quantity = product.get('quantity')
        session['basketPrice'] += float(product_price) * float(product_quantity)
        session['basketQuantity'] += int(product_quantity)
    print("Updated price to: {price}".format(price=session['basketPrice']))
    return session['basketPrice']


def make_order_from_form(form_data):
    new_order = Order(
        first_name=form_data.first_name.data,
        last_name=form_data.last_name.data or '',
        email=form_data.email.data,
        phone_number=form_data.phone.data,
        payment_type=form_data.payment_type.data,
        order_number=uuid.uuid4().hex,
        address_line_1=form_data.address_1.data,
        address_line_2=form_data.address_2.data,
        city=form_data.city.data,
        state=form_data.state.data,
        country=form_data.country.data,
        pincode=form_data.pincode.data,
        no_contact_delivery=form_data.no_contact_delivery.data or False,
        total_price=session['basketPrice'],
    )
    for product in session['basket']:
        p = Product.query.filter_by(_id=product.get('product_id')).one()
        order_details = OrderDetails(product_quantity=product.get('quantity'))
        order_details.products = p
        new_order.orders.append(order_details)
    return new_order
