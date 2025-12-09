name = input("What is your name? ")
if name in ["yo mama", "Yo Mama", "Yo mama", "yo Mama", "Alex G", "alex G", "Alex g", "alex g", "2hollis", "pibble", "Pibble", "Jasper", "Jacqueline"]:
    print("Hush up " + name)
elif name in ["Owen", "owen", "Hamster_Ham", "hamsterham"]:
    print("Hello Owen! :)")
else: 
    print("Hello " + name + "!")

res1 = int (input("How old are you? "))
if res1 >= 17:
    print("damn " + name + ", you old asf XD")
elif res1 == 4:
    print("You are the youngest person ever!")
else:
    print("newgen")

res2 = input("What is your favorite food? ")
if res2 in ["Pizza", "pizza"]:
    print("Pizza is good, I like pizza.")
elif res2 in ["Caviar", "caviar"]:
    print("Ooooooo fancypants mcgee over here with the caviar")
elif res2 in ["Burger", "Burgers", "burger", "burgers", "Cheeseburger", "cheeseburger"]:
    print("Burgers are amazing!")

res3 = input("What do you like to do in your free time? ")
if res3 in ["Listen to music", "listen to music", "Music", "music"]:
       musinput = input("I like music too! Who is your favorite artist? ")
       if musinput in ["Alex G", "Alex g", "alex g", "alex G", "Nature TV", "Vacations", "vacations"]:
        print("Wow! I Love " + musinput + " too!")
       else:
        print("I'll have to check out " + musinput + "!")
else:
    print("That sounds fun!")

res4 = input("What is your favorite animal? ")
if res4 in ["Seals", "Seal", "seal", "seals"]:
    print("I love " + res4 + " too!")
else:
    print("Wow! " + res4 + " I never would have guessed!")

res5 = input("What is your favorite candy? ")
if res5 in ["Hot tamales", "hot tamales", "Atomic Fireballs", "Atomic fireballs", "atomic fireballs"]:
    print("I love " + res5 + " Too!")
else:
    print("Sounds yummy!")

res6 = input("Do you like sports? (Y/N) ")
for res6 in ["Yes", "yes", "Y", "y"]:
    sportres = input("Really? Which one? ")
    if sportres == ["Baseball", "baseball"]:
        print("I love " + sportres + " Too! Go Twins!!")
        continue
    else:
        print("Sounds fun!")
        continue
for res6 in ["No", "no", "N", "n"]:
    print("That's ok! Sports aren't for everyone. ")
    continue
else:
    print("Please type Y or N. ")



print("end program")