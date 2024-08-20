"*************************canteen menu************************"
import platform
import os
def myclear():
 if platform.system()=="Windows":
    print(os.system("cls"))
def intromain():
     myclear()
     print("**********CANTEEN******MANAGEMENT****SYSTEM******PROJECT*******************")
     print("***************************************************************************")

def intro():
    print("****************************CANTEEN-MANAGEMENT*************************")
    print("===========================================================")
    print("****************************S=Y=S=T=E=M********************************")
    print("PROJECT:Canteen Management System")
    print("MADE BY :Soham Nandy and Tushar Sharma")
    print("---------------SCHOOL : ARMY PUBLIC SCHOOL BENGDUBI--------------------")

def main():
    ch=0
    myclear()
    intromain()
    print("=================MAIN MENU====================")
    print("01. PRODUCTS REPORT GENERATOR")
    print("02. ADMINISTRATOR")
    print("03. EXIT")
    print("==============================================")
    ch=int(input("Please Select Your Option (1-3)"))
    return ch

def middleadminmenu():
    ch=0
    intromain()
    print("===========CUSTOMER'S-PRODUCT'S MENU===========")
    print("01. CUSTOMER'S MENU")
    print("02. PRODUCT'S MENU")
    print("03. CANTEEN SALE MENU")
    print("04. BACK TO MAIN")
    print("==============================================")
    ch=int(input("Please Select Your Option (1-4) "))
    return ch
def canteen_menu():
    ch=0
    intromain()
    print("===========CANTEEN SALE MENU===========")
    print("01. ADD CUSTOMER PURCHASE")
    print("02. MODIFY CUSTOMER PURCHASE")
    print("03. DELETE CUSTOMER PURCHASE")
    print("04. BACK TO MAIN")
    print("==============================================")
    ch=int(input("Please Select Your Option (1-4) "))
    return ch
def admin_menu1():
    ch=0
    myclear()
    intromain()
    print("=================ADMIN MENU====================")
    print("1.CREATE CUSTOMERS DETAILS")
    print("2.DISPLAY ALL CUSTOMERS DETAILS")
    print("3.SEARCH RECORD(QUERY) ")
    print("4.MODIFY CUSTOMERS RECORDS")
    print("5.DELETE CUSTOMERS RECORDS")
    print("6.BACK TO MAIN MENU")
    ch=int(input("Please Enter Your Choice (1-6) "))
    return ch
"""***************************************************************
 ADMINSTRATOR PRODUCT FUNCTION
****************************************************************"""
def admin_menu():
    ch=0
    myclear()
    intromain()
    print("=================ADMIN MENU====================")
    print("1.CREATE PRODUCTS")
    print("2.DISPLAY ALL PRODUCTS AVAILABEL")
    print("3.SEARCH RECORD(QUERY) ")
    print("4.MODIFY PRODUCTS")
    print("5.DELETE PRODUCTS")
    print("6.DISPLAY ALL INVOICES PAID OR NOT PAID")
    print("7.BACK TO MAIN MENU")
    ch=int(input("Please Enter Your Choice (1-7) "))
    return ch
"""**********************************************************
MODIFY MENU
********************************************************"""
def modify_menu():
    ch=0
    myclear()
    intromain()
    print("===============MODIFY MENU==================")
    print("1.MODIFY CUSTOMER NAME")
    print("2.MODIFY CUSTOMER ADDRESS")
    print("3.MODIFY CUSTOMER PHONE NUMBER")
    print("4.BACK TO MAIN MENU")
    ch=int(input("Please Enter Your Choice (1-4) "))
    return ch
"""**********************************************************
 MODIFY MENU
********************************************************"""
def modify_prodmenu():
    ch=0
    myclear()
    intromain()
    print("===============MODIFY PRODUCT MENU==================")
    print("1.MODIFY PRODUCT NAME")
    print("2.MODIFY PRODUCT COMPANY")
    print("3.MODIFY PRODUCT PRICE")
    print("4.MODIFY PRODUCT QUANTITY")
    print("5.MODIFY PRODUCT DISCOUNT")
    print("6.MODIFY PRODUCT PURCHASE DATE")
    print("7-MODIFY PRODUCT INVOICE PAID OR NOT PAID")
    print("8.BACK TO MAIN MENU")
    ch=int(input("Please Enter Your Choice (1-8) "))
    return ch

"""*********************************************************
REPORT MENU
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def reportmenu():
    ch=0
    myclear()
    intromain()
    print("===============REPORTS MENU==================")
    print("1.DISPLAY ALL CUSTOMER INVOICE")
    print("2.DISPLAY CUSOMER INVOICE BY INVOICE NUMBER")
    print("3.DISPLAY ALL CUSTOMER INVOICE DATEWISE")
    print("4.DISPLAY ALL THE PRODUCT INVOICE")
    print("5.DISPLAY PRODUCT INVOICE BY INVOICE NUMBER")
    print("6.DISPLAY ALL PRODUCT INVOICE DATEWISE")
    print("7.BACK TO MAIN MENU")
    ch=int(input("Please Enter Your Choice (1-7) "))
    return ch
