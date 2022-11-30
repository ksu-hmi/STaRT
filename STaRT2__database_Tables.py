# import the mysql client for python

import pymysql

 

# Create a connection object

dbServerName    = "127.0.0.1"

dbUser          = ""

dbPassword      = ""

dbName          = "STaRT_Database"

charSet         = "utf8mb4"

cusrorType      = pymysql.cursors.DictCursor

 

connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,

                                     db=dbName, charset=charSet,cursorclass=cusrorType)

try:

                                     



    cursorObject        = connectionObject.cursor()                                     

 
     # SQL query string creating database tables

     #SQL creating Disaster table
     # Disaster_Type allowed values:fire, hurricane, tornado, random shooting
 

    Q1        = """CREATE TABLE Disaster(Disaster_Name varchar(50) PRIMARY KEY ,
                     Disaster_Type varchar(50), Disaster_Reason varchar(50),Disaster_Country varchar(50),
                     Disaster_State varchar(50),Disaster_Date varchar(50))""" 

    
    #SQL creating Location table
     #Location_Type allowed values:residential, commercial, park, staging area
     #Related_Disaster is a foreign key to Disaster table. Related_Disaster must exist in Disaster table to update
     #Location_VictimsNbr is a counter that is incremented from the Victims table"""

    Q2         = """CREATE TABLE Location (Location_ID int PRIMARY KEY ,Location_County varchar(50), 
                      Location_Address varchar(50),Location_City varchar(50) ,Location_Zip varchar(50),
                      Location_VictimsNbr int,Location_Type varchar(50),Location_Tag boolean,Related_Disaster varchar(50),
                      FOREIGN KEY (Related_Disaster) REFERENCES  Disaster(Disaster_Name))"""

    #SQL creating Volunteer table:
    #Volunteer Full Name is a combination of Volunteer_FirstName and Volunteer_LastName

    Q3            = """CREATE TABLE Volunteers(Volunteer_FullName varchar(50) PRIMARY KEY,
                         Volunteer_FirstName varchar(50) ,Volunteer_LastName varchar(50), 
                         Volunteer_Age int,Volunteer_Expertise varchar(50),
                        Volunteer_Certification varchar(50),Volunteer_Location int,
                        FOREIGN KEY (Volunteer_Location) REFERENCES Location(Location_ID))""" 
 
    #SQL creating Victims table:
    #Related_Disaster is a foreign key to Diaster table. Related_Disaster must exist in Disaster table to update
     #LocationID_Found and Assigned_LocationID are foreign keys to Location table. Locations must exist in Location table to update
     #Volunter_Name is a foreign key to Volunteer table. Volunteer_Name must exist in Volunteer table to update

    Q4            = """CREATE TABLE Victims(Victim_FullName varchar(50) PRIMARY KEY,
                        Victim_FirstName varchar(50) ,Victim_LastName varchar(50), 
                         Victim_Age int,Triage_Date int, Process_Steps  varchar(50),
                         Final_Disposition varchar(50),Related_Disaster varchar(50),
                         LocationID_Found int,Volunteer_Name varchar(50),Assigned_LocationID int , 
                        FOREIGN KEY (Related_Disaster) REFERENCES Disaster(Disaster_Name),
                        FOREIGN KEY (LocationID_Found) REFERENCES Location(Location_ID),
                        FOREIGN KEY (Volunteer_Name) REFERENCES Volunteers(Volunteer_FullName),
                        FOREIGN KEY (Assigned_LocationID) REFERENCES Location(Location_ID))""" 

    #SQL creating Victim_Minor table:
    #No edits allowed in this table. Conditionally updated based on Victims table

    Q5        = """CREATE TABLE Victim_Minor(Victim_FullName varchar(50) PRIMARY KEY,
                     Victim_Age int,Related_Disaster varchar(50),Assigned_LocationID int,
                     FOREIGN KEY (Victim_FullName) REFERENCES Victims(Victim_FullName),
                     FOREIGN KEY (Related_Disaster) REFERENCES Disaster(Disaster_Name),
                     FOREIGN KEY (Assigned_LocationID) REFERENCES Location(Location_ID))"""

    #SQL creating Victim_Immediate table:
    #No edits allowed in this table. Conditionally updated based on Victims table

    Q6        = """CREATE TABLE Victim_Immediate(Victim_FullName varchar(50) PRIMARY KEY,
                     Victim_Age int,Related_Disaster varchar(50),Assigned_LocationID int,
                     FOREIGN KEY (Victim_FullName) REFERENCES Victims(Victim_FullName),
                     FOREIGN KEY (Related_Disaster) REFERENCES Disaster(Disaster_Name),
                     FOREIGN KEY (Assigned_LocationID) REFERENCES Location(Location_ID))"""
                 
    #SQL creating Victim_Delayed table:
    #No edits allowed in this table. Conditionally updated based on Victims table

    Q7        = """CREATE TABLE Victim_Delayed(Victim_FullName varchar(50) PRIMARY KEY,
                     Victim_Age int,Related_Disaster varchar(50),Assigned_LocationID int,
                     FOREIGN KEY (Victim_FullName) REFERENCES Victims(Victim_FullName),
                     FOREIGN KEY (Related_Disaster) REFERENCES Disaster(Disaster_Name),
                     FOREIGN KEY (Assigned_LocationID) REFERENCES Location(Location_ID))"""
                 
    #SQL creating Victim_Dead table:
    #No edits allowed in this table. Conditionally updated based on Victims table

    Q8        = """CREATE TABLE Victim_Dead(Victim_FullName varchar(50) PRIMARY KEY,
                     Victim_Age int,Related_Disaster varchar(50),Assigned_LocationID int,
                     FOREIGN KEY (Victim_FullName) REFERENCES Victims(Victim_FullName),
                     FOREIGN KEY (Related_Disaster) REFERENCES Disaster(Disaster_Name),
                     FOREIGN KEY (Assigned_LocationID) REFERENCES Location(Location_ID))"""
                 
         
 

    # Execute the sqlQuery

    cursorObject.execute(Q1)
    cursorObject.execute(Q2)
    cursorObject.execute(Q3)
    cursorObject.execute(Q4)
    cursorObject.execute(Q5)
    cursorObject.execute(Q6)
    cursorObject.execute(Q7)
    cursorObject.execute(Q8)


   

    # SQL query string

    sqlQuery            = "show tables"   

 

    # Execute the sqlQuery

    cursorObject.execute(sqlQuery)

   

 

    #Fetch all the rows

    rows                = cursorObject.fetchall()

 

    for row in rows:

        print(row)

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionObject.close()