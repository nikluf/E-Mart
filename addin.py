def addcart():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    if con.is_connected():
        print("connection successful")
    
    
    u=int(input("enter the id of the item u want"))
    y=int(input("enter quantity u want to buy"))
    cur.execute("select * from listofitems")
    tup=()
    for i in cur:
        if i[0]==u and y<=i[2]:
            
            tup+=i##this tup contains all data from actual table
    
    
    b=tup[1]
    c=tup[3]
    totuy=True
    cur.execute("select * from cart")
    pou=()
    for i in cur:
        if i[0]==u:## checking if an item already exists in cart an if then adding quantity
            totuy=False
            pou+=i
    if totuy==False:
        ruyt=tup[2]
        reo=ruyt-y## updated for the actual table(quantty)
        rte=pou[2]
        fre=pou[2]+y
        cur.execute("update cart set quantity_bought={} where itemid={}".format(fre,u))
        con.commit()
        #cur.execute("update listofitems set quantity={} where itemcode={}".format(reo,u))
        #con.commit()

    
    else:
        cur.execute("insert into cart values({},'{}',{},{})".format(u,b,y,c))
        ruyt=tup[2]
        reo=ruyt-y
        
        con.commit()
        #cur.execute("update listofitems set quantity={} where itemcode={}".format(reo,u))
        #con.commit()



