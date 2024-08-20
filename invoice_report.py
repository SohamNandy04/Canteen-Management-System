import mysql.connector
import os
import datetime
import product as pr
#----------create customer purchase records
def cust_purchase():
    #-----search and display the customer record
    try:
        pobj=pr.product()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        cno=int(input("ENTER CUST ID"))
        Query=("SELECT * FROM customer WHERE custid=%s")
        data=(cno,)
        C.execute(Query,data)
        rc=C.fetchone()
        if rc:
            tmpcustid=rc[0]
            tmpcustnm=rc[1]
            print("CUSTID\tCUSTNAME\tCUSTADDRESS\tCUSTPHONE")
            print(rc[0],"\t",rc[1],"\t",rc[2],"\t",rc[3])
            C.close()
            cinv=int(input("ENTER THE INVOICE NO"))
            cdt=input("Enter the invoice date(yyyy-mm-dd)")
            #---------------search for products
            while True:
                pr.displaallproddata()
                prno=int(input("ENTER THE PROD ID"))
                conn=connection.MySQLConnection(user='root' ,password='root',host='localhost' ,database='canteensys')
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
                qt=int(input("Enter the quantity"))
                addcustinvoice(int(rc[0]),rc[1],qt,int(rc[3]),cinv,cdt,tmpcustid,tmpcustnm)
                wantmore=input("press (y-yes to continue) or (n-No to exit)")
                if wantmore=="n" or wantmore=="N":
                    break
                os.system('cls')
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-----search and display the customer record
        #---------search the invioce and modify the product quantity
    def modify_purchase():
        tmp=0
        t=0
        try:
            pobj=pr.product()
            conn=mysql.connector.connect(user='root' ,password='',host='localhost' ,database='canteensys')
            C=conn.cursor()
            ino=int(input("ENTER INVOICE ID"))
            Query=("SELECT prodid,prod_nm,prod_qty,prod_pr,prod_totprice FROM customer_invoice WHERE cust_invoice=%s")
            data=(ino,)
            C.execute(Query,data)
            rc=C.fetchall()
            if rc:
                print("PRODID\t\tPROD NAME\t\tQUANTTY\t\tPRICE\t\tTOTAL PRICE")
                for x in rc:
                    print(x[0],"\t\t",x[1],"\t\t",x[2],"\t\t",x[3],"\t\t",x[4])
                    ch=input("Do yo want to modify quantity(Y/N)")
                    if ch=="y" or ch=="Y":
                        nqty=int(input("Enter new Quantity:"))
                        if nqty>int(x[2]):
                            tmp=nqty-int(x[2])
                            q=("UPDATE product SET prod_qty=prod_qty-%s WHERE prodid=%s")
                            d=(tmp,x[0])
                            C.execute(q,d)
                            t=nqty*int(x[3])
                            q=("UPDATE customer_invoice SET prod_qty=prod_qty+%s,prod_totprice=%s WHERE prodid=%s AND cust_invoice=%s")
                            d=(tmp,t,x[0],ino)
                            C.execute(q,d)
                            conn.commit()
                            print(C.rowcount, "record(s) affected")
                        else:
                            tmp=int(x[2])-nqty
                            q=("UPDATE product SET prod_qty=prod_qty+%s WHERE prodid=%s")
                            d=(tmp,x[0])
                            C.execute(q,d)
                            t=nqty*int(x[3])
                            q=("UPDATE customer_invoice SET prod_qty=prod_qty-%s,prod_totprice=%s WHERE prodid=%s AND cust_invoice=%s")
                            d=(tmp,t,x[0],ino)
                            C.execute(q,d)
                            conn.commit()
                            print(C.rowcount, "record(s) affected")
            else: input("-------invoice number not found!!!")
            os.system('cls')
            C.close()
            conn.close()
        except mysql.connector.Error as err:
            print(err)
            conn.close()
            #---------search the invioce and modify the product quantity
            #---------search the invoice and delete the record
