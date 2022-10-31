import datetime

from . import db
from .enums import PaymentType, ProductCategory, PaymentStatus


class Product(db.Model):
    __tablename__ = 'products'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    image_2 = db.Column(db.String(500), nullable=True)
    original_price = db.Column(db.Float)
    discount_price = db.Column(db.Float)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand._id'))
    category = db.Column(db.Enum(ProductCategory, values_callable=lambda x: [str(category.value) for category in ProductCategory]), nullable=False)
    specifications = db.Column(db.String(1500), nullable=False)
    in_stock = db.Column(db.Boolean, nullable=True, default=True)
    products = db.relationship('OrderDetails', back_populates='products')

    def __repr__(self):
        return """ProductName:{name}\n
         ProductDescription:{desc}\n ProductOriginalPrice:{original_price}\n
         ProductDiscountPrice:{discount_price}
          \n Brand:{brand}""".format(
            name=self.name,
            desc=self.description,
            original_price=self.original_price,
            discount_price=self.discount_price,
            brand=self.brand_id,
            img=self.image
        )

    def get_product(self):
        return str(self)

    def json(self):
        return dict(
            name=self.name,
            desc=self.description,
            original_price=self.original_price,
            discount_price=self.discount_price,
            brand=self.brand_id,
            img=self.image,
            img2=self.image_2 or '',
            category=self.category.value,
            specifications=self.specifications,
            in_stock=self.in_stock,
        )


class Brand(db.Model):
    __tablename__ = 'brand'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    logo = db.Column(db.String(500), nullable=False)
    products = db.relationship('Product', backref='brand', cascade='all, delete-orphan')

    def __repr__(self):
        return """ID: {id} \n Name: {name} \n Description: {desc} \n Logo: {logo}""".format(
            id=self._id,
            name=self.name,
            desc=self.description,
            logo=self.logo,
        )

    def get_brand_details(self):
        return str(self)


class OrderDetails(db.Model):
    __tablename__ = "order_details"
    product_id = db.Column(db.ForeignKey("products._id"), primary_key=True)
    order_id = db.Column(db.ForeignKey("orders._id"), primary_key=True)
    product_quantity = db.Column(db.Integer)
    products = db.relationship("Product", back_populates='products')
    orders = db.relationship("Order", back_populates='orders')


class Order(db.Model):
    __tablename__ = 'orders'

    _id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False, default='CONFIRMED')
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    total_price = db.Column(db.Float)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address_line_1 = db.Column(db.String(200), nullable=False)
    address_line_2 = db.Column(db.String(200), nullable=True)
    city = db.Column(db.String(40), nullable=False)
    state = db.Column(db.String(40), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    no_contact_delivery = db.Column(db.Boolean, default=False)
    payment_type = db.Column(db.Enum(PaymentType, values_callable=lambda x: [str(p_type.value) for p_type in PaymentType]), nullable=False, default=PaymentType.PAYMENT_ON_DELIVERY)
    payment_status = db.Column(db.Enum(PaymentStatus, values_callable=lambda x: [str(p_type.value) for p_type in PaymentStatus]), nullable=False, default=PaymentStatus.PENDING)
    card_details = db.Column(db.Integer, db.ForeignKey('card_details._id'), nullable=True)
    order_number = db.Column(db.String(10), nullable=False)
    orders = db.relationship('OrderDetails', back_populates='orders')

    def __repr__(self):
        return ""

    def json(self):
        return dict(
            _id=self._id,
            status=self.status,
            payment_status=str(self.payment_status.value),
            payment_type=str(self.payment_type.value),
            card=self.card_details or None,
            order_number=self.order_number,
            no_contact_delivery=self.no_contact_delivery,
            date=self.date,
            price=self.total_price,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone_number,
            address_1=self.address_line_1,
            address_2=self.address_line_2,
            city=self.city,
            state=self.state,
            country=self.country,
            pincode=self.pincode,
        )


class CardDetails(db.Model):
    __tablename__ = 'card_details'

    _id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16), nullable=False, unique=True)
    card_expiry = db.Column(db.String, nullable=False)
    cvc = db.Column(db.Integer)
    orders = db.relationship('Order', backref='cardDetails')
