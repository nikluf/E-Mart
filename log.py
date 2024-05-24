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
    
    
        

    
