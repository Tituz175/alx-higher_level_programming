#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)
print(type(m.__dict__))
print(m.__dict__)


mj = class_to_json(m)
print(type(mj))
print(mj)