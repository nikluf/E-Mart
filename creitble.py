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
                
    

       
        
        
