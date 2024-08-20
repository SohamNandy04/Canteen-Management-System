import canteen_menu as CM
import customers as cust
import product as pr
import invoice_report as inv_rp
import sys
#from mysql.connector import (connection)
#-----------------product menu
#------------------customer menu
def modifyprodshow():
    choice1=" "
    choice1=CM.modify_prodmenu()
    while True:
        if choice1==1:
            #-----to search and update product name
            pr.search_mod_prodnm()
            break
        elif choice1==2:
            #-------to search and update the product company name
            pr.search_mod_prodcompy()
            break
        elif choice1==3:
            #-------to search and update the product price
            pr.search_mod_prodprice()
            break
        elif choice1==4:
            #-------to search and update the product qty
            pr.search_mod_prodqty()
            break
        elif choice1==5:
            #-------to search and update the product discount
            pr.search_mod_proddiscount()
            input("-----press any key--------")
            break
        elif choice1==6:
            #-------to search and update the product purchase date
            pr.search_mod_proddate()
            break
        elif choice1==7:
            pr.search_updt_invoice()
            input("-----------press any key------------")
            break
        elif choice1==8:
            main()
        else:
            print("Enter the correct choice")
            input("Enter any key to continue")
            modifyprodshow()
                #-----------------product menu
def product_show():
    choice1=" "
    choice1=CM.admin_menu()
    while True:
        if choice1==1:
            #-------to enter the record of product
            pr.writeproddata()
            break
        elif choice1==2:
            #-------to display all the records of product
            pr.displaallproddata()
            break
        elif choice1==3:
            #-------search and display
            pr.searchdisplayproddata()
            break
        elif choice1==4:
            #----modify the record
            modifyprodshow()
            break
        elif choice1==5:
            #------delete the record
            pr.search_del_prod()
            input("-----press any key--------")
            break
        elif choice1==6:
            pr.showallprodinvoice()
            input("-------press any key-------")
            break
        elif choice1==7:
            main()
        else:
             print("Enter the correct choice")
             input("Enter any key to continue")
             product_show()
            #------------------customer menu
def cust_show():
    choice1=" "
    choice1=CM.admin_menu1()
    while True:
        if choice1==1:
            #-------to enter the record of customer
            cust.writecustdata()
            break
        elif choice1==2:
            #-------to display all the records of customer
            cust.displaallcustdata()
            break
        elif choice1==3:
            #-------search and display
            cust.searchdisplaycustdata()
            break
        elif choice1==4:
            #----modify the record
            modifyshow()
            break
        elif choice1==5:
            #------delete the record
            cust.search_del_cust()
            input("-----press any key--------")
            break
        elif choice1==6:
            main()
        else:
            print("Enter the correct choice")
            input("Enter any key to continue")
            cust_show()
                #--------MODIFY MENU AREA
def modifyshow():
    choice1=CM.modify_menu()
    while True:
        if choice1==1:
            #--to search custid and modify customer name
            cust.search_mod_custnm()
            input("----Press any key------")
            break
        elif choice1==2:
            #----to search custid and modify customer address
            cust.search_mod_custadd()
            input("----Press any key------")
            break
        elif choice1==3:
            #---to search custid and search customer phone
            cust.search_mod_custphno()
            input("----Press any key------")
            break
        elif choice1==4:
            print("\a")
            break
        else:
            print("Enter the correct choice")
            input("-----Press any key to continue-----")
            choice1=0
            modifyshow()
            #------------------------- #--------administrator menu
def midmenu():
    choice1=CM.middleadminmenu()
    while True:
        if choice1==1:
            cust_show()
            break
        elif choice1==2:
            product_show()
            break
        elif choice1==3:
            canteen_show()
            break
        elif choice1==4:
            print("\a")
            break
        else:
            print("Enter the correct choice")
            input("Enter any key to continue")
            choice1=0
            midmenu()
def canteen_show():
    choice1=CM.canteen_menu()
    while True:
        if choice1==1:
            inv_rp.cust_purchase()
            break
        elif choice1==2:
            inv_rp.modify_purchase()
            break
        elif choice1==3:
            inv_rp.delete_purchase()
            break
        elif choice1==4:
            print("\a")
            break
        else:
            print("Enter the correct choice")
            input("Enter any key to continue")
            choice1=0
            canteen_show()
            #-----------reports
def gen_reports():
    choice1=CM.reportmenu()
    while True:
        if choice1==1:
            inv_rp.report_all_custinv()
            break
        elif choice1==2:
            inv_rp.report_cust_invno()
            break
        elif choice1==3:
            inv_rp.report_all_custinv_date()
            break
        elif choice1==4:
            inv_rp.report_all_prodinv()
            break
        elif choice1==5:
            inv_rp.report_prod_invno()
            break
        elif choice1==6:
            inv_rp.report_all_prodinv_date()
            break
        elif choice1==7:
            print("\a")
            break
        else:
            print("Enter the correct choice")
            input("Enter any key to continue")
            choice1=0
            gen_reports()
#-----------reports #-------------Main MENU------------------------------
def main():
    CM.intro()
    choice=0
    while(True):
        choice=CM.main()
        if choice==1:
            CM.myclear()
            gen_reports()
        elif choice==2:
            CM.myclear()
            midmenu()
        elif choice==3:
            print("Thank you,Do visit again")
            sys.exit()
            break
        else:
            print("Enter the correct choice")
            input("Enter any key to continue")
