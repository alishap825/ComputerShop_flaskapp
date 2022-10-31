from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import db, Product, CardDetails
from .utils import (
    get_paginated_products_for_category, get_paginated_products_for_brand,
    make_order_from_form)
from .enums import ProductCategory, FilterType, PaymentType, PaymentStatus
from .forms import CheckoutForm, CardForm

view = Blueprint('view', __name__)


@view.route('/')
@view.route('/index')
@view.route('/home')
def index():
    if 'basketQuantity' not in session.keys():
        session['basketQuantity'] = 0
    return render_template("index.html")


@view.route('/notFound')
def not_found():
    return render_template("404.html")


@view.route('/products', methods=['GET', 'POST'])
def products():
    page_limit = int(request.args.get('pageLimit')) if request.args.get('pageLimit') else 5  # default 5 if not supplied by user
    page_number = int(request.args.get('pageNumber')) if request.args.get('pageNumber') else 1  # default 1 if not supplied by user
    print(page_limit)
    session['pageLimit'] = page_limit
    session['pageNumber'] = page_number
    products_list = Product.query.order_by(
            Product._id.desc()
        ).paginate(page=page_number, per_page=page_limit)
    return render_template("productdetails.html", products=products_list)


@view.route('/singleproduct', methods=['GET', 'POST'])
def single_product():
    product_id = request.args.get('product_id')
    print(product_id)
    db_product = Product.query.filter_by(_id=product_id).one()
    print(type(db_product))
    product = {
        'id': db_product._id,
        'name': db_product.name,
        'description': db_product.description,
        'original_price': db_product.original_price,
        'discount_price': db_product.discount_price,
        'specifications': [[val.split(':')] for val in str(db_product.specifications).split('|')],
        'category': db_product.category,
        'brand': db_product.brand.name,
        'in_stock': db_product.in_stock,
        'image': db_product.image,
        'image2': db_product.image_2 or '',
    }
    print(product)
    return render_template("singleproductdetails.html", product=product)


@view.route('/filterproducts', methods=['GET', 'POST'])
def filter_product_details():
    filter_value = request.args.get('filterValue')
    filter_type = request.args.get('filterType')
    page_limit = int(request.args.get('pageLimit')) if request.args.get('pageLimit') else 5  # default 5 if not supplied by user
    page_number = int(request.args.get('pageNumber')) if request.args.get('pageNumber') else 1  # default 1 if not supplied by user
    session['pageLimit'] = page_limit
    session['pageNumber'] = page_number
    print(filter_type)
    print(filter_value)
    print(page_limit)
    print(page_number)
    final_products = []
    search = False
    if filter_type == FilterType.CATEGORY.value:
        # products are fetched in the descending order to show the latest added products first
        if filter_value == ProductCategory.LAPTOP.value:
            final_products = get_paginated_products_for_category(ProductCategory.LAPTOP, page_number, page_limit)
        elif filter_value == ProductCategory.ACCESSORY.value:
            final_products = get_paginated_products_for_category(ProductCategory.ACCESSORY, page_number, page_limit)
        elif filter_value == ProductCategory.DESKTOP.value:
            final_products = get_paginated_products_for_category(ProductCategory.DESKTOP, page_number, page_limit)
        print(type(final_products))
        print(final_products)
        print(final_products.iter_pages())
    elif filter_type == FilterType.BRAND.value:
        final_products = get_paginated_products_for_brand(filter_value, page_number, page_limit)
        search = True

    return render_template(
        "productdetailsfilter.html",
        product=filter_value,
        products=final_products if final_products else None,
        filter_type=filter_type,
        is_search=search,
    )


@view.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    card_form = CardForm()
    checkout_card_details = None
    if form.payment_type.data == PaymentType.CARD.value:
        if card_form.validate_on_submit():
            _existing_card_details = CardDetails.query.filter_by(card_number=card_form.card_number.data).all()
            if not _existing_card_details:
                checkout_card_details = CardDetails(
                    card_number=card_form.card_number.data,
                    card_expiry=card_form.expiry.data,
                    cvc=int(card_form.cvc.data),
                )
            else:
                print("Found existing card details, using these details....")
                print(_existing_card_details)
                checkout_card_details = _existing_card_details[0]
    if form.validate_on_submit():
        order = make_order_from_form(form)
        print(request.values)
        print(order)
        if checkout_card_details:
            order.payment_status = PaymentStatus.COMPLETE
            checkout_card_details.orders.append(order)
            db.session.add(checkout_card_details)
        else:
            db.session.add(order)
        db.session.commit()
        print('ORDER SUCCESS')
        session['basketQuantity'] = 0
        session['basketPrice'] = 0
        session['basket'] = None
        session['latestOrder'] = order.json()
        return redirect(url_for('view.order_success'))
    return render_template('checkout.html', form=form, cardForm=card_form)


@view.route('/orderSuccess', methods=['GET','POST'])
def order_success():
    if 'latestOrder' not in session.keys():
        return redirect(url_for('view.not_found'))
    return render_template('orderPlaced.html', order_details=session['latestOrder'])
