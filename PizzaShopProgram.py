#!/usr/bin/python
#
# JulioGomez
#
# This program will help the customer create their own pizza and see if they enjoy it
#

#right here we imported the PizzaShop object
import PizzaShop




#here i defined the customer questions
def customer_questions():
    """
    this function will be asking the user all their questions about their pizza
    :return:
    """
#this right here im basically pulling the Pizza from the PizzaShop object
    customer_pizza = PizzaShop.Pizza()

    customer_pizza.set_pizza_size()

    print "For pizza size you chose: " + customer_pizza.pizza_size

    customer_pizza.set_pizza_sauce()

    print "For the sauce you chose: " + customer_pizza.pizza_sauce

    customer_pizza.set_pizza_toppings()

    print "For the toppings you picked: " + customer_pizza.pizza_toppings

    customer_pizza.set_pizza_vegetables()

    print "For the vegetables you picked: " + customer_pizza.pizza_vegetables

#this is just going to print a bunch of blank lines so the code from above doesnt cluster with what the customer ordered
    for i in range(0, 20):
        print ""
#this right here is just printing out the characteristics of the customers pizza
    print "Congrats you have just ordered a " + customer_pizza.pizza_size.lower() + " pizza with " \
          + customer_pizza.pizza_sauce.lower() + "" " sauce, " + customer_pizza.pizza_toppings.lower() + " and "\
          + customer_pizza.pizza_vegetables.lower() + ", sounds delicious!"

    print "You have " + str(customer_pizza.total_slices) + " total slices of pizza. ENJOY!"

def main():
    """
    this is the main function it basically just running the customer questions function
    :return:
    """
    customer_questions()


main()
