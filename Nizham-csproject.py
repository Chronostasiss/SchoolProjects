#Airline reservation software

import datetime#input datetime.date
import mysql.connector
from tabulate import tabulate
import random


mydb=mysql.connector.connect(
        host="127.0.0.1",
        username="root",
        passwd="bismillah",
        database="csproject")

if mydb.is_connected():
        print("Successfully connected to MYSQL Server")



print()
print("***************** WELCOME TO OUR AIRLINE RESERVATION SYSTEM *****************")
print("*****************       Echo Airline is at your service     *****************")
print("***************** For more than 150 destination around the world  *****************")
print()
ch='YES'
while ch=='YES':
	mydb=mysql.connector.connect(
        host="127.0.0.1",
        username="root",
        passwd="bismillah",
        database="csproject")
	
	def login():
		print("1.ADMIN ONLY: ")
		print("2.Log in as an existing customer: ")
		print("3.Sign in as a new customer: ")
		print("4.Enter as a Guest: ")
		print("5.To exit the program")
		c1=int(input("Enter your choice: "))

		if c1==1:
			def admin_login():

			    j=0
			    ch='y'
			    cursor=mydb.cursor()
			    cursor.execute('select username,password from admin ')
			    a=cursor.fetchall()
			    while ch=='y':

			        nm=input('Enter Username:')
			        pswd=input('Enter Password: ')
			        
			        for i in a:

			            if i[0]==nm:

			                if i[1]==pswd:

			                    print('\n Successfully logged in')

			                    j=1
			                    ch='yes'
			                    while ch=='yes':

				                    def menu():
				                    	print('\n')
				                    	print('****************************')
				                    	print("1.To alter passengers information: ")
				                    	print("2.To alter eatables food menu: ")
				                    	print("3.To alter luggage table: ")
				                    	print("4.To alter classtype table: ")
				                    	print("5.Back to main ")
				                    	print("****************************")
				                    	print("")
				                    	print('\n')

				                    menu()

				                    def food_drinks():
				                    	cursor=mydb.cursor()
				                    	cursor.execute('select * from eatables')
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=['Serial number',"Menu",'Price']))

				                    	#input values
				                    	item=input("Enter a new food/drink name: ")
				                    	price=int(input("Enter the price of it: "))
				                    	val=(item,price)
				                    	add_val='INSERT INTO eatables(eatableslist,price)VALUES(%s,%s)'
				                    	cursor.execute(add_val,val)
				                    	mydb.commit()
				                    	cursor.close()
				                    	mydb.close()

				                    

				                    def passenger_info():
				                    	cursor=mydb.cursor()
				                    	cursor.execute('select * from passenger')
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=['Serial Number',"Name","Address","Mobile Number","Departure","Arrival","Departure Date","Arrival Date"]))
				                    	#inputing value
				                    	cursor.close()
				                    	mydb.close()

				                    

				                    def price_luggage():
				                    	cursor=mydb.cursor()
				                    	cursor.execute("select * from luggage")
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=['Serial Number','Weight','Price']))
				                    	cursor.close()
				                    	mydb.close()

				                    def class_type():
				                    	cursor=mydb.cursor()
				                    	cursor.execute("select * from classtype")
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=["Serial Number","Class Type","Price"]))
				                    	cursor.close()
				                    	mydb.close()

				                    

				                    opt=""
				                    opt=int(input("Enter your choice: "))
				                    if opt==1:
				                    	passenger_info()

				                    elif opt==2:
				                    	food_drinks()

				                    elif opt==3:
				                    	price_luggage()

				                    elif opt==4:
				                    	class_type()

				                    else:
				                    	a=input("Do you want to continue? (y/n):" )
				                    	if a=='y':
				                    		ch='yes'
				                    	elif a=='n':
				                    		break



			                else:
			                    print('\n Password incorrect ')
			                    j=2
			                    break
			                
			            
			        if j==1:
			            break
			        else:
			            if j==0:
			                print('Name incorrect')
			                ch=input('Do you want to enter name and password again (y/n): ')
			                if ch=='y':
			                    continue
			                else:
			                    break
			            elif j==2:
			                ch=input('Do you want to enter name and password again (y/n): ')
			                if ch=='y':
			                    continue
			                else:
			                    break

			    cursor.close()
			    mydb.close()

			admin_login()


		if c1==2:

			def customer_login():


			    j=0
			    ch='y'
			    cursor=mydb.cursor()
			    cursor.execute('select username,password from customer ')
			    a=cursor.fetchall()
			    while ch=='y':

			        nm=input('Enter Username:')
			        pswd=input('Enter Password: ')
			        
			        for i in a:

			            if i[0]==nm:

			                if i[1]==pswd:

			                    

			                    j=1
			                    ch='yes'
			                    while ch=='yes':
			                    	
				                    def c_menu():
				                    	print("\n")
				                    	print("****************************")
				                    	print("Please follow the procedure")
				                    	print("1. Register your information")
				                    	print("2. Choose your meal and beverages")
				                    	print("3. Pick your desired classtype")
				                    	print("4. Check in your luggage weight")
				                    	print("5.Back to main menu")
				                    	print("****************************")
				                    	print("\n")

				                    c_menu()

				                    def c_passenger_info():
				                    	cursor=mydb.cursor()
				                    	cursor.execute('select * from passenger')
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=['Serial Number',"Name","Address","Mobile Number","Departure","Arrival","Departure Date","Arrival Date"]))    
				                    	nos=int(input("Enter your ticket number: "))
				                    	name=input("Enter your name: ")
				                    	address=input("Enter your address: ")
				                    	mob_nos=int(input("Enter your mobile number: "))
				                    	dep=input("Enter departure location: ")
				                    	arriv=input("Enter Arrival location: ")
				                    	dep_date=input(datetime.date)
				                    	arriv_date=input(datetime.date)
				                    	val=(name,address,mob_nos,dep,arriv,dep_date,arriv_date)
				                    	add_info="INSERT INTO bookinginfo(ticketno,name,address,mobilenumber,departure,arrival,departuredate,arrivaldate)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
				                    	cursor.execute(add_info,val)
				                    	mydb.commit()
				                    	cursor.close()
				                    	mydb.close()

				                    def c_food_drinks():
				                    	cursor=mydb.cursor()
				                    	cursor.execute("select * from eatables")
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=['Serial Number','Name','Price']))
				                    	nos=int(input("Enter your unique ID :"))
				                    	food=input("Enter desired food/beverage : ")
				                    	for i in food:
				                    		if food=="Chicken Burger":
				                    			p=4
				                    		elif food=="Beef Burger":
				                    			p=6
				                    		elif food=="Fish Fillet":
				                    			p=7
				                    		elif food=="Chicken Fillet":
				                    			p=5
				                    		elif food=="Fried Rice":
				                    			p=4
				                    		elif food=="Mineral Water":
				                    			p=1
				                    		elif food=="Lemon Iced Tea":
				                    			p=2
				                    		elif food=="Black Coffee":
				                    			p=2
				                    		elif food=="Black Tea":
				                    			p=2
				                    		elif food=="Green Tea":
				                    			p=2
				                    		elif food=="Fruit Juice":
				                    			p=1
				                    		elif food=="Soft Drinks":
				                    			p=1
				                    		else:
				                    			print("Wrong Input")
				                    		break
				                    	new_p=p
				                    	val=(nos,food,new_p)
				                    	add_menu="INSERT INTO bookinginfo(orderedeatables,oeprice)VALUES(%s,%s)"
				                    	cursor.execute(add_menu,val)
				                    	mydb.commit()
				                    	cursor.close()
				                    	mydb.close()


				                    def c_class_type():
				                    	cursor=mydb.cursor()
				                    	cursor.execute("select * from classtype")
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=['Serial Number','Class Type',"Price"]))
				                    	print()
				                    	print("The above information are the classes and its corresponding prices!  ")
				                    	nos=input("Enter your ticker number: ")
				                    	ordered_class=input("Enter class of your choice: ")
				                    	for i in ordered_class:
				                    		if ordered_class=='First Class':
				                    			p=575
				                    			print("The price will be ",p)
				                    		elif ordered_class=="Business":
				                    			p=475
				                    			print("The price will be ",p)
				                    		elif ordered_class=='Economy':
				                    			p=375
				                    			print("The price will be ",p)
				                    		else:
				                    			print("Invalid input!!")
				                    		break
				                    	new_p=p
				                    	val=(nos,ordered_class,new_p)
				                    	add_val="INSERT INTO bookinginfo(orderedclass,ocprice)VALUES(%s,%s)"
				                    	cursor.execute(add_val,val)
				                    	mydb.commit()
				                    	cursor.close()
				                    	mydb.close()


				                    def c_price_luggage():
				                    	cursor=mydb.cursor()
				                    	cursor.execute("select * from luggage")
				                    	a=cursor.fetchall()
				                    	print(tabulate(a,headers=['Serial Number','We',"Price"]))
				                    	nos=int(input("Enter your ticker number: "))
				                    	w=int(input("Enter weight: "))
				                    	for i in range (w):
				                    		if w>=40 and w<=50:
				                    			print("the weight you have entered exceeds the limit,you will be charged with extra fees")
				                    			new_w=45+((w-40)*10)
				                    			print("The new rated price is ",new_w,'BD')
				                    		elif w>=50 and w<=60:
				                    			print("the weight you have entered exceeds the limit,you will be charged with extra fees")
				                    			new_w=65+((w-40)*20)
				                    			print("The new rated price is ",new_w,'BD')
				                    		elif w>=60 and w<=70:
				                    			print("the weight you have entered exceeds the limit,you will be charged with extra fees")
				                    			new_w=85+((w-40)*30)
				                    			print("The new rated price is ",new_w,'BD')
				                    		else:
				                    			print("We're sorry,but the weight you have entered exceeds our quoted weight for each passenger! ")
				                    		break

				                    	price=new_w
				                    	val=(nos,w,price)
				                    	add_info="INSERT INTO bookinginfo(weightchecked,totalprice)VALUES(%s,%s)"
				                    	cursor.execute(add_info,val)
				                    	mydb.commit()
				                    	cursor.close()
				                    	mydb.close()

				                    opt=""
				                    opt=int(input("Enter your choice: "))
				                    if opt==1:
				                    	c_passenger_info()
				                    elif opt==2:
				                    	c_food_drinks()
				                    elif opt==3:
				                    	c_class_type()
				                    elif opt==4:
				                    	c_price_luggage()
				                    else:
				                    	a=input("Do you want to continue? (y/n):" )
				                    	if a=='y':
				                    		ch='yes'
				                    	elif a=='n':
				                    		break

			                else:
			                    print('\n Password incorrect ')
			                    j=2
			                    break
			                

			            
			        if j==1:
			            break
			        else:
			            if j==0:
			                print('Name incorrect')
			                ch=input('Do you want to enter name and password again (y/n): ')
			                if ch=='y':
			                    continue
			                else:
			                    break
			            elif j==2:
			                ch=input('Do you want to enter name and password again (y/n): ')
			                if ch=='y':
			                    continue
			                else:
			                    break

			    cursor.close()
			    mydb.close()

			customer_login()


		if c1==3:

			def register_customer_login():
				cursor=mydb.cursor()
				cursor.execute("select * from customer")
				a=cursor.fetchall()

				#input values
				print()
				print("*************DISCLAIMER*************")
				print()
				print("1. Your ticker number will be automatically generated")
				print("2.The ticket number will not be able to be changed in the future")
				print()
				name=input("Enter your username: ")
				pswd=input("Enter your password(only alphabets): ")
				ticket_no=random.randint(1111,9999)
				print("This is your ticket number: ",ticket_no)
				val=(ticket_no,name,pswd)
				add_info="INSERT INTO customer(ticketno,username,password)VALUES(%s,%s,%s)"
				cursor.execute(add_info,val)
				print("Successfully registered")
				mydb.commit()
				cursor.close()
				mydb.close()
			register_customer_login()

		if c1==4:
			print("Kindly sign in to fully enjoy our services :)")

		if c1==5:
			a=input("Do you really want to stop (y/n): ")
			if a=='n':
				ch='YES'	
			else:
				print("Thank You")
				
							

	login()



    
    
usercheck()

	    
