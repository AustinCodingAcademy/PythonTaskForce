# Plain ol data object
class Person:
    def __init__(self, name, age, street_address):
        """
        Create a new person
        :param string name: Person's full name
        :param int age: Person's age
        :param string street_address: This is their street address
        :return:
        """
        self.person_name = name
        self.age = age
        self.street_address = street_address

    def get_address(self):
        """
        This method gives us the person's address
        :return: string
        """
        return self.street_address


class Product:
    def __init__(self, product_name, product_category, product_price):
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price
        self.discount_amount = 0.00

    def set_discount(self, discount_amt):
        """
        Setting the discount property
        :param discount_amt:
        :return: None
        """
        self.discount_amount = discount_amt

    def get_price(self):
        """
        This gives us the product price and takes the discount into consideration.
        :return:
        """
        return self.product_price - self.discount_amount


class Order:
    def __init__(self, ObjPerson, listOfProducts):
        self.ObjPerson = ObjPerson
        self.listOfProducts = listOfProducts

        if len(listOfProducts) == 0:
            raise Exception('Must pass list of Products')

    def place_order(self):
        """
        This method will place the order, send the email, charge the card etc..etc...
        :return: bool
        """
        num_items = 0
        order_total = 0.00
        order_discount = 0.00

        for product in self.listOfProducts:
            order_total = order_total + product.get_price()
            num_items += 1
            order_discount = order_discount + product.discount_amount

        # Print out line items, like an old skool receipt
        for product in self.listOfProducts:
            print "%s\t\t%s\t\t%.2f" % (product.product_name, product.product_category, product.product_price)

        print "\t\t\tDiscount Amount: %.2f" % order_discount
        print "\t\t\tTotal Amount: %.2f" % order_total


if __name__ == "__main__":
    shopper = Person('Samir', 30, '5421 Hickory Dr')

    firstProduct = Product('Nike Shox', 'Shoes', 54.99)
    firstProduct.set_discount(5.00)  # This is called a setter : ) please use me ^_^

    secondProduct = Product('MacBook Pro', 'Laptop', 1450.00)
    thirdProduct = Product('Keyboard', 'Laptop', 15.00)

    # Put these products in a list
    products = [firstProduct, secondProduct, thirdProduct]

    newOrder = Order(shopper, products)
    newOrder.place_order()