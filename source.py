import tkinter as tk
import mysql.connector
from tkinter import *
  
 
db = mysql.connector.connect(host ="localhost",
                                    user = 'root',
                                    db ="priorityqueue")
cursor = db.cursor()
  
root2 = tk.Tk()

root2.geometry("950x400")
root2.title("Theme Park Priority Queue System")

frame1=Frame(master=root2, width=300, height=200)
frame1.place(x=0,y=0)

frame2=Frame(master=root2, width=300, height=200)
frame2.place(x=300,y=0)

frame3=Frame(master=root2, width=300, height=200)
frame3.place(x=0,y=200)

frame4=Frame(master=root2, width=300, height=200)
frame4.place(x=300,y=200)

frame5=Frame(master=root2, width=300, height=200)
frame5.place(x=600,y=0)

frame6=Frame(master=root2, width=300, height=200)
frame6.place(x=600,y=200)
  
labelArray=[]
for x in range(50):
    label=Label(frame1)
    label.pack(side=TOP)
    labelArray.append(label)

def queryGuests():
     
    
         
   
    savequery = "select * from GUEST"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
         
        
        
        for x in range(50):
            labelArray[x].config(text='')
        i=0
        for x in myresult:
            labelArray[i].config(text=x)
            i=i+1
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")
  
 


  
 


 
submitbtn = tk.Button(root2, text ="Query Guests",
                      bg ='gray', command = queryGuests)
submitbtn.place(x = 100, y = 175, width = 100)

def submitaddguest():
     
    name = Nameentry.get()
    gid = Identry.get()
  
    print(f"The name entered by you is {name} {gid}")
  
    addguest(name, gid)

def submitremoveguest():
     
    name = Nameentry.get()
    gid = Identry.get()
  
    print(f"The name entered by you is {name} {gid}")
  
    removeguest(name, gid)
 
 
def addguest(name, gid):
     
   
    add_guest = ("INSERT INTO GUEST "
               "(GUEST_ID, NAME) "
               "VALUES (%s, %s)")
    data_guest=(int(gid), name)
     
    try:
        cursor.execute(add_guest, data_guest)
        db.commit()
        
         
    except:
        db.rollback()
        print("Error occured")
  
 
def removeguest(name, gid):
     
   
    remove_guest = "DELETE FROM GUEST WHERE GUEST_ID="+gid
    data_guest=(int(gid))
    print(data_guest) 
    try:
        cursor.execute(remove_guest)
        db.commit()
        
         
    except:
        db.rollback()
        print("Error occured")


lblfrstrow = tk.Label(frame3, text ="Guest Name", )
lblfrstrow.place(x = 50, y = 20)
 
Nameentry = tk.Entry(frame3, width = 35)
Nameentry.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(frame3, text ="Guest ID")
lblsecrow.place(x = 50, y = 50)
 
Identry = tk.Entry(frame3, width = 35)
Identry.place(x = 150, y = 50, width = 100)
 
submitbtn2 = tk.Button(root2, text ="Add Guest",
                      bg ='gray', command = submitaddguest)
submitbtn2.place(x = 100, y = 280, width = 100)

submitbtn3 = tk.Button(root2, text ="Remove Guest",
                      bg ='gray', command = submitremoveguest)
submitbtn3.place(x = 100, y = 320, width = 100)




#rightside

labelArray2=[]
for x in range(50):
    label=Label(frame2)
    label.pack(side=TOP)
    labelArray2.append(label)

def queryTimes():
     
    
         
  
    savequery = "select * from APPOINTMENT_TIMES"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
       
        
        for x in range(50):
            labelArray2[x].config(text='')
        i=0
        for x in myresult:
            labelArray2[i].config(text=x)
            i=i+1
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")
  
 


  


 
submitbtn4 = tk.Button(root2, text ="Query Appointment Times",
                      bg ='gray', command = queryTimes)
submitbtn4.place(x = 400, y = 175, width = 200)

def submitaddtime():
     
    timeID = Nameentry2.get()
    attractionID = Identry2.get()
    time = Timeentry.get()
  
    print(f"The name entered by you is {timeID} {attractionID}")
  
    addtime(timeID, attractionID, time)

def submitremovetime():
     
    timeID = Nameentry2.get()
  
    print(f"The name entered by you is {timeID}")
  
    removetime(timeID)
 
 
def addtime(timeID, attractionID, time):
     
   
    add_time = ("INSERT INTO APPOINTMENT_TIMES "
               "(APPOINTMENT_ID, ATTRACTION_ID, APPOINTMENT_TIME) "
               "VALUES (%s, %s, %s)")
    data_time=(timeID, attractionID, time)
     
    try:
        cursor.execute(add_time, data_time)
        db.commit()
        
         
    except:
        db.rollback()
        print("Error occured")
  
 
