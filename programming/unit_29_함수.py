"""
사칙연산 함수 만들기
덧셈, 뺄셈, 나눗셈의 결과가 나오도록 해라.
이 때 나눗셈의 결과는 실수로 출력되어야 한다.
입력은 한번에 '10 20' 으로 받는다.
"""


def calculator():
    num = input().split()
    print(f'덧셈 : {int(num[0]) + int(num[1])}')
    print(f'뺄셈 : {int(num[0]) - int(num[1])}')
    print(f'나눗셈 : {float(num[0]) / float(num[1])}')


if __name__ == '__main__':
    calculator()
