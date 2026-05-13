from product import Product

class Cart:
    '''
    Represent a shopping cart that stores products and 
    calculates the total price.

    This class manages a collection of Product objects, supports adding and 
    removing items, and automatically persists the contents to a text file.
    '''

    def __init__(self, filepath: str = 'cart.txt') -> None:
        '''
        Initialize the cart with an empty product list and a file path.

        :param filepath: Path to the file where cart contents are saved.
        '''
        self._products = []
        self._total_price = 0
        self._filepath = filepath
    
    def __str__(self) -> str:
        '''
        Return a user-readable string representation of the cart contents.

        :return: A list of products with index numbers and the total price.
        '''
        if not self._products:
            return 'Корзина пуста.'

        result = 'Содержимое корзины:'
        for i, product in enumerate(self._products, 1):
            result += f'\n{i}) {product}'

        result += f'\n\nОбщая стоимость корзины: {self._total_price} руб.'

        return result

    def _save_to_file(self) -> None:
        '''
        Save the current list of products to the text file.

        The file is overwritten on every change to keep it synchronized.
        '''
        with open(self._filepath, 'w', encoding='utf-8') as file:
            for product in self._products:
                file.write(f'{product}\n')

    def add_product(self, product: Product) -> None:
        '''
        Add a product to the cart and update the total price.

        :param product: An instance of the Product class to be added.
        '''
        if not isinstance(product, Product):
            print(f'{product} не Product')
            return
        
        self._products.append(product)
        self._save_to_file()
        self._total_price += product.get_price()

    def remove_product(self, barcode: int) -> bool:
        '''
        Remove a product from the cart by its barcode.

        :param barcode: The unique barcode identifier of the product.
        :return: True if the product was found and removed, False otherwise.
        '''
        for product in self._products:
            if product.get_barcode() == barcode:
                self._products.remove(product)
                self._save_to_file()
                self._total_price -= product.get_price()
                return True
        return False