def removetime(timeID):
     
   
    remove_time = "DELETE FROM APPOINTMENT_TIMES WHERE APPOINTMENT_ID="+timeID
     
    try:
        cursor.execute(remove_time)
        db.commit()
        
         
    except:
        db.rollback()
        print("Error occured")


lblfrstrow2 = tk.Label(frame4, text ="Appointment ID", )
lblfrstrow2.place(x = 50, y = 20)
 
Nameentry2 = tk.Entry(frame4, width = 35)
Nameentry2.place(x = 150, y = 20, width = 100)
  
lblsecrow2 = tk.Label(frame4, text ="Attraction ID")
lblsecrow2.place(x = 50, y = 50)
 
Identry2 = tk.Entry(frame4, width = 35)
Identry2.place(x = 150, y = 50, width = 100)

timerow2 = tk.Label(frame4, text ="Time")
timerow2.place(x = 50, y = 80)
 
Timeentry = tk.Entry(frame4, width = 35)
Timeentry.place(x = 150, y = 80, width = 100)
 
submitbtn5 = tk.Button(root2, text ="Add Time",
                      bg ='gray', command = submitaddtime)
submitbtn5.place(x = 400, y = 310, width = 100)

submitbtn6 = tk.Button(root2, text ="Remove Time",
                      bg ='gray', command = submitremovetime)
submitbtn6.place(x = 400, y = 350, width = 100)



#farright

labelArray3=[]
for x in range(50):
    label=Label(frame5)
    label.pack(side=TOP)
    labelArray3.append(label)

def queryAppointments():
     
    

    savequery = "select GUEST_APPOINTMENTS.GUEST_ID, GUEST.NAME, GUEST_APPOINTMENTS.APPOINTMENT_ID, ATTRACTION.ATTRACTION_NAME, APPOINTMENT_TIMES.APPOINTMENT_TIME from GUEST_APPOINTMENTS INNER JOIN APPOINTMENT_TIMES ON GUEST_APPOINTMENTS.APPOINTMENT_ID = APPOINTMENT_TIMES.APPOINTMENT_ID INNER JOIN ATTRACTION ON ATTRACTION.ATTRACTION_ID=APPOINTMENT_TIMES.ATTRACTION_ID INNER JOIN GUEST ON GUEST.GUEST_ID=GUEST_APPOINTMENTS.GUEST_ID"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
         
  
        for x in range(50):
            labelArray3[x].config(text='')
        i=0
        for x in myresult:
            labelArray3[i].config(text=x)
            i=i+1
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")
  
 


  
 


 
submitbtn7 = tk.Button(root2, text ="Query Appointments",
                      bg ='gray', command = queryAppointments)
submitbtn7.place(x = 700, y = 175, width = 200)

def submitaddapp():
     
    appID = Nameentry3.get()
    gID = Identry3.get()

  
  
  
    addapp(appID, gID)

def submitremoveapp():
     
    appID = Nameentry3.get()
  
    gID = Identry3.get()
  
    removeapp(appID, gID)
 
 
def addapp(appID, gID):
     
   
    add_app = ("INSERT INTO GUEST_APPOINTMENTS "
               "(GUEST_ID, APPOINTMENT_ID) "
               "VALUES (%s, %s)")
    data_app=(gID, appID)
     
    try:
        cursor.execute(add_app, data_app)
        db.commit()
        
         
    except:
        db.rollback()
        print("Error occured")
  
 
def removeapp(appID, gID):
     
   
    remove_app = "DELETE FROM GUEST_APPOINTMENTS WHERE APPOINTMENT_ID="+appID +" AND GUEST_ID ="+gID
     
    try:
        cursor.execute(remove_app)
        db.commit()
        
         
    except:
        db.rollback()
        print("Error occured")


lblfrstrow3 = tk.Label(frame6, text ="Appointment ID", )
lblfrstrow3.place(x = 50, y = 20)
 
Nameentry3 = tk.Entry(frame6, width = 35)
Nameentry3.place(x = 150, y = 20, width = 100)
  
lblsecrow3 = tk.Label(frame6, text ="Guest ID")
lblsecrow3.place(x = 50, y = 50)
 
Identry3 = tk.Entry(frame6, width = 35)
Identry3.place(x = 150, y = 50, width = 100)

 
submitbtn8 = tk.Button(root2, text ="Add Appointment",
                      bg ='gray', command = submitaddapp)
submitbtn8.place(x = 700, y = 310, width = 150)

submitbtn9 = tk.Button(root2, text ="Remove Appointment",
                      bg ='gray', command = submitremoveapp)
submitbtn9.place(x = 700, y = 350, width = 150)




 
root2.mainloop()
