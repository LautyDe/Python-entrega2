class Cart():
    def __init__(self, cart_id, products=None):
        self.id = cart_id
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display_products(self):
        for product in self.products:
            print(product)


