while True:
    print("1. SETTINGS")
    print("2. HOME")
    print("3. PROFILE")
    print("4. EXIT")
    print("Enter Menu ID")
    command = input()

    if int(command) == 1:
        print("GO settings")
    elif int(command) == 2:
        print("Go home")
    elif int(command) == 3:
        print("Go profile")
    elif int(command) == 4:
        print("EXIT")
        break
    else:
        continue
    print("_____________________")