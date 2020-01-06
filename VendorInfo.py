

class Vendor:

    def __init__(self,vid,vnm):
        self.vendorRegNo=vid
        self.vendorName=vnm
        self.venderproducts=[]
        self.vendorAddress=set()

    def __str__(self):
        return '--------------------------------\n VendorId : {}, ' \
               'VenderName : {},' \
               '\n Products : {}' \
               '\n Addresses : {}' \
               '\n Account : {}'.format(self.vendorRegNo,self.vendorName,self.venderproducts,self.vendorAddress,self.account)

vendor1 = Vendor("REG10293324389","Flipkart")

class Product:

    def __init__(self,pid,pnm,pqty,pcat,pprice=500):
        self.productId=pid
        self.productName=pnm
        self.productPrice=pprice
        self.productQty=pqty
        self.productCategory=pcat

    def __str__(self):
        return '\n ID : {} Name : {}, Qty : {}, Price : {}'.format(self.productId,self.productName,self.productQty,self.productPrice)

    def __repr__(self):
        return str(self)

p1 = Product(pid=101,pnm="Mobile",pqty=3,pprice=52939.3,pcat="YT")
p2 = Product(pid=152,pnm="Laptop",pqty=4,pprice=29349.3,pcat="TY")
p3 = Product(pid=133,pnm="Charger",pqty=8,pprice=9339.3,pcat="XX")
p4 = Product(pid=134,pnm="Desktop",pqty=2,pprice=22939.3,pcat="AA")
p5 = Product(pid=125,pnm="TV",pqty=9,pprice=19139.3,pcat="A")
products = [p1,p2,p3,p4,p5]
#print(products)
vendor1.venderproducts.extend(products)



class Address:

    def __init__(self,flat,society,city,state,country,pincode):
        self.flatNo = flat
        self.societyName=society
        self.cityName=city
        self.stateName=state
        self.countryName=country
        self.areaPin=pincode

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return self.flatNo and self.societyName.__hash__()

    def __eq__(self, other):
        return self.flatNo==other.flatNo and self.societyName==other.societyName


ad1 = Address(flat=1111,society="ABC",city="Pune",state="MH",country="India",pincode=881046)
ad2 = Address(flat=1211,society="XXX",city="Bglore",state="MH",country="India",pincode=534046)
ad3 = Address(flat=3411,society="XYZ",city="Chennai",state="MH",country="India",pincode=611046)
ad4 = Address(flat=1211,society="XXX",city="Pune",state="MH",country="India",pincode=47046)
#print(addressList)
vendor1.vendorAddress.add(ad1)
vendor1.vendorAddress.add(ad2)
vendor1.vendorAddress.add(ad3)
vendor1.vendorAddress.add(ad4)


#print(vendor1)

class Account:

    def __init__(self,aid,atype,abal):
        self.accountNo=aid
        self.accountType=atype
        self.accountBalnce=abal

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)

a1= Account(11223344,"Current",150000.32)
vendor1.account=a1

#print(vendor1)


class Customer:

    def __init__(self,cid,cnm,cadr,cacc):
        self.customerId=cid
        self.customreName=cnm
        self.customerAddress=cadr
        self.customerAccount=cacc
        self.purchaselist=[]

    def __str__(self):
        return f'\n\n---------------Customer Details---------------------\n {self.__dict__}'

    def __repr__(self):
        return str(self)

custad = Address(flat=9911,society="PPP",city="Pune",state="MH",country="India",pincode=991046)
custAcc= Account(9993344,"Saving",25000.32)
cust = Customer(11223,"AAAA",custad,custAcc)
#print(cust)



class FlipkartServices:

    def purchase_products(self,pname,pcat,pqty,cust):#stock cat qty custbal

        if type(pname)==str and len(pname)>=2 and type(pqty)==int and pqty>=1:
            product_found=False
            product_qty=False
            product_cat=False

            whichProduct = None

            for product in vendor1.venderproducts:
                if product.productName==pname:
                    product_found=True
                    if product.productCategory==pcat:
                        product_cat=True
                        if product.productQty>=pqty:
                            product_qty=True
                            whichProduct=product
                            break


            #ABC

            if product_qty==True: #C
                print('product avlb')
                totalBill = whichProduct.productPrice*pqty
                print('------------Before Trascation -----------------')
                print(vendor1.account.accountBalnce)
                print(cust.customerAccount.accountBalnce)
                print(cust.purchaselist)
                print(whichProduct)
                print('------------Trascation -----------------')
                if totalBill<=cust.customerAccount.accountBalnce:
                    cust.customerAccount.accountBalnce-=totalBill
                    vendor1.account.accountBalnce+=totalBill

                    custProduct = Product(pid=whichProduct.productId,pnm=whichProduct.productName,
                            pqty=pqty,pprice=whichProduct.productQty,pcat=whichProduct.productCategory)

                    cust.purchaselist.append(custProduct)
                    whichProduct.productQty-=pqty
                    print('Trascation Successful....!')
                    print(vendor1.account.accountBalnce)
                    print(cust.customerAccount.accountBalnce)
                    print(cust.purchaselist)
                    print(whichProduct)
                else:
                    print('insufficient balance')

            elif product_qty==False and product_cat==True:
                print('Product qty not avlbl')
            elif product_cat==False and product_found==True:
                print('product cat not found')
            elif product_found==False:
                print('product not found')
        else:
            print('INvalid date ...cannot process...!')

    def refundProducts(self):
        pass
        # all product fields from customer to inventory --- ALL*


'''

p1 = Product(pid=101,pnm="Mobile",pqty=3,pprice=52939.3,pcat="YT")
    p2 = Product(pid=152,pnm="Laptop",pqty=4,pprice=29349.3,pcat="TY")
p3 = Product(pid=133,pnm="Charger",pqty=8,pprice=9339.3,pcat="XX")
p4 = Product(pid=134,pnm="Desktop",pqty=2,pprice=22939.3,pcat="AA")
p5 = Product(pid=125,pnm="TV",pqty=9,pprice=19139.3,pcat="A")

'''


services = FlipkartServices()
services.purchase_products("Charger","XX",2,cust)
