print('\n'*48)
from databcreV2 import dbcr
dbcr()
import mysql.connector as mycon
con=mycon.connect(host="localhost",username="root",passwd="Madrid7",database="V2")
cur=con.cursor()
#if con.is_connected():
    #print("connection successful")
from cartcr import cartu
cartu()
from random import *

cur.execute("drop table cart ")

cartu()

from strmen import strupmen
from viewfullitb import adminfullitview,usfullitview,crtview,empview
from deletupitbl import admndelit,admninsertit
from prmnad import profitmngr
from delupemp import delemp,addemp,empdatup
from serchingus import srccate,itsrc
from amenu import admnmenu
from usermunu import usmenu
from log import loginin

from ad import adcrt
from cot import ckiot


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
            rtp=True########this
            while rtp:
                print("DO YOU WANT TO CREATE A NEW ACCOUNT(press 1) OR JUST LOG IN (press 2)")
                jo=int(input())
                if jo==1:
                    a=input("enter your First Name")
                    b=input("enter your last name")
                    c=input("enter gender")
                    d=input("enter password")
                    f=input("renter password")
                    if f==d:
                        h=randrange(0,10000)
                        cur.execute("select userid from listofusers")
                        t=True
                        while t:
                            cnt=0
                            for i in cur:
                                if i==h:
                                    cnt+=1
                                
                            if cnt==0:
                                print("your new user id will be",h,'(remember this)')
                                cur.execute("insert into listofusers values({},'{}','{}','{}','{}')".format(h,a,b,c,d))
                                con.commit()
                                print("successful")
                                print("\n \n will you like to create another new account(1) \n login(2) \n quit(3)")
                                o=int(input())
                                if o==1:
                                    t=False
                                if o==2:
                                    t=False
                                    rtp=False
                                if o==3:
                                    t=False
                                    rtp=False
                                    c=False
                                    b=False
                                    a=False
                                    print("THANK YOU")
                            if cnt==1:
                                print('dfv')
                                continue
                    if f!=d:
                        print("pass missmatch try again")
                if jo!=1:
                    rtp=False#####thos
                    print("OKAY THE \n \n WELCOME TO THE LOGIN MENU")
                
                
                    
                    
            print("---LOGIN::::::::: \n")    
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
                    
                    
                        
                    
                    
                    
                    
                
                        
                    
                    
                    
                    
                    
                
                
            
            
             
            


                    
                
            
            

                
            
    

    
