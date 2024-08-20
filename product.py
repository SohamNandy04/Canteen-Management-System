"""**********************************************
PRODUCT (product.py)
**********************************************"""
import mysql.connector
import os
import datetime
"""***************************************************************
CLASS USED IN PROJECT ****************************************************************
*******************
product information
*************************"""
class product:
    def __init__(self):
        self.__prod_id=0
        self.__prodname=" "
        self.__prod_comp=" "
        self.__prod_price=0
        self.__prod_qty=0
        self.__prod_dis=0
        self.__prod_DOP=0 #----date of purchase
        ##----------Public functions
        #-----------modify product details starts
        # ----to set the values---------
    def setprodid(self,pid):
        self.__prod_id=int(pid)
    def setprodnm(self,pnm):
        self.__prodname=pnm
    def setprodcmpy(self,cpy):
        self.__prod_comp=cpy
    def setprodpr(self,pr):
        self.__prod_price=int(pr)
    def setprodqty(self,qty):
        self.__prod_qty=int(qty)
    def setproddis(self,ds):
        self.__prod_dis=int(ds)
    def setproddate(self,dt):
        self.__prod_DOP=dt
    #*****************Product TO BE MODIFIED ENDS HERE
    def getprodid(self):
        return self.__prod_id
    def getprodnm(self):
        return self.__prodname
    def getprodcompy(self):
        return self.__prod_comp
    def getprodpr(self):
        return self.__prod_price
    def getprodqty(self):
        return self.__prod_qty
    def getproddis(self):
        return self.__prod_dis
    def getproddate(self):
        return self.__prod_DOP
    def prod_input(self,pid):
        print("======================================================================")
        print("PROD NO:")
        self.__prod_id=pid
        print(self.__prod_id)
        self.__prodname=input("NAME OF PRODUCT:")
        self.__prod_comp=input("NAME OF PRODUCT COMPANY:")
        self.__prod_price=int(input("PRODUCT PRICE:"))
        self.__prod_qty=int(input("PRODUCT QUANTITY:"))
        self.__prod_dis=int(input("PRODUCT DISCOUNT:"))
        self.__prod_DOP=input("PRODUCT DATE(yyyy-mm-dd) OF PURCHASED:")
        print("=====================================================================")
    def show_product(self):
        print("======================================================================")
        print("PROD NO:",self.__prod_id)
        print("NAME OF PRODUCT:",self.__prodname)
        print("PRODUCT COMPANY:",self.__prod_comp)
        print("PRODUCT PRICE:",self.__prod_price)
        print("PRODUCT QUANTITY:",self.__prod_qty)
        print("PRODUCT DISCOUNT:",self.__prod_dis)
        print("DATE OF PURCHASED:",self.__prod_DOP)
        print("=====================================================================")
    def showallprod(self):
        print(self.__prod_id,"\t",self.__prodname,"\t ",self.__prod_comp,"\t ",self.__prod_price,"\t\t",self.__prod_qty,"\t ",self.__prod_dis,"\t ",self.__prod_DOP)
    def showproddatamulti(self):
        print("======================================================================")
        print("PROD NO:",self.__prod_id)
        print("NAME OF PRODUCT:",self.__prodname)
        print("PRODUCT COMPANY:",self.__prod_comp)
        print("PRODUCT PRICE:",self.__prod_price)
        print("PRODUCT QUANTITY:",self.__prod_qty)
        print("PRODUCT DISCOUNT:",self.__prod_dis)
        print("DATE OF PURCHASED:",self.__prod_DOP)
        print("=====================================================================")
def getprodname(prid):
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="canteensys")
    #print(mydb)
    mycursor=mydb.cursor()
    query=("SELECT prod_nm FROM product WHERE prodid=%s")
    data=(prid,)
    mycursor.execute(query,data)
    rc=mycursor.fetchone()
    tmp=rc[0]
    mycursor.close()
    mydb.close()
    return tmp
