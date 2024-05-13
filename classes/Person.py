class Person():
    def __init__(self, _id, name, age):
        self._id = _id
        self.name = name
        self.age = age
        self.products = []

    def __str__(self):
        return f'My id is {self._id} and this is my cart {self.products}'
    
    def __len__(self):
        return len(self.products)

    def add_to_cart(self, product):
        self.products.append(product)

    def remove_from_cart(self, product):
        self.products.remove(product)

    def buy(self):
      print("Purchase successful!")
      self.products = []

