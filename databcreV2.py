
def dbcr(sqlpass):
    import mysql.connector as mycon
    con=mycon.connect(host="localhost",username="root",passwd=sqlpass)
    cur=con.cursor()
    # if con.is_connected():
    #     print("connection successful")
    cur.execute("SHOW DATABASES")
    # for i in cur:
    #     print(i)
    flag=False
    for i in cur:
        if 'V2' in i:
            flag=True### its not deleting database v2 if it exists and if not creates a new one
            break ######we create the database user adn nexxt we need to openit
    #print(flag)
    if not flag:
        cur.execute("create database V2")
        #print("donedonadone")
    #else:
        #print("already exists")
    #cur.close()
    con.close()
                
            
