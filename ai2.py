age=input("Сколько вам лет?")
age=int(age)
if 1<=age<=4:
    print("Слишком маленький,пора в садик!")

if 5<=age<=8:
    print("Откуда ты взял деньги?")

if 9<=age<=12:
    print("Подожди,вырости немного")
if 13<=age<=16:
    withp=input("С родителями?")
    if withp=="да":
        print("Приятного просмотра!")
    else:
        print("Только с родителями")

if age>=17:
    print("Вот ваши билеты!Приятного просмотра!")