def delete_purchase():
    tmp=0
    t=0
    try:
        pobj=pr.product()
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        ino=int(input("ENTER INVOICE ID"))
        Query=("SELECT prodid,prod_nm,prod_qty,prod_pr,prod_totprice FROM customer_invoice WHERE cust_invoice=%s")
        data=(ino,)
        C.execute(Query,data)
        rc=C.fetchall()
        if rc:
            print("PRODID\t\tPROD NAME\t\tQUANTTY\t\tPRICE\t\tTOTAL PRICE")
            for x in rc:
                print(x[0],"\t\t",x[1],"\t\t",x[2],"\t\t",x[3],"\t\t",x[4])
                ch=input("Do yo want to delete quantity(Y/N)")
                if ch=="y" or ch=="Y":
                    #nqty=int(input("Enter new Quantity:"))
                    #if nqty>int(x[2]):
                    tmp=int(x[2])
                    q=("UPDATE product SET prod_qty=prod_qty+%s WHERE prodid=%s")
                    d=(tmp,x[0])
                    C.execute(q,d)
                    #t=nqty*int(x[3])
                    q=("DELETE FROM customer_invoice WHERE prodid=%s AND cust_invoice=%s")
                    d=(x[0],ino)
                    C.execute(q,d)
                    conn.commit()
                    print(C.rowcount, "record(s) affected")
                else:
                    input("-------invoice number not found!!!")
                    os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #---------search the invoice and delete the record
        #----------create customer purchase records
def addcustinvoice(pid,pname,pqty,pprice,invoice,invoicedt,cid,cnm):
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        n=givecustINVOICEno()
        Query=("INSERT INTO customer_invoice VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(n,pid,pname,pqty,pprice,pqty*pprice,invoice,"PAID CHEQUE OR CASH",cid,cnm,invoicedt)
        C.execute(Query,data)
        C.close()
        C=conn.cursor()
        Query=("UPDATE product SET prod_qty=prod_qty-%s WHERE prodid=%s")
        data=(pqty,pid)
        C.execute(Query,data)
        conn.commit()
        print(C.rowcount, "record(s) affected")
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #----- #---------------GET customer INVOICE NUMBER
def givecustINVOICEno():
    count=1
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="canteensys")
    print(mydb)
    mycursor=mydb.cursor()
    query=("SELECT COUNT(*) FROM customer_invoice")
    q=("SELECT MAX(custinv_id) FROM customer_invoice")
    mycursor.execute(query)
    rc=mycursor.fetchone()
    tmp=rc[0]
    print(tmp)
    if tmp==0:
        count=1
    else:
        q=("SELECT MAX(custinv_id) FROM customer_invoice")
        mycursor.execute(q)
        rc=mycursor.fetchone()
        count=rc[0]
        count=count+1
        mycursor.close()
        mydb.close()
        return count
    #---------------customerINVOICE NUMBER
    #----------display all customer invoice
def report_all_custinv():
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        Query=("SELECT * FROM customer_invoice")
        C.execute(Query)
        rc=C.fetchall()
        print("INVOICENO\tPRODNAME\tQTY\tPRODPRICE\tCUST_NAME\t\tINV_DATE\t\tSTATUS")
        #---prodid,prod_nm,prod_qty,prod_pr,prod_totprice,cust_invoice,custinv_status,custid,cust_nm,invoice_date
        for x in rc:
            #print (x)
            print(x[6],"\t ",x[2],"\t",x[3],"\t",x[5],"\t ",x[9],"\t\t",x[10],"\t",x[7])
            input("press the key")
            os.system('cls')
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #----------display all customer invoice
def report_all_custinv_date():
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        dt=input("Enter the date of invoice(yyyy-mm-dd)")
        Query=("SELECT * FROM customer_invoice WHERE invoice_date=%s")
        data=(dt,)
        C.execute(Query,data)
        rc=C.fetchall()
        print("INVOICENO\tPRODNAME\tQTY\tPRODPRICE\tCUST_NAME\t\tINV_DATE\t\tSTATUS")
        #---prodid,prod_nm,prod_qty,prod_pr,prod_totprice,cust_invoice,custinv_status,custid,cust_nm,invoice_date
        for x in rc:
            #print (x)
            print(x[6],"\t ",x[2],"\t",x[3],"\t",x[5],"\t ",x[9],"\t\t",x[10],"\t",x[7])
            input("press the key")
            os.system('cls')
            C.close()
            conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #-------------product invoice
