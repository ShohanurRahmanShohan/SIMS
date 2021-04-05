from time import sleep
import csv
import ast
#Student_data load From CSV ..
Student_list = []
d = dict()
f = open("Student_Roll.csv")
for line in f:
   line = line.strip('\n')
   (key, val) = line.split(",")
   d[key] = val
   Student_list= d
#Student_data End here __

print ("""
 .----..----. .-.  .-. .----. 
{ {__-`} {-. \}  \/  {{ {__-` 
.-._} }} '-} /| {  } |.-._} } 
`----' `----' `-'  `-'`----'  
\n
Student management system   \n
[-]Quick Note [-]\n \nIf you wanted to change Roll of any student do it from \nStudent_data.csv all student data store on this csv
 \n[-]Quick Note [-]
\n __  __                  
 |  \/  |                 
 | \  / | ___ _ __  _   _ 
 | |\/| |/ _ \ '_ \| | | |
 | |  | |  __/ | | | |_| |
 |_|  |_|\___|_| |_|\__,_| \n
[1] Check Student By Name \n
[2] Check Student Paid on Not \n
[3] Register New Student \n
[4] Add student name who paid  \n  
""")
try :
	user_select =int(input("[+] Please select option by number : "))
except : 
   print("""\n Please Enter Number not cerector \n
Control C for exit the program
    """)
   sleep(30)
# Frist menu 
if user_select ==1 :
    #User_input  For Finding Roll by name 
    Student_name_input = input("Student name : ")
    student_name= Student_name_input.          islower()
    if (student_name==False) :
        print ()
        print()
        print("""Please Enter name lowercase \n [×]'Name' \n [✓]'name'
        """)
        print("×××××××××××××××××××××××")
    try :
        s =     str(Student_list[Student_name_input])
        print(" \n [√]Roll is - ",s)
    except :
         print(Student_name_input,"Isn't- Registered ")
#user input Finished for roll frsit menu 

#Secound  menu 
if user_select==2 :
  S= open("Student_paid.csv")
  student_list2=[]
  for line in S:
        line = line.strip('\n')
        (key, val) = line.split(",")
        d[key] = val
        student_list2= d
  Student_name_input = input("Student name : ")
  student_name= Student_name_input.          islower()
  if (student_name==False) :
        print ()
        print()
        print("""Please Enter name lowercase \n [×]'Name' \n [✓]'name'
        """)
        print("×××××××××××××××××××××××")
  try :
     sl= int(student_list2[Student_name_input])
     if sl==1:
     	print(Student_name_input, "\nShe/he pay the feee ")
     else  :
     	print(Student_name_inout, "Don't pay the fee ")
  except :
         print("\n This name isn't exict !! ")



#Thrid menu 
if user_select==3:
	  print("""\n Enter Student name like this :\n
	[✓] example {'harry' : '10' , 'shohan' : '20'} 
	[+] write name inside {    }
	[+] write name inside quot ' name ' /n
	[+] put colon after name 'name' : 
	[+] write down roll like name 'name':"roll"
	[+]use comma to assine multiple student \n """)
	  try :
	      my_dict = input("Student list :  ")
	      or_dict =  ast.literal_eval(my_dict)
	      with open('Student_Roll.csv', 'w') as w :
	        for key in or_dict.keys()  :
	        	w.write("%s,%s\n"%(key,or_dict[key]))
	        	print ("Done!!! List updated ")
	  except : 
	      	  print("""\nPlease  Enter Student name like this :\n
	[✓] example {'harry' : '10' , 'shohan' : '20'} 
	[+] write name inside {    }
	[+] write name inside quot ' name ' /n
	[+] put colon after name 'name' : 
	[+] write down roll like name 'name':"roll"
	[+]use comma to assine multiple student \n """)



#Forth ..
if user_select==4:
	  print("""\n Enter Student name like this :\n
	[✓] example {'harry' : '1' , 'shohan' : '1'} 
	[+] write name inside {    }
	[+] write name inside quot ' name ' /n
	[+] put colon after name 'name' : 
	[+] write down 1 like after colon 'name':'1' \n 1 means he paid 
	[+]use comma to assine multiple student \n """)
	  try :
	      my_dict = input("Student list :  ")
	      or_dict =  ast.literal_eval(my_dict)
	      with open('Student_paid.csv', 'w') as w :
	        for key in or_dict.keys()  :
	        	w.write("%s,%s\n"%(key,or_dict[key]))
	        	print ("Done!!! List updated ")
	  except : 
	      	  print("""\nPlease  Enter Student name like this :\n
	[✓] example {'harry' : '10' , 'shohan' : '20'} 
	[+] write name inside {    }
	[+] write name inside quot ' name ' /n
	[+] put colon after name 'name' : 
	[+] write down roll like name 'name':"roll"
	[+]use comma to assine multiple student \n """)

#Thrid menu 
if user_select==3:
	  print("""\n Enter Student name like this :\n
	[✓] example {'harry' : '10' , 'shohan' : '20'} 
	[+] write name inside {    }
	[+] write name inside quot ' name ' /n
	[+] put colon after name 'name' : 
	[+] write down roll like name 'name':"roll"
	[+]use comma to assine multiple student \n """)
	  try :
	      my_dict = input("Student list :  ")
	      or_dict =  ast.literal_eval(my_dict)
	      with open('Student_Roll.csv', 'w') as w :
	        for key in or_dict.keys()  :
	        	w.write("%s,%s\n"%(key,or_dict[key]))
	        	print ("Done!!! List updated ")
	  except : 
	      	  print("""\nPlease  Enter Student name like this :\n
	[✓] example {'harry' : '10' , 'shohan' : '20'} 
	[+] write name inside {    }
	[+] write name inside quot ' name ' /n
	[+] put colon after name 'name' : 
	[+] write down roll like name 'name':"roll"
	[+]use comma to assine multiple student \n """) 
	