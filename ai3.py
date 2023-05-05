age=input("Сколько вам лет?")
age=int(age)
if age<=4 and age>=1:
    print("Слишком маленький,пора в садик!")

elif age<=8:
    print("Откуда ты взял деньги?")

elif age<=12:
    print("Подожди,вырости немного")
elif age<=16:
    withp=input("С родителями?")
    if withp=="да":
        print("Приятного просмотра!")
    else:
        print("Только с родителями")

else:
    print("Вот ваши билеты!Приятного просмотра!")



