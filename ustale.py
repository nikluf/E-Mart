
def usertable(sqlpass):
    count=0
    from databcreV2 import dbcr
    dbcr(sqlpass)
    print('hh')
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd=sqlpass,database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    cur.execute("show tables")
    tutu=True
    for i in cur:
        #print(i)
        if 'listofusers' in i:
            tutu=False
            break
            
        else:
            continue

    #cur.execute("show tables")
    
    #for i in cur:
        #print(i)
    
    if tutu==True:
        cur.execute("create table listofusers(userid int primary key, First_Name varchar(10),Last_Name varchar(10), gender char(1),pass varchar(20))")
        cur.execute("insert into listofusers values(1,'','','m','')")
        con.commit()
    cur.close()
    con.close()
    
    
        
    


       
        
        



    
   
    
    
    
