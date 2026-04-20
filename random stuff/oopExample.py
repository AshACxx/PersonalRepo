class Person:

    "This is a person class"
    name = "T-1000"

    def greet(self):
        print("Ill be back")



terminator = Person()


print(f"The terminator has the name of {terminator.name}")

terminator.greet()