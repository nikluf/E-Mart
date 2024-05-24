def delemp():
    from databcreV2 import dbcr
    
    
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
   ## assuming input to be taken in driver code
    
    cur.execute("select * from emptable")
    print('-'*156)
        
    print("EMPLOYEE ID \t  FIRST NAME \t  SECOND NAME \t  JOB TYPE \t SAL PER ANNUM")
    print('-'*156)
    for m in cur:
        print(m[0],'\t \t',m[1],'\t \t',m[2],'\t \t',m[3],'\t \t',m[4])
    ioi=int(input('--> PLEASE ENTER THE ID OF THE EMPLOYEE TO BE REMOVED>>>'))
    cur.execute("delete from emptable where empcode={}".format(ioi))
    con.commit()
    cur.close()
    con.close()
    

def addemp():
    from databcreV2 import dbcr
   
    
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    
    ip=int(input('--> PLEASE ENTER THE NEW EMPLOYEE CODE>>>'))
    ui=input('--> PLEASE ENTER THE FIRST NAME>>>')
    yt=input('--> PLEASE ENTER THE LAST NAME>>>')
    gty=input('--> PLEASE ENTER THE POSITION>>>')
    der=int(input('--> PLEASE ENTER THE SALARY(PER ANNUM) >>>'))
    cur.execute("insert into emptable values({},'{}','{}','{}',{})".format(ip,ui,yt,gty,der))
    con.commit()
    cur.close()
    con.close()


def empdatup():
    from databcreV2 import dbcr
    
    
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    
    r=int(input('--> ENTER THE OLD EMPLOYEE CODE OF PERSON>>>'))
    a=int(input('--> PLEASE ENTER THE NEW EMPLOYEE CODE>>>'))
    b=input('--> PLEASE ENTER THE NEW FIRST NAME>>>')
    c=input('--> PLEASE ENTER THE NEW LAST NAME>>>')
    d=input('--> PLEASE ENTER THE NEW POSITION>>>')
    e=int(input('--> PLEASE ENTER THE NEW SALARY(PER ANNUM) >>>'))
    cur.execute("update emptable set empcode={},First_Name='{}',Second_Name='{}',Job_Type='{}',Salary_perannum={} where empcode={}".format(a,b,c,d,e,r))
    con.commit()
    cur.close()
    con.close()
    
    
    
    
    

