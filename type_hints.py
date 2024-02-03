# Nomal
price = 100
tax = 1.1

def calc_price_including_tax(price, tax):
    return int(price*tax)

if __name__=='__main__':
    print(f'{calc_price_including_tax(price=price, tax=tax)}円')

# type hints 型ヒントは、変数や関数の引数、戻り値の型を宣言するための機能

price: int = 100
tax: float = 1.1

def calc_price_including_tax(price: int, tax: float) -> int:
    return int(price*tax)

if __name__=='__main__':
    print(f'{calc_price_including_tax(price=price, tax=tax)}円')

# from typing は、Python のコードで型ヒントを使用するために必要なモジュール
from typing import List, Dirt

sample_list: List[int] = [1, 2, 3, 4]
