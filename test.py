class product:
    def __init__(self,name,unitprice,getperc,quantity):
        self.name=name
        self.unitprice=unitprice
        self.getperc=getperc
        self.quantity=quantity

class shopbasket:
    class __init__(self,name):
        self.product=[]
        self.name=leatherwallet
        self.name=umbrella
        self.name=cigarette
        self.name=honey        
class unitprice:
    class __init__(self,shopbasket):
        self.leatherwallet=1100
        self.umbrella=900
        self.cigarette=200
        self.honey=100
class gstperc:
    class __init__(self,shopbasket):
        self.leatherwallet=18
        self.umbrella=12
        self.cigarette=28
        self.honey=0

def calcutedisc(shopbasket):
    if product.unitprice>500:
        disc=5/unitprice*100
    else:
        disc=0
return disc
def calcgst(shopbasket):
    gstprice=gstperc/unitprice*100
return gstprice
def finalprice:
    total=product.unitprice+product.gstprice-product.disc
print("the total price is")
print(total)    


