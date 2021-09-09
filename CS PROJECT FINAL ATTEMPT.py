import random
import datetime
import mysql.connector
from tabulate import tabulate
db=mysql.connector.connect(
    host="127.0.0.1",
    username="root",
    passwd="hassan32",
    database="project")









def bookingtickets():
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
                           #PASSENGER#

    print("ENTER YOUR DATA")
    cursor=db.cursor()
    l=list()
    name=input("ENTER YOUR NAME:")
    age=int(input("ENTER YOUR AGE :"))
    address=input("ENTER YOUR ADDRESS")
    cprno=int(input("ENTER YOUR CPR NUMBER :"))
    mobileno=int(input("ENTER YOUR MOBILE NUMBER :"))
    print("\n")
    cursor.execute("select * from showlocation order by serialnumber")
    a=cursor.fetchall()
    print(tabulate(a,headers=['SERIALNO','AIRPORT','IATA CODE']))
    print("\n")
    departure=int(input("ENTER YOUR DEPARTURE PLACE ON THE BASIS OF SERIAL NUMBER :"))
    for i in range (len(a)):
        if departure==a[i][0]:
            departureplace=a[i][1]
            departurecode=a[i][2]
    print("ENTER YOUR DEPARTURE DATE IN   YYYY,M,DD ")
    departuredate=input(datetime.date)
    arrival=int(input("ENTER YOUR ARRIVAL PLACE ON THE BASIS OF SERIAL NUMBER :"))
    for i in range (len(a)):
        if arrival==a[i][0]:
            arrivalplace=a[i][1]
            arrivalcode=a[i][2]
    print("ENTER YOUR ARRIVAL DATE IN   YYYY,M,DD  ")
    arrivaldate=input(datetime.date)
    print("\n")


    
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
                               #CLASS AND FLIGHT#


    
    cursor.execute("select serialno,flight from showflight")
    d=cursor.fetchall()
    print(tabulate(d,headers=['SERIALNO','FLIGHTS']))
    print("\n")
    serialflight=int(input("ENTER YOUR FLIGHT ON THE BASIS OF SERIAL NO:"))

    
    cursor.execute("select * from showflight order by serialnumber")
    a=cursor.fetchall()
    for i in range (len(a)):
        if serialflight==a[i][0]:
            priceflight=a[i][2]
            flightname=a[i][1]
             
    print("\n")
    cursor.execute("select serialno,class from showclasstype order by serial number")
    b=cursor.fetchall()
    print(tabulate(b,headers=['SERIALNO','CLASS']))

    
    cursor.execute("select * from showclasstype")
    c=cursor.fetchall()
    cursor.close()
    print("\n")
    serialno=int(input("ENTER YOUR CLASS ON THE BASIS OF SERIIAL NUMBER :"))
    for i in range (len(c)):
        if serialno==c[i][0]:
            classtype=c[i][1]
            classprice=priceflight+c[i][2]
    print("\n")
    print("YOUR PRICE FOR THE SELECTED FLIGHT IS :",classprice)



    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
                               #eatables#

    pricefood=0
    fooditems=""
    cursor=db.cursor()
    cursor.execute("select * from showeatables order by serialno")
    a=cursor.fetchall()
    print(tabulate(a,headers=['SERIALNO','FOODITEMS','PRICE']))
    cursor.close()
    ask=int(input("ENTER THE NUMBER OF FOOD ITEMS YOU WANT :"))
    print("\n")
    for i in range (ask):
        serialno=int(input("ENTER THE SERIAL NUMBER OF THE FOOD ITEM: "))
        print("\n")
        for j in range (len(a)):
            if serialno==a[j][0]:
                fooditems=fooditems+a[j][1]+"   "
                pricefood=pricefood+a[j][2]

    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
                               #luggage#

    weight1=int(input("ENTER THE WEIGHT OF YOUR FIRST LUGGAGE :"))
    if weight1>30:
        print("THE WEIGHT WHICH YOU HAVE ENTERED IS EXCEDING OUR LIMITS")
        print("AS PER YOUR EXCEDING WEIGHT WE HAVE TAKEN ",(weight1-30)*10, " RS extra from you")
        price1=(weight1-30)*10
    else:
        price1=0
    weight2=int(input("ENTER THE WEIGHT OF YOUR SECOND LUGGAGE :"))
    if weight2>30:
        print("THE WEIGHT WHICH YOU HAVE ENTERED IS EXCEDING OUR LIMITS")
        print("AS PER YOUR EXCEDING WEIGHT WE HAVE TAKEN ",(weight2-30)*10, " RS extra from you")
        price2=(weight2-30)*10
    else:
        price2=0
    weight3=int(input("ENTER THE WEIGHT OF YOUR THIRD LUGGAGE :"))
    if weight3>30:
        print("THE WEIGHT WHICH YOU HAVE ENTERED IS EXCEDING OUR LIMITS")
        print("AS PER YOUR EXCEDING WEIGHT WE HAVE TAKEN ",(weight3-30)*10, " RS extra from you")
        price3=(weight3-30)*10
    else:
        price3=0
    weight=weight1+weight2+weight3
    price=price1+price2+price3
    print("THE EXTRA PRICE YOU SHOULD PAY FOR THE EXTTRA LUGGAGE IS :",price)

    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
                              
    ticketno=random.randint(100000,999999)

    print("THIS IS YOUR REQUIRED TICKET NUMBER PLEASE SAVE IT FOR FUTURE REFERENCE:",ticketno)
    totalprice=classprice+price
    val=(name,age,address,cprno,mobileno,departureplace,departurecode,departuredate,arrivalplace,arrivalcode,arrivaldate,flightname,classtype,weight1,weight2,weight3,fooditems,weight,totalprice,ticketno)
    addinfo="INSERT INTO storebooking (name,age,address,cprno,mobileno,departureplace,departurecode,departuredate,arrivalplace,arrivalcode,arrivaldate,flightname,classtype,weight1,weight2,weight3,fooditems,weight,totalprice,ticketno) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor=db.cursor()
    cursor.execute(addinfo,val)
    db.commit()
    cursor.close()
    db.close()
