

def emtble():
    count=True
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")

    cur.execute("show tables")

    for i in cur:
        if 'emptable' in i:
            count=False
        else:
            continue
        
    
    
    

    #cur.execute("show tables")
    
    #for i in cur:
        #print('')
    
    if count==True:
        cur.execute("create table emptable(empcode int primary key, First_Name varchar(30),Second_Name varchar(30),Job_Type varchar(30),Salary_perannum int)")
        cur.execute("insert into emptable values(1,'Rahul','Mishra','Manager',120000)")
        con.commit()
    cur.close()
    con.close()
    

       
        
        
