# he reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

# In more clear way you can say that SELF has following Characteristic-

#     Self is always pointing to Current Object.

# it is clearly seen that self and obj is referring to the same object


class check:
    def __init__(self):
        print("Address of self = ", id(self))


obj = check()
print("Address of class object = ", id(obj))

# this code is Contributed by Samyak Jain

# Another Example of Using SELF:
class car:
    # init method or constructor
    def __init__(self, model, color, type):
        self.model = model
        self.color = color
        self.type = type

    def show(self):

        print("Model is", self.model)
        print("color is", self.color)
        print("type is ", self.type)


# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue", "coupé")
ferrari = car("ferrari 488", "green", "break")

audi.show()  # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)

# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)

# Self is the first argument to be passed in Constructor and Instance Method.

# Self must be provided as a First parameter to the Instance method and constructor. If you don’t provide it, it will cause an error.

# Self is always required as the first argument
class check:
    def __init__(self):
        print("This is Constructor")


object = check()
print("Worked fine")


# # Following Error is produced if Self is not passed as an argument
# Traceback (most recent call last):
# File "/home/c736b5fad311dd1eb3cd2e280260e7dd.py", line 6, in <module>
# 	object = check()
# TypeError: __init__() takes 0 positional arguments but 1 was given


# this code is Contributed by Samyak Jain
