from ustale import usertable
from creitble import itemtable
from employee import emtble
from cartcr import cartu
from addin import addcart
from serchingus import srccate,itsrc
from cot import ckiot
cartu()

from databcreV2 import dbcr
dbcr()
import mysql.connector as mycon
con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
cur=con.cursor()
if con.is_connected():
    print("connection successful")
###starting wiht initial
from strmen import strupmen
rui=True

while rui:## while loops
    strupmen()
    rtu=int(input('enter choice'))
    if rtu==3:
        rui=False
        print('Thank You')
    if rtu==2:
        fry=True
        from amenu import admnmenu### accesing admn mneu
        while fry:
            admnmenu()
            ui=int(input())
            if ui==1:
                from viewfullitb import adminfullitview
                adminfullitview()
            elif ui==2:
                from delupemp import addemp
                addemp()
            elif ui==3:
                from delupemp import empdatup
                empdatup()
            elif ui==4:
                from prmnad import profitmngr
                profitmngr()
            elif ui==5:
                from deletupitbl import admndelit
                admndelit()
            elif ui==6:
                from deletupitbl import admninsertit
                admninsertit()
            elif ui==7:
                fry=False
            elif ui==8:
                fry=False
                rui=False
                print("Thank You")
    if rtu==1:###loginin 
        yo=True
        
        from usermunu import usmenu
        
        
        while yo:
            ruy=True
            j=int(input('ENTER USER ID'))
            o=input('ENTER PASSWORD')
            cur.execute("select * from listofusers")
            for i in cur:
                
                if i[0]==j and i[4]==o :
                    ruy=False    ## loginingin...
            print(ruy)
            if ruy==False:
                
                buy=True
                while buy:
                    print("SUCESSFUL")
                    print(120*'-')
                    usmenu()
                    o=int(input())## taking input for menu
                    if o==1:
                        
                        
                        
                        
                        
                        yre=True
                        while yre:
                            srccate()
                            addcart()
                            uop=int(input("do you want to go back(1,0)"))
                            if uop==1:
                                break
                                
                            elif uop==0:
                                continue
                    if o==2:
                        roro=True
                        while roro:
                            itsrc()
                            addcart()
                            uop=int(input("do you want to go back(1,0)"))
                            if uop==1:
                                break
                                ######
                            elif uop==0:
                                continue
                    if o==3:
                        cartu()
                        cur.execute("select * from cart")
                        uro=True
                        while uro:
                            for i in cur:
                                print(i)
                            uro=False
                        
                            
                        
                        
                            
                        
                    if o==4:
                        buy=False
                        yo=False
                        break
                    if o==5:
                        ckiot()
                    
                        
                        
                            
                        
                        
                                    
                            
                            
                            

                                           
                        

                    
                    
                   
                        
                    
                    
                    
                    
            
            
                        
        
            
            
            
        

    
        
            
            
            
            
        
    
    
    
