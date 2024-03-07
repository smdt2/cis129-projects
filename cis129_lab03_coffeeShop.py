#!/usr/bin/env python
# coding: utf-8
#Costumer imput
print('****************************************')

print("Gigi's cafe")

print("Number of coffees bought?")

coffees = int(input("Enter the number of coffees:"))

print("Number of Cookies bought?")

cookies = int(input("Enter the number of cookies:"))

print("Number of teas bought?")

teas = int(input("Enter the number of teas:"))

print("Number of croissants bought?")

croissants = int(input("Enter the number of croissants:"))

print('**************************************** \n \n****************************************')

print("Gigi's cafe receipt")

#Calculations
coffee_price = 3.99

total_coffee = (coffees * coffee_price)

cookie_price = 2

total_cookie = (cookies * cookie_price)

tea_price = 3

total_tea = (teas * tea_price)

croissant_price = 4

total_croissant = (croissants * croissant_price)

total_cost_before_tax = (coffees * coffee_price) + (cookies * cookie_price) + (croissants * croissant_price) + (teas * tea_price)

sales_tax = total_cost_before_tax * 0.06

total_cost_after_tax = total_cost_before_tax + sales_tax
#Results
print(f"{coffees} Coffees at ${coffee_price} each: $ {total_coffee}")

print(f"{cookies} Cookies at ${cookie_price} each: $ {total_cookie}")

print(f"{teas} Teas at ${tea_price} each: $ {total_tea}")

print(f"{croissants} Cookies at ${croissant_price} each: $ {total_croissant}")

print(f"6% tax: ${sales_tax}")

print("------")

print(f"Total: ${total_cost_after_tax}")

print('****************************************')

print("THANK YOU FOR YOUR PURCHASE")