def giveprodno():
    count=1000
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="canteensys")
    print(mydb)
    mycursor=mydb.cursor()        
    query=("SELECT COUNT(*) FROM product")
    q=("SELECT MAX(prodid) FROM product")
    mycursor.execute(query)
    rc=mycursor.fetchone()
    tmp=rc[0]
    print(tmp)
    if tmp==0:
        count=5001
    else:
        q=("SELECT MAX(prodid) FROM product")
        mycursor.execute(q)
        rc=mycursor.fetchone()
        count=rc[0]
        count=count+1
    mycursor.close()
    mydb.close()
    return count
        #---------------GET INVOICE NUMBER
def giveprodINVOICEno():
    count=1
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="canteensys")
    print(mydb)
    mycursor=mydb.cursor()
    query=("SELECT COUNT(*) FROM product_invoice")
    q=("SELECT MAX(prodinv_id) FROM product_invoice")
    mycursor.execute(query)
    rc=mycursor.fetchone()
    tmp=rc[0]
    print(tmp)
    if tmp==0:
        count=1
    else:
        q=("SELECT MAX(prodinv_id) FROM product_invoice")
        mycursor.execute(q)
        rc=mycursor.fetchone()
        count=rc[0]
        count=count+1
    mycursor.close()
    mydb.close()
    return count
    #---------------INVOICE NUMBER
def writeprod_invodata(prid,pr_nm,pr_dt,pr_qty,prdstat,prdinvo):
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        n=giveprodINVOICEno()
        Query=("INSERT INTO product_invoice VALUES(%s,%s,%s,%s,%s,%s,%s)")
        if prdstat=="PAID" or prdstat=="Paid" or prdstat=="paid":
            data=(n,prid,pr_nm,pr_dt,pr_qty,"CASH or CHEQUE",prdinvo)
        else:
            data=(n,prid,pr_nm,pr_dt,pr_qty,"NOT PAID",prdinvo)
        C.execute(Query,data)
        conn.commit()
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
def writeproddata():
    try:
        pobj=product()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        Query=("INSERT INTO product VALUES(%s,%s,%s,%s,%s,%s,%s)")
        no=giveprodno()
        pobj.prod_input(no)
        prdinvo=int(input("Enter the Invoice no:"))
        prdstat=input("Enter the status PAID or NOT PAID")
        now = pobj.getproddate()
        data=(pobj.getprodid(),pobj.getprodnm(),pobj.getprodcompy(),pobj.getprodpr(),pobj.getprodqty(),pobj.getproddis(),now)
        C.execute(Query,data)
        conn.commit()
        C.close()
        conn.close()
        writeprod_invodata(pobj.getprodid(),pobj.getprodnm(),now,pobj.getprodqty(),prdstat,prdinvo)
    except mysql.connector.Error as err:
        print(err)
        conn.close()        
            #------to display all the products\
def displaallproddata():
    try:
        pobj=product()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        Query=("SELECT * FROM product")
        C.execute(Query)
        rc=C.fetchall()
        print("PRODID\tPRODNAME\tCOMPANY\tPRODPRICE\tPRODQTY\tDISCOUNT\tDATEOFPURCHASE")
        for x in rc:
            pobj.setprodid(x[0])
            pobj.setprodnm(x[1])
            pobj.setprodcmpy(x[2])
            pobj.setprodpr(x[3])
            pobj.setprodqty(x[4])
            pobj.setproddis(x[5])
            pobj.setproddate(x[6])
            pobj.showallprod()
            input("press the key")
            os.system('cls')
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-------search and display the product record
def searchdisplayproddata():
    try:
        pobj=product()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        no=int(input("ENTER PRODUCT ID"))
        Query=("SELECT * FROM product WHERE prodid=%s")
        data=(no,)
        C.execute(Query,data)
        rc=C.fetchone()
        print("PRODID\tPRODNAME\tCOMPANY\tPRODPRICE\tPRODQTY\tDISCOUNT\tDATEOFPURCHASE")
        pobj.setprodid(rc[0])
        pobj.setprodnm(rc[1])
        pobj.setprodcmpy(rc[2])
        pobj.setprodpr(rc[3])
        pobj.setprodqty(rc[4])
        pobj.setproddis(rc[5])
        pobj.setproddate(rc[6])
        pobj.showallprod()
        input("press the key")
        os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
    #-------to search and update the product name
