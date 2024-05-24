
import mysql.connector as mycon
con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
cur=con.cursor()

def usmenu():
    print('\n','-'*156)
    print("WELCOME PLEASE ENTER \n --> 1)TO SEARCH BY CATEGORY \n --> 2)TO SEARCH BY NAME \n --> 3)TO VIEW CART \n --> 4)Quit \n --> 5)Checkout")
    print('\n','-'*156)

def admnmenu():
    print('WELCOME SIR \n \n  PLEASE ENTER YOUR CHOICE: \n \n 0) to view all employees \n \n 1) To View all items \n \n 2)add new employee \n \n 3)Edit Employee Data \n \n 4)Compare company performance \n \n  5)Delete exisiting items \n \n 6)insert new items \n \n 7)To go back to login menu \n \n 8)to exit from programme')
    
def dbcr():
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    cur.execute("SHOW DATABASES")
    flag=False
    for i in cur:
        if 'V2' in i:
            flag=True### its not deleting database v2 if it exists and if not creates a new one
            break ######we create the database user adn nexxt we need to openit
    if not flag:
        cur.execute("create database V2")
        #print("donedonadone")
    #else:
        #print("already exists")
    cur.close()
    con.close()
                
            
def usertable():
    count=0
    from databcreV2 import dbcr
    dbcr()
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
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


def itemtable():
    count=True
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")

    cur.execute("show tables")

    for i in cur:
        if 'listofitems' in i:
            count=False
        else:
            continue
        
    
    
    

    #cur.execute("show tables")
    
    #for i in cur:
        #print('')
    
    if count==True:
        cur.execute("create table listofitems(itemcode int primary key, itemname varchar(30),quantity int,sellingpriceperitem int,type varchar(30),costpriceperitem int)")
        cur.execute("insert into listofitems values(1,'kurkure',23,23,'snacks',20),(213,'lays',23,22,'snacks',21),(233,'hit',43,22,'homec',11),(453,'tedemede',400,10,'snacks',15),(555,'oyes',1000,20,'snacks',25),(387,'sprite_500ml',5000,50,'coldrinks',60),(456,'fanta_500ml',5500,70,'coldrinks',75),(892,'mountainduke_500ml',5000,40,'coldrinks',45),(898,'iphone6',200,80000,'mobilephone',80200),(911,'iphone8',500,90000,'mobilephone',90300),(619,'mia1',500,6000,'mobilephone',6100),(299,'philipsspeaker',200,2000,'electronics',2090),(333,'dellaptop',200,4000,'electronics',4100),(104,'hplaptop',500,5500,'electronics',5700),(192,'lenovolaptop',100,6000,'electronics',6200),(554,'nintendods',400,3500,'gaming',3600),(810,'nintendo3ds',200,5000,'gaming',5100),(980,'nintendoswitch',200,8000,'gaming',8150),(200,'ps4',1000,10000,'gaming',10500),(696,'ps3',200,8900,'gaming',9000),(400,'xbox360',1000,11000,'gaming',11200),(710,'apple_1kg',300,10,'fruits_vegetables',12),(499,'banana_1kg',1000,12,'fruits_vegetables',15),(888,'mango_1kg',700,20,'fruits_vegetables',25)")
        con.commit()
    cur.close()
    con.close()
                
    

       
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


def adminfullitview():
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    cur.execute("select * from listofitems")
    print('\n','-'*156)
    print("ITEMCODE \t ITEMNAME \t  QUANTITY \t SELLING PRICE \t CATEGORY \t COST PRICE ")
    for i in cur:
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3],'\t \t',i[4],'\t \t',i[5])
        print(120*'-')
        #print(f"{i[0]:7}{gap}{i[1]:20}{gap}{i[2]:6}{gap}")
    print('\n','-'*156)
        ### only for printing the table no input
    cur.close()
    con.close()
                

def usfullitview():
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    cur.execute("select * from listofitems")
    print('\n','-'*156)
    print("ITEMCODE \t ITEMNAME \t SELLING PRICE \t CATEGORY  ")
    for i in cur:
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[3],'\t \t',i[4])
        print(120*'-')
        ### only for printing the table no input
    print('\n','-'*156)
    cur.close()
    con.close()

def crtview():
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #print("1")

    cur.execute("select * from cart")
    #print("2")
    print('\n','-'*156)
    
    print("ITEMCODE \t ITEMNAME ,QUANTITY PURCHASED \t SELLING PRICE")
    for i in cur:
        
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3])
        print(120*'-')
    cur.close()
    con.close()

    
