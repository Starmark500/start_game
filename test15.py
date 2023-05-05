import random
number=random.randint(1,100)
popitki=1

answer=input("Угадай число,попытка номер "+ str(popitki))
if answer=="Сдаюсь":
    print("Твое число "+ str(number))
    exit()
answer=int(answer)

while number!=answer:
    if answer == "Сдаюсь":
        print("Твое число " + str(number))
        exit()
    answer = int(answer)
    if answer > 100 or answer < 0:
        answer=input("Данное число не подходит ,попробуйте сново.")
        continue
    if number>answer:
        popitki+=1

        answer=input("Мое число больше! попытка номер "+ str(popitki))
        continue

    if number<answer:
        popitki+=1

        answer=input("Мое число меньше! попытка номер " + str(popitki))

        continue







if number == answer:
    print("Ты угадал!Ты угадал с " + str(popitki))







