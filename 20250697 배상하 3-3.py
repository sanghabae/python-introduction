weight = float(input("몸무게를 kg 단위로 입력하세요 --> "))
height = float(input("키를 미터 단위로 입력하세요 --> "))
bmi = (weight / (height**2))
print("당신의 BMI =", bmi)
if bmi >=30:
    print("비만입니다.")
elif 24.99 <= bmi <= 29.99:
        print("과체중입니다.")
elif 18.5 <= bmi <= 24.99:
        print("정상입니다.")
else:
        print("저체중입니다.")
