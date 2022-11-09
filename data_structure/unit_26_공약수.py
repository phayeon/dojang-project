"""
공약수의 합 구하기
두 숫자의 공약수의 합이 결과로 나오도록 해라.
입력은 한번에 '10 20' 으로 받는다.
"""

def multiple():
    num = input().split()
    num1, num2 = int(num[0]), int(num[1])
    result = []
    for i, j in zip(range(1, num1), range(1, num2)):
        if (num1 % i == 0 and num2 % i == 0) or (num1 % j == 0 and num2 % j == 0):
            result.append(i)
        else:
            pass
    print(sum(result))


if __name__ == '__main__':
    multiple()
