class Parent:
    def __init__(self, arg1):
        self.arg1 = arg1


class Child(Parent):
    def stuff(self):
        print(f"thats theargument: {self.arg1}")
