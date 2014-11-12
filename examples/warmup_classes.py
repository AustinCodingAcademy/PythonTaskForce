class Person:
    def __init__(self, name, age, street_address):
        """

        :param name:
        :param age:
        :param street_address:
        :return:
        """
        self.person_name = name
        self.age = age
        self.street_address = street_address

    def get_address(self):
        """
        This method gives us the person's name
        :return: string
        """
        return self.street_address

class Product:
    def __init__(self, product_name, product_category, product_price):
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price

class Order:
    def __init__(self, ObjPerson, listOfProducts):
        self.ObjPerson = ObjPerson
        self.istOfProducts = listOfProducts

if __name__ == "__main__":

    shopper = Person('Paco, 28, 8021 N FM620')

    firstProduct = Product('Nike Shox', 'Shoes', 54.99)
    thirdProduct = Product('Keyboard', 'Laptop', 15.00)

    # Put these products in a list