# At first glance, it may seem that there is too much code, 
# but I justify it by the fact that the products in the store are not fixed, they can be changed 
# and everything will work the same without changing the code(only the main store).
# Moreover, you can write both the name of the product and just the number


# All goods are stored in the store
store = {
    'coke': 2.5,
    'water': 1.5,
    'chips': 1.75,
    'chocolate': 2,
}

# Here will be all the products you are going to buy
basket = []


# Function of menu


def menu():

    index = 0
    print('**********MENU**********')
    print('Choose your product')

    for name, price in store.items():
        index += 1
        print(str(index) + '.', name.capitalize(), '--', str(price) + '$')

    index += 1
    print(f'{index}.', 'Pay')

    index += 1
    print(f'{index}.', 'Show store')

    index += 1
    print(f'{index}.', 'EXIT')

    print('************************')


# Function works with choice and return price of all

def choose(choose, count):
    choose = choose.lower()
    if choose in store:
        basket.append([choose, store[choose]])
        count += store[choose]
        print('<<<<<<<<<<<<<<<<<<<')
        print('Product added to basket!!')
        print('<<<<<<<<<<<<<<<<<<<')
        print('\n')
    else:
        print('<<<<<<<<<<<<<<<<<<<')
        print('Invalid input')
        print('<<<<<<<<<<<<<<<<<<<')
        print('\n')
    return count


# fuction of payment

def pay(deposit, count):
    if not deposit.isdigit():
        print('Invalid input')
        return

    deposit = float(deposit)

    rest = deposit - count
    if rest >= 0:
        print('-------------------')
        print('Payment succsess')
        print('your rest:', rest)
        print('-------------------')
        basket.clear()
        return 0
    else:
        print('This money not enougth')
        return rest


# function show basket
def showBasket(basket, total):
    if len(basket):
        for el in basket:
            print(f'Your product {el[0]}, price: {el[1]}')
        print('Total:', total)
    else:
        print('Basket empty')

# main function


def main():

    # price of all goods
    count = 0

    storeKeys = list(store.keys())

    while True:
        menu()

        product = input('Write your choice: ').lower()

        if product == 'pay' or (product.isdigit() and int(product) == len(storeKeys) + 1):
            deposit = input('Put deposit: ')
            count = pay(deposit, count)

        elif product == 'show store' or (product.isdigit() and int(product) == len(storeKeys) + 2):
            showBasket(basket, count)

        elif product == 'exit' or (product.isdigit() and int(product) == len(storeKeys) + 3):
            return

        else:
            if product.isdigit() and int(product) <= len(storeKeys):
                count = choose(storeKeys[int(product) - 1], count)
            else:
                count = choose(product, count)

            print('<<<<<<<<<<<<<<<<<<<')
            print(f'your price: {count}')
            print('<<<<<<<<<<<<<<<<<<<')
            print('\n')


main()
