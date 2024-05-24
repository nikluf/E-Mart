from databcreV2 import dbcr

import mysql.connector as mycon
con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
cur=con.cursor()
#if con.is_connected():
    #print("connection successful")
def adcrt():
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    print('\n','-'*156,'\n')
    t=int(input('--> PLEASE ENTER THE ITEM ID TO ADD >>>'))
    print('\n')
    r=int(input("--> PLEASE ENTER THE QUANTITY TO BUY >>>"))
    print('\n','-'*156,'\n')
    ### t and r are inputs
    cur.execute("select * from listofitems")
    tup=()
    for i in cur:
        if i[0]==t and r<=i[2]:
            tup+=(i,)
    jojo=True
    cur.execute("select * from cart")
    tutu=0
    for i in cur:
        if i[0]==tup[0][0]:
            tutu=i[2]
            jojo=False
        else:
            continue
    #print(tup[0][1],tup[0][3])

    if jojo==False:
        cur.execute("update cart set quantity_bought={} where itemid={}".format(tutu+r,t))
        con.commit()
    else:
        cur.execute("insert into cart values({},'{}',{},{})".format(t,tup[0][1],r,tup[0][3]))
        con.commit()
    cur.close()
    con.close()
                
    
        