def report_all_prodinv():
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        Query=("SELECT * FROM product_invoice")
        C.execute(Query)
        rc=C.fetchall()
        print("INVOICENO\t\tPRODNAME\t\tQTY\tPURCHASE DATE\t\t STATUS")
        #---prodid,prodinv_nm,prodinv_date,prodinv_qty,prodinv_status,prodinv_invoiceno
        for x in rc:
        #print (x)
            print(x[6],"\t\t",x[2],"\t\t",x[4],"\t",x[3],"\t\t",x[5])
            input("press the key")
            os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
    #---------------DISPLAY ALL PRODUCT INVOICE DATEWISE
def report_all_prodinv_date():
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        dt=input("Enter the date of invoice(yyyy-mm-dd)")
        Query=("SELECT * FROM product_invoice WHERE prodinv_date=%s")
        data=(dt,)
        C.execute(Query,data)
        rc=C.fetchall()
        print("INVOICENO\t\tPRODNAME\t\tQTY\tPURCHASE DATE\t\t STATUS")
        #---prodid,prodinv_nm,prodinv_date,prodinv_qty,prodinv_status,prodinv_invoiceno
        for x in rc:
        #print (x)
            print(x[6],"\t\t",x[2],"\t\t",x[4],"\t",x[3],"\t\t",x[5])
            input("press the key")
            os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
    #---------report of particular product
def report_prod_invno():
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        pid=input("Enter the Product no:")
        Query=("SELECT p.prod_nm,p.prod_company,p.prod_qty,pinv.prodinv_qty,pinv.prodinv_invoiceno,pinv.prodinv_date,pinv.prodinv_status,p.prod_price FROM product p,product_invoice pinv WHERE p.prodid=pinv.prodid And p.prodid=%s")
        data=(pid,)
        C.execute(Query,data)
        rc=C.fetchall()
        print("*****************************************************************")
        print("PRODUCT ID:\t",pid,"\t\t\t\t","PRODUCT NAME:\t",rc[0][0])
        print("PRODUCT COMPANY:\t",rc[0][1],"\t\t\t\tTOTAL QUANTITY:",rc[0][2])
        print("*****************************************************************")
        print("INVOICENO\tDATE-OF-INVOICE\t\t\tSTATUS\t\tADDED QTY\t| AMOUNT |")
        print("*****************************************************************")
        sum1=0
        for x in rc:
            tmp=int(x[3])*int(x[7])
            sum1=sum1+tmp
            print(x[4],"\t\t",x[5],"\t",x[6],"\t\t",x[3],"\t\t ",tmp)
            print("-----------------------------------------------------------------")
            print("----------------------------------------------------TOTAL:\t",sum1)
            print("-----------------------------------------------------------------")
            input("press the key")
            os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        #---------report of customer invoice
def report_cust_invno():
    try:
        conn=mysql.connector.connect(user='root' ,password='root',host='localhost' ,database='canteensys')
        C=conn.cursor()
        cid=input("Enter the Customer no:")
        dt=input("Enter the Date(yyyy-mm-dd)")
        Query=('''SELECT C.custid,C.custname,C.custadd,C.cusrphno,Cinv.prod_nm,Cinv.prod_qty,Cinv.prod_pr,Cinv.cust_invoice,Cinv.custinv_status,
               cinv.invoice_date FROM customer C,customer_invoice Cinv WHERE C.custid=Cinv.custid AND C.custid=%s AND Cinv.invoice_date=%s''')
        data=(cid,dt)
        C.execute(Query,data)
        rc=C.fetchall()
        print("*******************************INVOICE*************************************")
        print("CUST ID:\t",cid,"\t\t\t\t","CUSTOMER NAME:\t",rc[0][0])
        print("INVOICE DATE:\t",dt,"\t\tADDRESS :",rc[0][2],"\t\tPHNO.",rc[0][3])
        print("***************************************************************************")
        print("INVOICENO\tQUANTITY\t\t\tSTATUS\t\tPROD NAME\t\t | AMOUNT |")
        print("***************************************************************************")
        sum1=0
        for x in rc:
            tmp=int(x[5])*int(x[6])
            sum1=sum1+tmp
            print(x[7],"\t\t",x[5],"\t",x[8],"\t\t",x[4],"\t\t\t ",tmp)
            print("==========================================================================")
            print("-----------------------------------------------------------TOTAL:\t\t",sum1)
            print("--------------------------------------------------------------------------")
            input("press the key")
            os.system('cls')
        C.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)
        conn.close()
        







        
