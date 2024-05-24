def logn():
    from databcreV2 import dbcr
    
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
    cur=con.cursor()
    if con.is_connected():
        print("connection successful")
    uo=False
    i=input('ENTER USER ID')
    o=input('ENTER PASSWORD')
    cur.execute("select * from listofusers")
    for i in cur:
        if i[0]==i and i[4]==o:
            uo=True
            
    if uo==True:
        return(a=2)
    else:
        return(a=1)
    
