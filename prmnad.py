def profitmngr():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    import matplotlib.pyplot as mapy
    cur.execute("select * from listofitems")
    cp=[]
    sp=[]
    it=[]
    ms=0
    mc=0
    for i in cur:
        it+=[i[1],]
        cp+=[i[5]*i[2],]
        mc+=i[5]*i[2]
        ms+=i[3]*i[2]    
        sp+=[i[3]*i[2],]
    print('-'*156,'\n','\t \t \t \t \t \t \t \t',"WELCOME SIR",'\n','-'*156,'\n \n',"::WE HAVE SPENT ALMOST ",mc,"ON OUR GOODS",'\n \n','MADE ALMOST ₹',ms-mc)
    prof=((ms-mc)/mc)*100
    if ms-mc>=0:
             print('\n \n WITH PROFIT MARGIN OF',prof,'%')
    else:
        print("\n \n with loss of",prof,'%')
    #print(it,cp,sp)
    mapy.plot(it,cp,color='yellow')
    mapy.plot(it,sp,color='green')
    mapy.xlabel('ITEM NAME')
    mapy.ylabel("ITEM TOTAL PRICE")
    mapy.title("ITEMS")
    mapy.show()
    cur.close()
    con.close()
        
