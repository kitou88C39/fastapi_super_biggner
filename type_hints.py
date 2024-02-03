# Nomal
price = 100
tax = 1.1

def calc_price_including_tax(price, tax):
    return int(price*tax)

if __name__=='__main__':
    print(f'{calc_price_including_tax(price=price, tax=tax)}円')

# type hints

price: int = 100
tax: float = 1.1

def calc_price_including_tax(price: int, tax: float):
    return int(price*tax)

if __name__=='__main__':
    print(f'{calc_price_including_tax(price=price, tax=tax)}円')