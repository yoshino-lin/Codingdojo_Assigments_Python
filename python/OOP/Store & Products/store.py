import product
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product, price = 0, category= "none",uid=-1):
        if uid<0:
            uid=len(self.products)+1
        self.products.append(product.Product(new_product,price,category,uid))
    def sell_product(self, id):
        for i in range(len(self.products)-1):
            if self.products[i].uid == id:
                print("uid: "+str(self.products[i].uid)+",name: "+self.products[i].name+" is removed")
                del self.products[i]
    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase,True)
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount,False)
    def info_display(self):
        for i in range(len(self.products)):
            self.products[i].print_info()
