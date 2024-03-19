# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:45:15 2024

@author: round
"""

#Defines the animal class
class Animal():
    def __init__(self):
        self.locamotion = "walks"
    
    def eat(self):
        print("yum")
    def sleep(self):
        print("zzZZZzzz")
        

#dfines the classes one under animal
class Mammal(Animal):
    def __init__(self):
        self.birthing_method = "live"

class Bird(Animal):
    def __init__(self):
        self.birthing_method = "eggs"
        self.locamotion = "flys"

class Fish(Animal):
    def __init__(self):
        self.has_lungs = False
        self.locamotion = "swims"
 
 
#defines the classes two under animal
class Dog(Mammal):
    @staticmethod    
    def speak():
        print("bark!")

class Cat(Mammal):
    @staticmethod    
    def speak():
        print("meow!")
        
class Eagle(Bird):
    def __init__(self):
        self.locamotion = "soars"
        
class Lungfish(Fish):
    def __init__(self):
        self.has_lungs = True
        
class Jellyfish(Fish):   #although a jellyfish is not technically a fish, for the purposes of this it's close enough
    @staticmethod
    def sleep():
        print("Jellyfish cannot technically sleep")
        

Tom = Jellyfish()
Jerry = Cat()
Bald = Eagle()

Tom.sleep()

Jerry.sleep()
Jerry.speak()


print(Bald.locamotion)


 
    

        
