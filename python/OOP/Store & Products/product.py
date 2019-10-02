class Product:
    def __init__(self, name, price, category, uid):
        self.name = name;
        self.price = price
        self.category = category
        self.uid = uid
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price *= (1+percent_change)
        elif is_increased == False:
            self.price *= (1-percent_change)
        return self.price
    def print_info(self):
        print("name: "+self.name+", category: "+self.category+",  price: "+str(self.price)+", uid:"+str(self.uid))
