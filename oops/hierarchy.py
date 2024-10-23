class shop:
    def grocery(s):
        print("ITEMS")
    def stationary(s):
        print("STATIONARY")  
class staff(shop):  
    def distribution(s):
        print("DISTRIBUTE")
    def other_services(s):
        print("OTHERS")
class customer(shop):
    def buy(s):
        print("BUY")        
             

cus1=customer()
cus1.grocery()
cus2=staff()
cus2.stationary()

            