from cart import Cart
from product import Product

def load_products_from_file(filename: str = 'products.txt') -> list:
    '''
    Load products from a text file.

    Reads a file where each line contains product data separated by semicolons
    and creates a list of Product instances.

    :param filename: Path to the file with product data.
    :return: A list of loaded Product objects.
    '''
    products = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            name, price, barcode = line.strip().split(';')
            product = Product(name, float(price), int(barcode))
            products.append(product)

    return products

def show_products(products: list) -> None:
    '''
    Display the list of available products.

    :param products: A list of Product instances.
    '''
    print('Ассортимент товаров:')
    for index, product in enumerate(products, 1):
        print(f'{index}) {product}')

def main() -> None:
    '''
    Main application loop for managing the shopping cart interactively.
    '''
    products = load_products_from_file()
    cart = Cart()

    run = True
    while run:
        print('\nМеню:')
        print('1. Показать товары')
        print('2. Добавить товар в корзину')
        print('3. Удалить товар из корзины')
        print('4. Посмотреть корзину')
        print('0. Выход')

        choice = input('\nВыберите пункт меню: ')

        match choice:
            case '1':
                show_products(products)

            case '2':
                show_products(products)
                number: int = int(input('Введите номер товара: '))

                if 1 <= number <= len(products):
                    cart.add_product(products[number - 1])
                    print('Товар добавлен в корзину.')
                else:
                    print('Неверный номер товара.')

            case '3':
                print(cart)
                barcode = int(input(
                    'Введите штрих-код товара для удаления: '))

                if cart.remove_product(barcode):
                    print('Товар удалён из корзины.')
                else:
                    print('Товар не найден в корзине.')

            case '4':
                print(cart)

            case '0':
                print('Выход из программы.')
                run = False

            case _:
                print('Неверный пункт меню.')


if __name__ == '__main__':
    main()