import random
weather=random.choice(["погода ясная"])
princess=random.choice(["принцесса прекрасная","принцесса ужасная"])
# princess=random.choice(["принцесса ужасная",])
hunger=random.choice(["великан не голоден","великан очень голоден"])


print(weather)
print(princess)
print(hunger)
if weather=="погода ясная":
    if princess=="принцесса прекрасная":
        print("Принцесса пошла гулять...но тут")
        print("Великан безжалостно расправляется с маленькой прекрасной принцессой")

    else:
        print("Принцесса пошла гулять...но тут")
        if hunger=="великан очень голоден":
            print("Великан ест принцессу не задумываясь")

        else:
            print("Принцесса безжалостно расправляется с маленьким великаном")