def search_mod_prodnm():
    try:
    #pobj=product()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER PROD ID"))
        pnm=input("Enter the prod name")
        Query=("UPDATE product SET prod_nm=%s WHERE prodid=%s")
        data=(pnm,pno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-------to search and update the product company name
def search_mod_prodcompy():
    try:
        #pobj=product()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER PROD ID"))
        pcnm=input("Enter the new company name")
        Query=("UPDATE product SET prod_company=%s WHERE prodid=%s")
        data=(pcnm,pno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-------to search and update the product price
def search_mod_prodprice():
    try:
        #cobj=customer()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        cno=int(input("ENTER PROD ID"))
        cph=input("Enter the new price")
        Query=("UPDATE product SET prod_price=%s WHERE prodid=%s")
        data=(cph,cno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-------to search and update the product qty
def search_mod_prodqty():
    try:
        #cobj=customer()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER PROD ID"))
        pqty=int(input("Enter the add more qty"))
        prdate=input("Enter the purchase date(yyyy-mm-dd)")
        prdinvo=int(input("Enter the Invoice no:"))
        prdstat=input("Enter the status PAID or NOT PAID")
        Query=("UPDATE product SET prod_qty=prod_qty+%s WHERE prodid=%s")
        data=(pqty,pno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
        prnm=getprodname(pno)
        writeprod_invodata(pno,prnm,prdate,pqty,prdstat,prdinvo)
    except mysql.connector.Error as err:
        print(err)
        conn.close()
    #-------to search and update the product discount
def search_mod_proddiscount():
    try:
        #cobj=customer()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER PROD ID"))
        pdis=int(input("Enter the new discount"))
        Query=("UPDATE product SET prod_discount=%s WHERE prodid=%s")
        data=(pdis,pno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-------to search and update the product purchase date
def search_mod_proddate():
    try:
        #cobj=customer()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER PROD ID"))
        pdt=input("Enter the modified date of purchase")
        Query=("UPDATE product SET prod_purchasedt=%s WHERE prodid=%s")
        data=(pdt,pno)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-------to search and delete the product
def search_del_prod():
    try:
        #cobj=customer()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER PROD ID"))
        Query=("DELETE FROM product WHERE prodid=%s")
        data=(pno,)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
def search_updt_invoice():
    try:
        #cobj=customer()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER INVOICE NO"))
        Query=("SELECT * FROM product_invoice WHERE prodinv_invoiceno=%s")
        data=(pno,)
        C.execute(Query,data)
        row_count = C.rowcount
        rc=C.fetchone()
        C.close()
        conn.close()
        if rc:
            print("PRODID\tPRODNAME\tDATE\tPRODQTY\tSTATUS\tINVOICENO")
            print(rc[1],"\t",rc[2],"\t",rc[3],"\t",rc[4],"\t",rc[5],"\t",rc[6])
            if rc[5] == "NOT PAID" or rc[5] == "not paid" or rc[5] == "Not Paid":
                chstat=input("want to pay by CASH OR CHEQUE(Y/N)")
                if chstat=="y" or chstat=="Y":
                    setstatus(pno,"CASH or CHEQUE")
                else: print("Please Pay and clear the bill")
        else: print("not such invoice exists")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
def setstatus(pno1,st):
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        Query=("UPDATE product_invoice SET prodinv_status=%s WHERE prodinv_invoiceno=%s")
        data=(st,pno1)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
def showallprodinvoice():
    try:
        #cobj=customer()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pno=int(input("ENTER PROD NO"))
        Query=("SELECT * FROM product_invoice WHERE prodid=%s")
        data=(pno,)
        C.execute(Query,data)
        rc=C.fetchall()
        if rc:
            print("PRODID\tPRODNAME\t\t DATE\t\tPRODQTY\tSTATUS\t\tINVOICENO")
            for x in rc:
                print(x[1],"\t",x[2],"\t\t",x[3],"\t\t",x[4],"\t",x[5],"\t\t",x[6])
        else:
            print("not such invoice exists")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()