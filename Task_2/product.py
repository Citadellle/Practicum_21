from ean_13_data import EAN_COUNTRY_CODES

class Product:
    '''
    Represents a product with a name, price, and barcode.

    Automatically determines the country of origin based on 
    the EAN-13 barcode prefix.
    '''

    def __init__(self, name: str, price: float, barcode: int) -> None:
        '''
        Initialize a new Product instance.

        :param name: The name of the product.
        :param price: The price of the product.
        :param barcode: The 13-digit barcode of the product.
        '''
        self._name = name
        self._price = price
        self._barcode = barcode
        self._country = self._get_country_by_barcode()
    
    def __str__(self) -> str:
        '''
        Return a user-friendly string representation of the product.

        :return: A formatted string containing name, 
        price, barcode, and country.
        '''
        return (f'Товар: {self._name} ; '
                f'Цена: {self._price} руб. ; '
                f'Штрих-код: {self._barcode} ; '
                f'Страна выпуска: {self._country}')
    
    def __repr__(self) -> str:
        '''
        Return an official string representation of the product.

        :return: A string representation for debugging purposes.
        '''
        return (f'Товар: {self._name} ; '
                f'Цена: {self._price} руб. ; '
                f'Штрих-код: {self._barcode} ; '
                f'Страна выпуска: {self._country}')

    def _get_country_by_barcode(self) -> str:
        '''
        Extract the country of origin from the barcode prefix.

        :return: Country name or 'Неизвестная страна' if 
        the code is not found.
        '''
        country_code = str(self._barcode)[:3]
        return EAN_COUNTRY_CODES.get(country_code, 'Неизвестная страна')

    def get_name(self) -> str:
        '''Get the current product name.'''
        return self._name
    
    def set_name(self, name: str) -> None:
        '''Set a new product name.'''
        self._name = name

    def get_price(self) -> float:
        '''Get the current product price.'''
        return self._price
    
    def set_price(self, price: int) -> None:
        '''
        Set a new product price.

        Validates that the price is not negative.
        :param price: The new price to set.
        '''
        if price < 0:
            print('Цена не может быть отрицательной')
        self._price = float(price)

    def get_barcode(self) -> int:
        '''Get the current barcode.'''
        return self._barcode
    
    def set_barcode(self, barcode: int) -> None:
        '''
        Set a new barcode and update the country of origin.

        :param barcode: The new 13-digit barcode.
        '''
        self._barcode = barcode
        self._country = self._get_country_by_barcode()

    def get_country(self) -> str:
        '''Get the country of origin.'''
        return self._country