#--------------------------------------------------------------------------------#
#to check the information of the user#
    
def usercheck():
    
    b=int(input("ENTER YOUR TICKET NUMBER :"))
    cursor=db.cursor()
    cursor.execute("select ticketno from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['TICKET NUMBER']))

    print("\n")

    cursor.execute("select name,age,cprno,mobileno from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['NAME','AGE','CPR NUMBER','MOBILE NUMBER']))

    print("\n")

    cursor.execute("select address from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['ADDRESS']))

    print("\n")

    cursor.execute("select departureplace,departurecode,departuredate from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['DEPARTURE PLACE','DEPARTURE CODE','DEPARTURE DATE']))

    print("\n")

    cursor.execute("select arrivalplace,arrivalcode,arrivaldate from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['ARRIVAL PLACE','ARRIVAL CODE','ARRIVAL DATE']))

    print("\n")

    cursor.execute("select flightname,classtype from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['FLIGHT NAME','CLASS TYPE']))

    print("\n")

    cursor.execute("select weight1,weight2,weight3 from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['1st WEIGHT IN KG','2nd WEIGHT IN KG','3rd WEIGHT IN KG']))

    print("\n")

    cursor.execute("select fooditems from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['FOOD ITEMS LIST']))

    print("\n")

    cursor.execute("select totalprice from storebooking where ticketno = '%s'", [b])
    a=cursor.fetchall()
    print(tabulate(a,headers=['TOTAL PRICE']))
    cursor.close()
    db.close()




def usermain():
    print('\n')
    print('****************************')
    print("1.BOOKING TICKETS")
    print("2.BOOKING INFO")
    print("3. FEEDBACK AND QUERIES")
    print("4.RETURN TO THE MAIN PAGE")
    print("****************************")
    print('\n')
    choose=int(input("ENTER YOUR CHOICE : "))
    if choose==1:
        bookingtickets()
                                                
    elif choose==2:
        usercheck()
    elif choose==3:
        userfeedback()
    elif choose==4:
        main()

def userlogin():
    cursor=db.cursor()
    username=input("ENTER YOUR USERNAME : ")
    password=input("ENTER YOUR PASSWORD: ")
    cursor.execute("select * from userlogin")
    a=cursor.fetchall()
    leng=len(a)
    ch='y'
    while ch=='y':
        for i in range(leng):
            if a[i][0]==username and a[i][1]==password:
                print("you are logged in ")
                ch='n'
                usermain()
                break
        else:
            print("you have entered the wrong id or pass")
            signinsignup()
            break
    cursor.close()
    db.close()

def usersignup():
    try:
        username=input("enter your name")
        password=input("enter your pass")
        cursor=db.cursor()
        cursor.execute("select * from userlogin")
        a=cursor.fetchall()
        leng=len(a)
        for i in range(leng):
            conpass=input("confirm your password: ")
            if conpass==password:
                val=(username,password)
                addval=("insert into userlogin (id,pass) values (%s,%s)")
                cursor.execute(addval,val)
                db.commit()
                print("signed up sucessfully")
                print("now you can sign in in the login page")
                signinsignup()
                break
            else:
                print("your password is not matching")
                signinsignup()
                break
    except:
        print("YOUR ID EXIST OR YOU HAVE ENTERED WRONG INFORMATION PLEASE TRY AGAIN")
        signinsignup()

def signinsignup():
    print('\n')
    print("1. LOGIN INTO AN EXSTING ACCOUNT ")
    print("2. SIGN UP")
    print("IF YOU DONT NOT HAVE AN ACCOUNT PLEASE SIGN UP TO ENJOY OUR SERVICE =-= THANK YOU")
    print('\n')
    enter=int(input("ENTER YOUR CHOICE : "))
    if enter==1:
        userlogin()
    elif enter==2:
        usersignup()




def userfeedback():
    cursor=db.cursor()
    name=input("ENTER YOUR NAME :")
    feed=input("PLEASE ENTER YOUR FEEDBACK ABOUT THE TRAVEL SYSTEM AND IF OU HAVE ANY QURIES OR COMPLAINTS PLEASE TYPE IT")
    val=(name,feed)
    addval='INSERT INTO feedback(name,feedback)VALUES(%s,%s)'
    cursor.execute(addval,val)
    db.commit()
    print("YOUR FEEDBACK HAD BEEN SENT TO ADMIN SUCESSFULLY THANK YOU")
    cursor.close()
    db.close()
    usermain()




#----------------------------ADMIN MODE------------------------------------------------------------------#


def updatefooditems():
    cursor=db.cursor()
    cursor.execute('select * from showeatables order by serialno')
    a=cursor.fetchall()
    b=(a[-1][0])+1
    print('\n')
    print(tabulate(a,headers=['Serial number',"Menu",'Price']))
    print('\n')

    #input values
    item=input("ENTER A NEW FOOD / DRINK NAME: ")
            
    price=int(input("ENTER THE PRICE OF YOUR REQUIRED FOOD / DRINK: "))
    val=(b,item,price)
    add_val='INSERT INTO showeatables(serialno,fooditems,price)VALUES(%s,%s,%s)'
    cursor.execute(add_val,val)
    db.commit()
    print("------------INFORMATION UPDATED SUCESSFULLY------------")
    cursor.close()
    adminmain()
    db.close()





def updateairportname():
    cursor=db.cursor()
    cursor.execute('select * from showlocation order by serialno')
    a=cursor.fetchall()
    b=(a[-1][0])+1
    print('\n')
    print(tabulate(a,headers=['Serial number','airportname','airportcode']))
    print('\n')
    #input values
    airname=input("ENTER A NEW AIRPORT NAME: ")        
    aircode=input("ENTER THE AIRPORT CODE : ")
    val=(b,airname,aircode)
    add_val='INSERT INTO showlocation(serialno,airportname,airportcode)VALUES(%s,%s,%s)'
    cursor.execute(add_val,val)
    db.commit()
    print("------------INFORMATION UPDATED SUCESSFULLY------------")
    cursor.close()
    adminmain()
    db.close()

def updateflightname():
    cursor=db.cursor()
    cursor.execute('select * from showflight order by serialno')
    a=cursor.fetchall()
    b=(a[-1][0])+1
    print('\n')
    print(tabulate(a,headers=['Serial number','flight','price']))
    print('\n')
    #input values
    airlinesname=input("ENTER A NEW AIRLINES: ")
            
    airprice=input("ENTER THE PRICE OD THAT AIRLINES: ")
    val=(b,airlinesname,airprice)
    add_val='INSERT INTO showflight(serialno,flight,price)VALUES(%s,%s,%s)'
    cursor.execute(add_val,val)
    db.commit()
    print("------------INFORMATION UPDATED SUCESSFULLY------------")
    cursor.close()
    adminmain()
    db.close()

def showadminbooking():
    cursor=db.cursor()
    cursor.execute('select ticketno from storebooking')
    a=cursor.fetchall()
    print('\n')
    print(tabulate(a,headers=['ticketno']))
    print('\n')
    print("enter the ticket number for getting their particuar information")
    print('\n')
    usercheck()
    adminmain()
    cursor.close()
    db.close()

def deletefooditems():
    cursor=db.cursor()
    cursor.execute('select * from showeatables order by serialno')
    a=cursor.fetchall()
    print('\n')
    print(tabulate(a,headers=['Serial number',"Menu",'Price']))
    print('\n')
    rem=int(input("ENTER THE SERIAL NUMBER OF FOOD ITEM YOU WANT TO DELETE"))
    cursor.execute("delete from showeatables where serialno = '%s'", [rem])
    db.commit()
    print("------------INFORMATION UPDATED SUCESSFULLY------------")
    cursor.close()
    adminmain()
    db.close()

def deleteairportname():
    cursor=db.cursor()
    cursor.execute('select * from showlocation order by serialno')
    a=cursor.fetchall()
    print('\n')
    print(tabulate(a,headers=['Serial number','airportname','airportcode']))
    print('\n')
    rem=int(input("ENTER THE SERIAL NUMBER OF AIRPORT YOU WANT TO DELETE"))
    cursor.execute("delete from showlocation where serialno = '%s'", [rem])
    db.commit()
    print("------------INFORMATION UPDATED SUCESSFULLY------------")
    cursor.close()
    adminmain()
    db.close()

def deleteflightname():
    cursor=db.cursor()
    cursor.execute('select * from showflight order by serialno')
    a=cursor.fetchall()
    print('\n')
    print(tabulate(a,headers=['Serial number',"flight",'Price']))
    print('\n')
    rem=int(input("ENTER THE SERIAL NUMBER OF AIRLINES YOU WANT TO DELETE"))
    cursor.execute("delete from showflight where serialno = '%s'", [rem])
    db.commit()
    print("------------INFORMATION UPDATED SUCESSFULLY------------")
    cursor.close()
    adminmain()
    db.close()

    

def deletebooking():
    cursor=db.cursor()
    cursor.execute('select ticketno from storebooking ')
    a=cursor.fetchall()
    print('\n')
    print(tabulate(a,headers=['TICKET NUMBER']))
    print('\n')
    rem=int(input("ENTER THE TICKET NUMBER YOU WANT TO REMOVE : "))
    cursor.execute("delete from storebooking where ticketno = '%s'", [rem])
    db.commit()
    print("------------INFORMATION UPDATED SUCESSFULLY------------")
    cursor.close()
    adminmain()
    db.close()

    


def adminmain():
    print('\n')
    print('****************************')
    print("1.ADD AIRPORT NAME ")
    print("2. DELETE AIRPORT NAME")
    print("3.ADD AIRLINES")
    print("4. DELETE AIRLINES")
    print("5.ADD FOOD ITEMS")
    print("6. DELETE FOOD ITEM")
    print("7.LOOK THE BOOKING INFO OF USER ")
    print("8. DELETE BOOKING OF THE COSTUMER")
    print("9.LOOK INTO USER FEEDBACK AND QUERIES")
    print("10.RETURN BACK TO THE MAIN PAGE")
    print("****************************")
    print('\n')
    choose=int(input("ENTER YOUR CHOICE : "))
    if choose==1:
        updateairportname()
                                                
    elif choose==2:
        deleteairportname()
        
    elif choose==3:
        updateflightname()
        
    elif choose==4:
        deleteflightname()
        
    elif choose==5:
        updatefooditems()
        
    elif choose==6:
        deletefooditems()

    elif choose==7:
        usercheck()

    elif choose==8:
        deletebooking()
    elif choose==9:
        adminfeedback()
    elif choose==10:
        main()
        

def adminlogin():
    ch='y'
    cursor=db.cursor()
    cursor.execute("select id,pass from adminlogin")
    a=cursor.fetchall()
    while ch=='y':
        username=input("ENTER YOUR USERNAME : ")
        password=input("ENTER YOUR PASSWORD : ")
        for i in range (len(a)):
            if a[i][0]==username and a[i][1]==password:
                print("----------------SUCCESSFULLY LOGGED IN--------------")
                ch='n'
                adminmain()
                break
            else:
                print("YOU HAVE ENTERED THE WRONG ID OR PASSWORD PLEASE ENTER AGAIN")
                break


def adminfeedback():
    cursor=db.cursor()
    cursor.execute("select * from feedback")
    a=cursor.fetchall()
    print(tabulate(a,headers=['NAME','FEEDBACKS']))
    cursor.close()
    db.close()
    b=int(input("IF YOU FINISHED READING FEEDBACK PRESS 1 TO GET BACK TO THE ADMIN PAGE"))
    if b==1:
        adminmain()




def main():
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    print("********************************************************************************")
    print('\n')
    print("                 WELCOME TO NIZHAM AND HASSAN TRAVELS                        ")
    print('\n')
    print("********************************************************************************")
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    print('\n')
    print("1. USERMODE ")
    print("2. ADMIN MODE")
    enter=int(input("ENTER YOUR CHOICE :"))
    if enter==1:
        signinsignup()
    elif enter==2:
        adminlogin()

main()








    
