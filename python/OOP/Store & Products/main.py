import store

product_shop = store.Store("shop_product_list")
product_shop.add_product("melon")
product_shop.add_product("apple",100,"fruit")
product_shop.add_product("banana",50,"fruit")
product_shop.add_product("banana",50,"fruit")
product_shop.add_product("peach",30,"fruit")
product_shop.add_product("tomato",85,"vege")
product_shop.add_product("potato",70,"vege")
product_shop.add_product("corn",100,"vege")
product_shop.info_display()

product_shop.sell_product(1)
product_shop.info_display()

print("inflation:")
product_shop.inflation(0.05)
product_shop.info_display()

print("Clearance:")
product_shop.set_clearance("vege",0.1)
product_shop.info_display()
