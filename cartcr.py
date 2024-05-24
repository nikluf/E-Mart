def cartu():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    rt=True
    cur.execute("show tables")
    for i in cur:
        if 'cart' in i:
            rt=False
        
    #if rt==False:
        #cur.execute("drop table cart")
    if rt==True:
        cur.execute("create table cart(itemid int primary key,item_name varchar(30),quantity_bought int,price_peritem int)")
    
    cur.close()
    con.close()
                
