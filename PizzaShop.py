#!/usr/bin/python
#
#JulioGomez
#
#this program will help the customer build his own pizza and eat it as well as ask him if they enjoy it
#

class Pizza:

    pizza_size = None
    pizza_sauce = None
    pizza_toppings = None
    pizza_vegetables = None
    total_slices = None

    def __init__(self, size=None, sauce=None, toppings=None, vegetables=None, total_slices=None):
        """
        :param size:
        :param sauce:
        :param toppings:
        :param vegetables:
        :return:
        """
        self.pizza_size
        self.pizza_sauce
        self.pizza_toppings
        self.pizza_vegetables
        self.total_slices

    def set_pizza_vegetables(self):
        """
        these are the veggies on the pizza
        :param vegetables:
        :return:
        """
        #this is the list of veggies, and yes i know some pineapple is a fruit
        pizza_vegetables = ["Pineapple", "Onions", "Peppers", "Zucchini"]
        #this asks the user to enter what vegetable they want, they only get 1 choice
        vegetables = raw_input("Enter the vegetable you would like: Pineapple, Onions, Peppers, Zucchini ").title()
        #this while loops checks if the vegetable that the user typed is not in the pizza_vegetables variable then itll
        #keep asking over and over again until they type in a vegetable in that list
        while vegetables not in pizza_vegetables:
            vegetables = raw_input("Enter one of the vegetable choices: ").title()

        self.pizza_vegetables = vegetables

    def set_pizza_toppings(self):
        """
        these are the toppings on the pizza
        :param toppings:
        :return:
        """
        #this is the list of toppings
        pizza_toppings = ["Bacon", "Sausage", "Pepperoni", "Chicken", "Ham", "Turkey"]
        #this asks the user what topping they want, only get 1 topping
        toppings = raw_input("Enter the topping you want on your pizza: Bacon, Sausage, Pepperoni, Chicken, Ham, Turkey ").title()
        #this while loop does checks if toppings isnt in pizza toppings itll repeat itself until user types one in the list
        while toppings not in pizza_toppings:
            toppings = raw_input("Enter one of the topping choices: ").title()

        self.pizza_toppings = toppings

    def set_pizza_sauce(self):
        """
        this is what sauce is on the pizza
        :param sauce:
        :return:
        """
        #this is the list of sauces
        pizza_sauces = ["Marinara", "Garlic", "Alfredo"]
        #this ask the user their sauce
        sauce = raw_input("Enter the sauce you want on your pizza: Marinara, Garlic, Alfredo ").title()
        #this checks if sauce in pizza sauces if not itll repeat till the user picks something in the pizza sauces list
        while sauce not in pizza_sauces:
            sauce = raw_input("Enter one of the sauce choices: ").title()

        self.pizza_sauce = sauce

    def set_pizza_size(self):
        """
        this is the size of the pizza
        :param size:
        :return:
        """
        #these are the pizza sauces
        pizza_sizes = {"Small": 4, "Medium": 6, "Large": 8}
        #this ask user for sauce
        size = raw_input("Enter the size of your pizza: Small, Medium, Large ").title()
        #this checks if the size in pizza sizes if not itll repeat till user chooses something in pizza sizes list
        while size not in pizza_sizes:
                size = raw_input("Enter one of the size choices: ").title()

        self.total_slices = pizza_sizes.get(size)

        self.pizza_size = size
