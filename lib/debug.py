#!/usr/bin/env python3


from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee


coffee = Coffee("Vanilla Latte")
steve = Customer("Steve")
dima = Customer("Dima")
Order(steve, coffee, 2.0)
Order(steve, coffee, 4.0)
Order(dima, coffee, 5.0)
Order(dima, coffee, 2.0)



print(Customer.most_aficionado(coffee))













