# Test update to City table in World database
# Import the mysql client for python
import pymysql

# Add administrators (individuals who can add/edit catastrophes details, locations, and volunteers data)
admins = {'STaRTadmin1':'MOT123','STaRTadmin2':'MOT123'}

# Create a connection object
databaseServerIP            = "127.0.0.1"   # IP address of the MySQL database server
databaseUserName            = "root"        # User name of the database server
databaseUserPassword        = "KSUHMI"      # Password for the database user
DatabaseName                = "Start2"       # Name of the database that is to be created
charSet                     = "utf8mb4"     # Character set
cursorType                  = pymysql.cursors.DictCursor

connectionObject   = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, db=DatabaseName, charset=charSet,cursorclass=cursorType)
cursorObject       = connectionObject.cursor() 

# added new code for different functions to update tables
### function to update/insert Disaster data

def enterDisaster():
    Disaster_Name = input("Enter Disaster Name To Update: ")
    Disaster_Type = input("Enter Disaster Type: ")
    Disaster_Reason = input("Enter Disaster_Reason: ")
    Disaster_Country = input("Enter Disaster Country: ")
    Disaster_State = input("Enter Disaster State: ")
    Disaster_Date = input("Enter Disaster Date (format: MM/DD/YYYY): ")

    q="select * from disaster where Disaster_Name='Disaster_Name'"
    cursorObject.execute(q)
    row=cursorObject.fetchone()
    
    if(row==None):
        print("New Disaster record created")
        sql = "INSERT INTO disaster (Disaster_Name, Disaster_Type, Disaster_Reason, Disaster_Country, Disaster_State, Disaster_Date) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (Disaster_Name, Disaster_Type, Disaster_Reason, Disaster_Country, Disaster_State, Disaster_Date)
        cursorObject.execute(sql, val)
        connectionObject.commit()
        connectionObject.close()
    
    else:
        print('record found')

        sql = "UPDATE disaster SET Disaster_Type = 'Disaster_Type', Disaster_Reason = 'Disaster_Reason', Disaster_Country='Disaster_Country', Disaster-State='Disaster_State', Disaster_Date='Disaster_Date' WHERE Disaster_Name= 'Rich'"
        cursorObject.execute(sql)  
        connectionObject.commit()
        connectionObject.close()

#################################################

### function to update/insert Location data

def enterLocation():
    Location_ID = input("Enter Location ID To Update: ")
    Location_County = input("Enter Location County: ")
    Location_Address = input("Enter Location Address: ")
    Location_City = input("Enter Location City: ")
    Location_Zip = input("Enter Location Zip: ")
    Location_VictimsNbr = input("Enter Location Victims Number: ")
    Location_Type = input ("enter Location Type: ")
    Location_Tag = input ("Enter Location Tag: ")
    Related_Disaster = input ("enter Related Disaster: ")

    q="select * from location where Location_ID='Location_ID'"
    cursorObject.execute(q)
    row=cursorObject.fetchone()
    
    if(row==None):
        print("New Location record created")
        sql = "INSERT INTO location (Location_ID, Location_County, Location_Address, Location_City, Location_Zip, Location_VictimsNbr, Location_Type, Location_Tag, Related_Disaster) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (Location_ID, Location_County, Location_Address, Location_City, Location_Zip, Location_VictimsNbr, Location_Type, Location_Tag, Related_Disaster)
        cursorObject.execute(sql, val)
        connectionObject.commit()
        connectionObject.close()
    else:
        print ("Record Found") 
        #sql = "UPDATE location SET Location_ID WHERE Location_ID = Location_ID"
        #val = (Location_County, Location_Address, Location_City, Location_Zip, Location_VictimsNbr, Location_Type, Location_Tag, Related_Disaster)
        #cursorObject.execute(sql, val)  
        #connectionObject.commit()
        #connectionObject.close()

###################################################
### function to update/insert Volunteer data

def enterVolunteer():
    

##################################################
### function to update/insert Victim data

def enterVictim():



#############################################
# Main functions

def main():
    print("User: " + login)
    #Here we present STaRT main menu options once an admin logs in successfully.
    print(""" 
    Welcome to STaRT Application - an Application for tracking disaster discovery
    [1] - Enter Disaster Details
    [2] - Enter Location Details
    [3] - Enter Volunteer Details
    [4] - Exit
    """)

    action = input('What would you like to do? (Enter a number:) ')
    # Here we process the admin choice of what they want to do.
    if action == '1':
        print('1 selected - enter catastrophe details')
        enterDisaster()
    elif action == '2':
        print('2 selected - enter location details')
        enterLocation()
    elif action == '3':
        print('3 selected - enter volunteer details')
        enterVolunteer()
    elif action == '4':
        print('4 selected - Exit')
        exit()
    else:
        print('Valid option not selected.')

def main1():
    print(""" 
    Welcome to STaRT Application - an Application for tracking disaster discovery
    [5] - Enter Victim Details
    [6] - Exit
    """)

    action = input('What would you like to do? (Enter a number:) ')
    # Here we process the admin choice of what they want to do.
    if action == '5':
        print('5 selected - enter victim details')
        enterVictim()
    elif action == '6':
        print('6 selected - Exit')
        exit()
    else:
        print ('Valid option not selected')    

# Login code

login = input('User: ')
if login in admins:
    password = input('Password: ')
    if admins[login] == password:
        print('Welcome,',login)
        #now run the code
        #while True:
        main()
    else:
        print('Invalid password.')
elif login in volunteers:
    print('Welcome', login)
    main1()
else:   
    print('Invalid user.')

