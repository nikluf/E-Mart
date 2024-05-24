def admndelit():
    from databcreV2 import dbcr
    dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    j=int(input("do u want to see the complete table \n 1-YES \n 2-NO:"))
    if j==1:
        cur.execute("select * from listofitems")
        print('\n','-'*156)
        print("ITEMCODE \t ITEMNAME \t  QUANTITY \t SELLING PRICE \t CATEGORY \t COST PRICE ")
        for i in cur:
            print(120*'-')
            print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3],'\t \t',i[4],'\t \t',i[5])
            print(120*'-')
        #print(f"{i[0]:7}{gap}{i[1]:20}{gap}{i[2]:6}{gap}")
        print('\n','-'*156)
    

        
    

    uop=int(input('--> PLEASE ENTER THE ID OF THE ITEM >>>'))
    out=int(input('--> PLEASE ENTER THE QUANTITY TO BE REMOVED>>>'))
    cur.execute("select * from listofitems")
    deli=True
    upd=True
    for i in cur:
        
        
        if i[0]==uop:
            #print('hola')
            
            uiy=i[2]
            gyt=uiy-out
            #print(gyt)
            if i[2]==out or gyt<0:
                #print('yes')
                #print(uop)
                deli=False
                
            elif gyt>0:
                #print(gyt,uop)
                upd=False
    
    if deli==False:
        cur.execute("delete from listofitems where itemcode = {}".format(uop))
        con.commit()
    elif upd==False:
        cur.execute("update listofitems set quantity={} where itemcode={}".format(gyt,uop))
                
        con.commit()
    cur.close()
    con.close()
                
     
def admninsertit():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    print('-'*150,'\n')
    tyu=int(input('--> PLEASE ENTER THE ITEM ID >>>'))
    fre=input('--> PLEASE ENTER THE ITEM NAME >>>')
    frt=int(input('-->PLEASE ENTER THE QUANTITY BOUGHT>>>'))
    fgh=int(input('--> PLEASE ENTER THE COST PRICE >>>'))
    tre=input('--> PLEASE ENTER THE TYPE OF PRODUCT >>>')
    ghy=int(input('--> PLEASE ENTER THE SELLING PRICE >>>'))
    cur.execute("insert into listofitems values({},'{}',{},{},'{}',{})".format(tyu,fre,frt,ghy,tre,fgh))
    con.commit()
    cur.close()
    con.close()
                
    
