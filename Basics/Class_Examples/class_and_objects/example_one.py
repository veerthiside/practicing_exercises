class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o


    def do_work(self):
        if self.occupation == "tennis player":
            print(f"{self.name} plays tennis.")
        elif self.occupation == "actor":
            print(f"{self.name} plays a role in movies.")

    def speaks(self):
        print(f"{self.name} says, how are you?")

tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova", "tennis player")
maria.do_work()
maria.speaks()