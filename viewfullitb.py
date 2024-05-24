from ustale import usertable
usertable()### to check existence of the user table
from databcreV2 import dbcr

import mysql.connector as mycon
con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
cur=con.cursor()
#if con.is_connected():
    #print("connection successful")
def adminfullitview():
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    cur.execute("select * from listofitems")
    print('\n','-'*156)
    print("ITEMCODE \t ITEMNAME \t  QUANTITY \t SELLING PRICE \t CATEGORY \t COST PRICE ")
    for i in cur:
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3],'\t \t',i[4],'\t \t',i[5])
        print(120*'-')
        #print(f"{i[0]:7}{gap}{i[1]:20}{gap}{i[2]:6}{gap}")
    print('\n','-'*156)
        ### only for printing the table no input
    cur.close()
    con.close()


def usfullitview():
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    cur.execute("select * from listofitems")
    print('\n','-'*156)
    print("ITEMCODE \t ITEMNAME \t SELLING PRICE \t CATEGORY  ")
    for i in cur:
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[3],'\t \t',i[4])
        print(120*'-')
        ### only for printing the table no input
    print('\n','-'*156)
    cur.close()
    con.close()

def crtview():
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #print("1")

    cur.execute("select * from cart")
    #print("2")
    print('\n','-'*156)
    
    print("ITEMCODE \t ITEMNAME ,QUANTITY PURCHASED \t SELLING PRICE")
    for i in cur:
        
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3])
        print(120*'-')
    cur.close()
    con.close()

def empview():
    

    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    cur.execute("select * from emptable")
    print('\n','-'*156)
    print("EMP ID \t FIRST NAME \t  LAST NAME \t JOB POS \t SALARY PER ANNUM ")
    for i in cur:
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3],'\t \t',i[4])
        print(120*'-')
    print('\n','-'*156)
    cur.close()
    con.close()


    
    


