"""
문자열은 한 줄로 저장되어 있다.
words.txt 파일에서 c가 포함 된 단어를
각 줄에 순서대로 출력하는 프로그램을 만들어라.
(점(.)과 콤마(,)는 출력하지 않는다.)
"""


def file():
    with open('./data/words.txt', 'r') as file:
        txt = file.read()
        word = txt.replace(',', '').split()
    for i in word:
        if i.find('c') != -1 or i.find('C') != -1:
            print(i)
        else:
            pass


if __name__ == '__main__':
    file()