def empview():
    

    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    cur.execute("select * from emptable")
    print('\n','-'*156)
    print("EMP ID \t FIRST NAME \t  LAST NAME \t JOB POS \t SALARY PER ANNUM ")
    for i in cur:
        print(120*'-')
        print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3],'\t \t',i[4])
        print(120*'-')
    print('\n','-'*156)
    cur.close()
    con.close()



def loginin():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    yo=True
    while yo:
        aota=() ##tuple inwhich i put first id nd pass

        cur.execute("select * from listofusers")
        for i in cur:
            aota+=((i[0],i[4]),)
        uid=int(input('--> ENTER YOUR USER ID>>>'))
        print('\n')
        pas=input('--> ENTER YOUR PASSWORD>>>')
        if (uid,pas) in aota:
            yo=False### a while loop running tilll right pass entered
        else:
            print('\n','-'*156,'\n')
            print('INCORRECT PASSWORD ')
            print('\n','-'*156,'\n','WILL YOU LIKE TO RETRY YES OR NO:')
            mo=input()
            if mo.lower()==yes:
                continue
            else:
                break
    cur.close()
    con.close()



def strupmen():
    print("\t \t \t \t \t \t \t \t WELCOME TO NIKHIL SERVICES... \n \n PLEASE ENTER THE MODE ENTRY: \n \n --> 1) USER \n \n --> 2) ADMIN \n\n  --> 3)QUIT")
    print('\n','-'*156)
    
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



