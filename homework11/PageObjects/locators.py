from selenium.webdriver.common.by import By


class AdminPageLocators:
    DESCRIPTION_ACTIONS = (By.CSS_SELECTOR, '.panel-heading')
    USER_NAME = (By.CSS_SELECTOR, '#input-username')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    HELP_BLOCK = (By.CSS_SELECTOR, '.help-block')
    BTN_LOGIN = (By.CSS_SELECTOR, 'button')


class CardProductPageLocators:
    IMAGES_PRODUCT = (By.CSS_SELECTOR, '.col-sm-8 ul.thumbnails li')
    REFERENCES = (By.CSS_SELECTOR, '.nav.nav-tabs')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'h1')
    PROPERTY_PRODUCT = (By.CSS_SELECTOR, '.col-sm-4 .list-unstyled')
    BTN_ADD_TO_CARD = (By.CSS_SELECTOR, '#product button')


class MainPageLocators:
    OPENCART_SIGNATURE = (By.CSS_SELECTOR, 'footer .container p a')
    SEARCH_LINE = (By.ID, 'search')
    BUCKET = (By.ID, 'cart')
    SWIPER_WRAPPER_PRODUCTS = (By.CSS_SELECTOR, '#slideshow0 .swiper-wrapper')
    MACBOOK_AIR_POSTER = (By.CSS_SELECTOR, '.swiper-slide-active [alt="MacBookAir"]')
    IPHONE6_POSTER = (By.CSS_SELECTOR, '.swiper-slide-active [alt="iPhone 6"]')


class RegistrationUserLocators:
    BTNS_SUBSCRIBE = [(By.CSS_SELECTOR, 'fieldset'), (By.CSS_SELECTOR, '.col-sm-10')]
    PRIVACY_POLICY_CHECKPOINT = (By.CSS_SELECTOR, '[type=checkbox]')
    BTN_CONTINUE = (By.CSS_SELECTOR, '[type=submit]')


class ProductPageLocators:
    MENU = (By.CSS_SELECTOR, '#menu')
    CATALOG_REF = (By.CSS_SELECTOR, '#menu-catalog [data-toggle="collapse"]')
    PRODUCTS_CATEGORY = (By.CSS_SELECTOR, '.collapse.in li')
    BTN_ADD_NEW_PRODUCT = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, '.alert')


class AddProductPageLocators:
    GENERAL_TAB = (By.CSS_SELECTOR, '[href="#tab-general"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
    META_TEG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA_TAB = (By.CSS_SELECTOR, '[href="#tab-data"]')
    MODEL = (By.CSS_SELECTOR, '#input-model')
    BTN_SAVE = (By.CSS_SELECTOR, '.pull-right .btn.btn-primary')


class DelProductPageLocator:
    CHECKBOX_PRODUCT = (By.CSS_SELECTOR, '.table.table-bordered tbody input')
    BTN_DELETE = (By.CSS_SELECTOR, '.btn-danger')


class RegistrationPageLocators:
    DROPDOWN_FOR_REG = (By.CSS_SELECTOR, '#top-links .dropdown')
    BTN_REGISTRATION = (By.CSS_SELECTOR, '.dropdown-menu.dropdown-menu-right a')
    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    E_MAIL = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    BTN_CONTINUE = (By.CSS_SELECTOR, '.btn-primary')
    CHECKBOX_PRIVACY = (By.CSS_SELECTOR, '[type="checkbox"]')
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, '#content h1')


class CurrencyLocators:
    BTN_CURRENCY = (By.CSS_SELECTOR, '.btn-link.dropdown-toggle')
    CURRENT_CURRENCY = (By.CSS_SELECTOR, '.btn-link.dropdown-toggle strong')
    NEW_CURRENCY = (By.CSS_SELECTOR, '.btn-link.dropdown-toggle strong')
    US_DOLLAR = (By.CSS_SELECTOR, '[name="USD"]')
    POUND_STERLING = (By.CSS_SELECTOR, '[name="GBP"]')
    EURO = (By.CSS_SELECTOR, '[name="EUR"]')

class CatalogLocators:
    CATALOG = (By.CSS_SELECTOR, '#column-left .list-group')
