def srccate():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    cur.execute("select * from listofitems")
    print('\n','-'*156,'\n')
    print('\n')
    i=input('ENTER THE CATEGORY YOU WANT TO VIEW>>')
    print('ITEM CODE \t ITEM NAME \t PRICE PER ITEM \t  TYPE')
    for j in cur:
        if i==j[4]:
            print(j[0],'\t \t',j[1],'\t \t',j[3],'\t \t',j[4])
    print('\n','-'*156,'\n')
    cur.close()
    con.close()


def itsrc():
     from databcreV2 import dbcr
     dbcr()
     import mysql.connector as mycon
     con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
     cur=con.cursor()
     from viewfullitb import crtview
     #if con.is_connected():
         #print("connection successful")
     cur.execute("select * from listofitems")
     print('\n','-'*156,'\n')
     t=[]
     uy=input('ENTER THE ITEM NAME TO SEARCH>>>')
     print('ITEM CODE \t ITEM NAME \t PRICE PER ITEM \t  TYPE')
     for i in cur:
         if i[1]==uy.lower():###check for lowercasse
             t+=[i[0],i[1],i[3],]
             print(i[0],'\t \t',i[1],'\t \t',i[3],'\t \t',i[4])
     j=int(input("DO YOU WANT TO ADD THIS \n PRESS 1 IF YES \n PRESS 2 IF NO \n PRESS 3 TO VIEW CART"))
     print(t)
     if j==1:
         PRINT('\n \n ')
         toy=int(input("ENTER THE QUANTITY >>>"))
         t.insert(2,toy)
         p=tuple(t)
         #print(p)
         cur.execute("insert into cart values{}".format(p))
         con.commit()
     if j==3:
         crtview()
     cur.close()
     con.close()
     
         
         
            


            
            
    
            
            
