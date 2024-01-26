# Classes and Objects

Python is an object oriented programming language and every unit is considered as an object. Here, we are going into the detail of classes and objects which is one of the most important topics in Python language.

## Class

A class is a user-defined blueprint or prototype from which objects are created.

**Syntax:**

```py
class ClassName:
    #statement(s)
object = ClassName()
print(object.attribute)
```

## Object

- Object is an instance of a class.
- A class is like a blueprint while an instance is a copy of the class with actual values.

![Alt text](https://pynative.com/wp-content/uploads/2021/08/class_and_objects.jpg "Flowchart of class and object")

## Constructor

A constructor is a unique function that gets called *automatically* when an object is created from the class.
A constructor will be created as `__init__` method as shown below.

**Syntax:**

```py
class ClassName:
    def __init__():       # constructor fn definition
        #statement(s)
```

- The main purpose of a constructor is to ***assign values*** to data members of that class.
- Using constructors, we can write programs more efficiently.
For example:

```py
class laptop:
    def __init__(self):
        print("Demo")
    def display(self):
        print("Display")
hp = laptop()
```

Output will be:

```txt
demo
```