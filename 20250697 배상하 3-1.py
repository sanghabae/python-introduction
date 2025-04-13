number = int(input("정수를 입력하세요 -->"))
original = number
total = 0
if number > 0:
    while number > 0:
        total = total + number % 10
        number = number // 10
    print("{} 자리수의 합: {}".format(original, total))