def admndelit():   # updated a liitle###
    from databcreV2 import dbcr
    dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    #if con.is_connected():
        #print("connection successful")
    d=int(input("would you like to see to see the complete table? \n 1-YES \n 2-NO ")
    
    
          
          
    
            

        
          
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
                
dbcr()
from cartcr import cartu
cartu()

cur.execute("drop table cart ")

cartu()




############# making a loop with some var(a as True)#######
a=True
while a:
    strupmen() ###printing the first screen
    print('\n')
    u=int(input('ENTER YOUR CHOICE >>> '))
    if u==3:### if 3 then breaking otherwise just running the loop
        print('THANK YOU')
        a=False
    if u==2:
        ##### making another loop with var b
        b=True
        while b:
            admnmenu()
            print('\n')
            t=int(input("ENTER CHOICE >>> "))
            if t==0:
                print('\n')
                empview()
                print('\n')
                #cur.execute("select * from emptable")
                #print("EMPLOYEE ID FIRST NAME LAST NAME JOB POSITION SALARY PER ANNUM")
                #for i in cur:
                    #print('-'*120)
                    #print(i[0],'\t \t',i[1],'\t \t',i[2],'\t \t',i[3],'\t \t',i[4])
                    #print('-'*120)
            if t==1:
                print('\n','-'*156,'\n')
                adminfullitview() ##prints all items and then goes to admin menu
            if t==2:
                print('\n','-'*156,'\n')
                addemp()
                #empview()
                #print("YOU NEED TO RESTART TO SEE THE CHANGES")##add employees and then goes back to admn menu
                #e=int(input("will you like to go back or keep adding changes will be visible after restart(1/0)"))
                
                #if e==1:
                    #b=False
                    #a=False
                    #print("PLEASE RESTART")
                #print("record inserted")
                    
                
                    
            if t==3:
                print('\n','-'*156,'\n')
                empdatup()
                #print("YOU NEED TO RESTART TO SEE THE CHANGES")##add employees and then goes back to admn menu
                #e=int(input("will you like to go back or keep adding changes will be visible after restart(1/0)"))
                
                #if e==1:
                    #b=False
                    #a=False
                    #print("PLEASE RESTART")### edits data adn then goes bavk
            if t==4:
                print('\n','-'*156,'\n')
                profitmngr()
            if t==5:
                print('\n','-'*156,'\n')
                admndelit()
                #print("YOU NEED TO RESTART TO SEE THE CHANGES")##add employees and then goes back to admn menu
                #e=int(input("will you like to go back or keep adding changes will be visible after restart(1/0)"))
                
                #if e==1:
                    #b=False
                    #a=False
                    #print("PLEASE RESTART")
            if t==6:
                print('\n','-'*156,'\n')
                admninsertit()
                #print("YOU NEED TO RESTART TO SEE THE CHANGES")##add employees and then goes back to admn menu
                #e=int(input("will you like to go back or keep adding changes will be visible after restart(1/0)"))
                
                #if e==1:
                    #b=False
                    #a=False
                    #print("PLEASE RESTART")
            if t==7:
                b=False ## makes fales and goes back to login menu
            if t==8:
                print('\n','-'*156,'\n')
                print('Thank you')
                b=False
                a=False### completely emits
       #a,b,u,t used >>>>         
   #######################################################
    if u==1:
        c=True####another while loop with var c
        while c:
            loginin()## completely logininh by other while loops
            print('\n','-'*156,'\n')
            print('SUCCESSFULL')
            uyo=True## another while loop with uyo just not to go back to loogin
            while uyo:
                usmenu()### now in the user menu
                f=int(input("ENTER YOUR CHOICE >>> "))
                if f==1:
                    lo=True
                    while lo:
                        cur.execute("select distinct type from listofitems")
                        print("HERE ARE THE CATEGORIES:")
                        print('\n')
                        for i in cur:
                            print(i[0])
                        srccate()
                        print('\n')
                        qw=int(input("PRESS 1-WANT TO ADD TO CART \n \n PRESS 0-DON'T WANT TO "))
                        print('\n','-'*156)
                        if qw==1:
                            adcrt()
                            irt=int(input('PRESS 1-IF YOU WANT TO SEARCH AGAIN \n PRESS 0-IF YOU WANT TO GO BACK \n PRESS 2-VIEW CART \n PRESS 3-TO CHECKOUT '))
                            print('\n','-'*156)
                            if irt==1:
                                continue
                            elif irt==0:
                                lo=False
                            elif irt==2:
                                crtview()
                                rt=int(input("PRESS 1  IF U WANT TO CHECKOUT \n PRESS 2 TO GO BACK"))
                                if rt==2:
                                    #continue
                                    lo=False
                                if rt==1:
                                    ckiot()
                                    lo=False
                                    c=False
                                    uyo=False
                                    a=False
                                    
                            elif irt==3:
                                ckiot()
                                lo=False
                                c=False
                                uyo=False
                                a=False
                        elif qw==0:
                            lo=False
                        
                if f==4:
                    print('\n','-'*156,'\n')
                    print('THANK YOU')
                    uyo=False
                    c=False
                    a=False
                if f==3:

                    crtview()
                if f==2:
                    roro=True##inside while loop taking inputs then giving suitable out[pys
                    while roro:
                        #print('haha')
                        yoyo=True
                        while yoyo:
                            print('\n','-'*156,'\n')
                            itsrc()
                            print('\n')
                            qw=int(input("PRESS 1-WANT TO SEARCH AGAIN \n PRESS 0-DON'T WANT TO \n PRESS 3 - WANT TO CHECKOUT"))
                            print('\n','-'*156)
                            if qw==1:
                                continue
                            #adcrt()
                                #irt=int(input('PRESS 1-IF YOU WANT TO SEARCH AGAIN \n PRESS 0-IF YOU WANT TO GO BACK \n PRESS 2-VIEW CART \n PRESS 3-TO CHECKOUT '))
                                #print('\n','-'*156)
                                #if irt==1:
                                    #continue
                                #elif irt==0:
                                    #lo=False
                                #elif irt==2:
                                    #crtview()
                                    #rt=int(input("ENTER IF U WANT TO CHECKOUT(1) OR NOT(2)"))
                                    #if rt==2:
                                        #roro=False
                                    #if rt==1:
                                        #ckiot()
                                        #lo=False
                                        #c=False
                                        #uyo=False
                                        #a=False
                                #elif irt==3:
                                    #ckiot()
                                    #lo=False
                                    #c=False
                                    #uyo=False
                                    #a=False
                            if qw==0:
                                yoyo=False
                                roro=False
                            if qw==3:
                                ckiot()
                                roro=False
                                yoyo=False
                                c=False
                                uyo=False
                                a=False
                                
                            
                            
                if f==5:
                    a=int(input("DO YOU WANT TO VIEW YOUR CART PRESS 1-YES || PRESS 2 -NO >>>"))
                    if a==1:
                        crtview()
                    else:
                        continue
                    
                    ckiot()
                    uyo=False
                    c=False
                    a=False
                    
                    
                        
                    
                    
                    
                    
                
                        
                    
                    
                    
                    
                    
                
                
            
            
             
            


                    
                
            
            

                
            
    

    


        

                
    
        
