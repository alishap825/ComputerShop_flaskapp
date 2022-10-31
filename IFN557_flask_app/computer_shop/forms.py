from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, EmailField, BooleanField,
                     SelectField)
from wtforms.validators import InputRequired, Length, Email, ValidationError
from .enums import PaymentType


class CheckoutForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        InputRequired('First name cannot be blank'),
        Length(min=3, max=50, message='First name should be a minimum of 3 characters')
    ])
    last_name = StringField('Last Name')
    email = EmailField('Email', validators=[
        InputRequired('Email cannot be blank'),
        Email('Please enter a valid email address'),
        Length(message='Email length should be more than 2', min=2, max=128)
    ])
    phone = StringField('Phone', validators=[
        InputRequired('Phone cannot be blank'),
        Length(min=9, max=12)
    ])
    address_1 = StringField('Address Line 1', validators=[
        InputRequired('Address Line 1 cannot be blank'),
        Length(min=2, max=200)
    ])
    address_2 = StringField('Address Line 2', validators=[
        InputRequired('Address Line 2 cannot be blank'),
        Length(min=2, max=200)
    ])
    city = StringField('City', validators=[
        InputRequired('City cannot be blank'),
        Length(min=2, max=200)
    ])
    state = StringField('State', validators=[
        InputRequired('State cannot be blank'),
        Length(min=2, max=200)
    ])
    country = StringField('Country', validators=[
        InputRequired('Country cannot be blank'),
        Length(min=2, max=200)
    ])
    pincode = StringField('Pincode', validators=[
        InputRequired('Pincode cannot be blank'),
        Length(min=3, max=200)
    ])
    no_contact_delivery = BooleanField('No Contact Delivery', description='Follow Covid-19 Safety')
    payment_type = SelectField('Payment type', choices=[
        (PaymentType.PAYMENT_ON_DELIVERY.value, 'Payment On Delivery'),
        (PaymentType.CARD.value, 'Card')])

    def validate_phone(self, phone):
        try:
            p = int(phone.data)
            if not type(p) == int:
                raise ValueError()
        except ValueError:
            raise ValidationError('Invalid phone number')

    def validate_pincode(self, pincode):
        try:
            p = int(pincode.data)
            if not type(p) == int:
                raise ValueError()
        except ValueError:
            raise ValidationError('Invalid pincode')


class CardForm(FlaskForm):
    card_number = StringField('Card Number', validators=[
        InputRequired('Country cannot be blank'),
        Length(min=2, max=200)
    ])
    expiry = StringField('Expiry', validators=[
        InputRequired('Expiry cannot be blank')
    ])
    cvc = StringField('CVC', validators=[
        InputRequired('CVC cannot be blank'),
        Length(min=3, max=3)
    ])

    def validate_card_number(self, card_number):
        try:
            p = int(card_number.data)
            if not type(p) == int:
                raise ValueError()
        except ValueError:
            raise ValidationError('Invalid card number')

    def validate_cvc(self, cvc):
        try:
            p = int(cvc.data)
            if not type(p) == int:
                raise ValueError()
        except ValueError:
            raise ValidationError('Invalid CVC value')
