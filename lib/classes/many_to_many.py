class Coffee:

    def __init__(self, name):
        self.name = name
        print(f"The coffee {self.name} was made")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name") and isinstance(new_name, str) and len(new_name) >= 3:
            self._name = new_name
        else:
            raise Exception("the coffee name must be of type string and can not be reset after being created.")
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len([order for order in self.orders()])
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(self.orders())
    

class Customer:


    def __init__(self, name):
        self.name = name
        print(f"{self.name} entered the shop")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception("The name must be of type string, and between 1 and 15 characters!")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def most_aficionado(coffee):
        top_orders = {}
        for order in coffee.orders():
            if order.customer not in top_orders:
                top_orders[order.customer] = [order.price]
            else:
                top_orders[order.customer].append(order.price)
        top_c = None
        top_p = 0
        for customer, price in top_orders.items():
            print(top_orders)
            # print(f"{customer} | {price}")
            if sum(price) > top_p:
                top_c = customer
                top_p = sum(price)
            print(top_c._name , top_p)
        return top_c

            


    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.all.append(self)
        print(f"{self.customer.name} bought the {self.coffee.name} at the price of {self.price}")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_cust):
        if isinstance(new_cust, Customer):
            self._customer = new_cust
        else:
            raise Exception("The customer must of instance class Customer")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception("The coffee must be of instance class Coffee")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not hasattr(self, "_price") and isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
            self._price = new_price
        else:
            raise Exception("the price must be of type Float, and between 1.0 and 10.0 dollars.")