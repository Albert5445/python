def anun_decorator(func):
    def wrapper():
        print("____teachers____")
        print("---Hamlet Movsisyan---")
        print("---Vazgen Sargsyan---")
        func()
        print("____developers____")
        print("---Moso Mxitaryan---")
        print("---Hovo Simonyan---")
    return wrapper


def Avelacum():
    print("____avelacum____")
    print("---Narek Sahakyan---")
    print("---Sona Khachatryan---")

f = anun_decorator(Avelacum)
f()
