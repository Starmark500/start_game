age=input("Сколько вам лет?")
age=int(age)
if age<=4 and age>=1:
    print("Слишком маленький,пора в садик!")

if age>=5 and age<=8:
    print("Откуда ты взял деньги?")

if age>=9 and age<=12:
    print("Подожди,вырости немного")
if age>=13 and age<=16:
    withp=input("С родителями?")
    if withp=="да":
        print("Приятного просмотра!")
    else:
        print("Только с родителями")

if age>=17:
    print("Вот ваши билеты!Приятного просмотра!")



