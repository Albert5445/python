print("_____MENU_____")
print("1. HOME")
print("2. SETTINGS")
print("3. PROFILE")
print("4. EXIT")

comand = 2
login = True

if comand == 1:
    print("You are in Home")
elif comand == 2 :
    print("You are in Settings")
elif comand == 3 and login == True:
    print("You Entered your profile")
else:
    print("Something is wrong Exit ")