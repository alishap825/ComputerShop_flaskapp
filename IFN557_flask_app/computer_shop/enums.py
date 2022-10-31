from enum import Enum


class BasketAction(Enum):
    ADD_TO_BASKET = 'add'
    REMOVE_FROM_BASKET = 'remove'


class ProductCategory(Enum):
    LAPTOP = 'laptop'
    ACCESSORY = 'accessory'
    DESKTOP = 'desktop'


class PaymentType(Enum):
    PAYMENT_ON_DELIVERY = 'POD'
    CARD = 'Card'


class FilterType(Enum):
    CATEGORY = 'category'
    BRAND = 'brand'


class PaymentStatus(Enum):
    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
