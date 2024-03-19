# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:55:41 2024

@author: round
"""

class Employee():
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age
        
    def print_info(self):
        print(f"Name : {self.name} Age : {self.age} Position : {self.position}")
    
class SalariedEmployee(Employee):
    def Calc_Sal(self):
        if self.position == "manager":
            return 110000
        
        elif self.position == "human resources":
            return 75000
        
        elif self.position == "accountant":
            return 95000
        
class HourlyEmployee(Employee):
    def __init__(self, name, position, age, hours):
        super().__init__(name, position, age)
        self.hours = hours
        
    def Calc_Sal(self):
        if self.position == "Janitor":
            return 20 * self.hours
        elif self.position == "Reciptionist":
            return 17.5 * self.hours
        
class CommisionEmployee(Employee):
    def __init__(self, name, position, age, money_made):
        super().__init__(name, position, age)
        self.money_made = money_made
    
    def Calc_Sal(self):
        return 40000 + self.money_made * 0.35
        
    
#defines several employees
Sal = SalariedEmployee("Sal", "manager", 49)
Hal = HourlyEmployee("hal", "Janitor", 24, 960)
Pal = CommisionEmployee("Pal", "sales-person", 49, 50000)
Cal = HourlyEmployee("Cal", "Reciptionist", 35, 1680)
Dal = SalariedEmployee("Dal", "accountant", 58)

#defines a list of those employees
Employee_list = [Sal, Hal, Pal, Cal, Dal]

for i in range(len(Employee_list)):
    print(Employee_list[i].Calc_Sal())
