def coupon():
    price = int(input())
    sale = input()
    if sale == 'Cash3000' or sale == 'Cash 5000':
        print(price - int(sale[-4:]))
    else:
        print('입력 오류')


if __name__ == '__main__':
    coupon()
