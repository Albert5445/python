class Robpot:
    def introduce_self(self, ):
        print("My name is " + self.name )

r1 = Robpot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30



r2 = Robpot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight= 40

r1.introduce_self()
r2.introduce_self()