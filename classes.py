class Goya:
    def say_about_you(self):
        print("My name is " + self.name)


r1 = Goya
r1.name = "Albert"
r1.age = 21
r1.profetion = "programer"


r1.say_about_you()