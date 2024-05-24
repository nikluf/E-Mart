def ckiot():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    cur.execute("select * from cart")
    sumo=0
    tuy=()
    for i in cur:
        tuy+=(i[0],)
        qty=i[2]
        pr=i[3]
        sumo+=(i[2]*i[3])
    print('-'*156,'\n')
    print('-->YOUR FINAL AMOUNT is ₹',sumo)
    u=input('--> ENTER METHOD OF PAYMENT >>>')
    h=input('--> ENTER CODE >>>')
    cur.execute("select * from listofitems")
    tu=()
    for i in cur:
        if i[0] in tuy:
            tu+=(i[2],)
            
    r=len(tu)
    for i in range(r):
    
        cur.execute("update listofitems set quantity={} where itemcode={}".format(tu[i],tuy[i]))
        con.commit()
        #print("d")

    ty=()
    cur.execute("select * from cart")
    for i in cur:
        ty+=((i[0],i[2]),)
    #print(ty)
    l=len(ty)
    #print(l)
    
    
    for i in range(l):
        cur.execute("update listofitems set quantity=quantity-{} where itemcode={}".format(ty[i][1],ty[i][0]))
        con.commit()
    cur.close()
    con.close()
                
        
 
            
        
        
        
