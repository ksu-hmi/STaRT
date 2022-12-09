# Test update to City table in World database
# Import the mysql client for python
import pymysql
import pandas as pd
# Add administrators (individuals who can add/edit catastrophes details, locations, and volunteers data)
admins = {'STaRTadmin1':'MOT123','STaRTadmin2':'MOT123'}

# Create a connection object
databaseServerIP            = "127.0.0.1"   # IP address of the MySQL database server
databaseUserName            = "root"        # User name of the database server
databaseUserPassword        = "password"      # Password for the database user
DatabaseName                = "dbname"       # Name of the database that is to be created
charSet                     = "utf8mb4"     # Character set
cursorType                  = pymysql.cursors.DictCursor

connectionObject   = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, db=DatabaseName, charset=charSet,cursorclass=cursorType)
cursor      = connectionObject.cursor() 


### function to veiw Disaster data

sql_query1 = f'SELECT * FROM Disaster;'
sql_query2 = f'SELECT * FROM Location;'
sql_query3 = f'SELECT * FROM Volunteers;'

##########################################################
# Code related to Disaster table: Retrieve-Insert-Update # 
##########################################################
def view_data():
    try:
        with connectionObject.cursor() as cursor:
             cursor.execute(sql_query1)

        # Connection is not autocommit by default, so we must commit to save changes
        connectionObject.commit()
        
        # Fetch all the records from SQL query output
        results = cursor.fetchall()
        
        # Convert results into pandas dataframe
        df = pd.DataFrame(results)
        
        print(f'Successfully retrieved records')
        print(df)
        return df
              
    except Exception as e:
        print(f'Error encountered: {e}')

### function to insert Disaster data 
       
def  insert_disaster_data():
    Disaster_Name = input("Enter Disaster Name To Update: ")
    Disaster_Type = input("Enter Disaster Type: ")
    Disaster_Reason = input("Enter Disaster_Reason: ")
    Disaster_Country = input("Enter Disaster Country: ")
    Disaster_State = input("Enter Disaster State: ")
    Disaster_Date = input("Enter Disaster Date (format: MM/DD/YYYY): ")
    try:
        with connectionObject.cursor() as cursor:
            q2 = f"INSERT INTO Disaster (Disaster_Name, Disaster_Type, Disaster_Reason,\
                                           Disaster_Country, Disaster_State, Disaster_Date) \
                                           VALUES (%s, %s, %s, %s, %s, %s);"
            cursor.execute(q2, (Disaster_Name, Disaster_Type, Disaster_Reason,\
                                Disaster_Country, Disaster_State, Disaster_Date))
 # Connection is not autocommit by default, so we must commit to save changes
        connectionObject.commit()
        print(f'Successfully inserted records')
        
    except Exception as e:
        print(f'Error in insertion to MySQL database: {e}')

### function to update Disaster data record

def  update_disaster_data():
    cursor      = connectionObject.cursor()
    name=str(input("Enter the disaster name to update: "))
    q="select * from Disaster where Disaster_Name =%s"
    cursor.execute(q,name)
    record = cursor.fetchone()
    print(record)
    while True:

        print('''
            
            1 = edit type
            2 = edit reason
            3 = edit country      
            4 = edit state
            5 = edit date
            6 = Exit''')

        feature = input("Enter which feature of the data do you want to edit: ")
        

        
        if (feature == "1"):
            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                name=str(input("Enter the disaster name to update: "))
                update_value = str(input ("Enter the new value: "))
                
                sql = "UPDATE Disaster set Disaster_Type= %s Where Disaster_Name=%s"
                data=(update_value,name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass
        elif (feature == "2"):
            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                name=str(input("Enter the disaster name to update: "))
                update_value = str(input ("Enter disaster reason new value: "))
                
                sql = "UPDATE Disaster set Disaster_Reason= %s Where Disaster_Name=%s"
                data=(update_value,name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass
        
        elif (feature == "3"):

            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                name=str(input("Enter the disaster name to update: "))
                update_value = str(input ("Enter disaster country new value: "))
                
                sql = "UPDATE Disaster set Disaster_Country= %s Where Disaster_Name=%s"
                data=(update_value,name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass
        elif (feature == "4"):
            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                name=str(input("Enter the disaster name to update: "))
                update_value = str(input ("Enter disaster state new value: "))
                
                sql = "UPDATE Disaster set Disaster_State= %s Where Disaster_Name=%s"
                data=(update_value,name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass
        elif (feature == "5"):
            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                name=str(input("Enter the disaster name to update: "))
                update_value = str(input ("Enter disaster date new value: "))
                
                sql = "UPDATE Disaster set Disaster_Date= %s Where Disaster_Name=%s"
                data=(update_value,name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass
        elif(feature == "6"):
            connectionObject.close()
            print("THANK YOU !")
            break
        


##########################################################
# Code related to Location table: Retrieve-Insert-Update # 
##########################################################
 
# function to view location data
def view_location_data():
    try:
        with connectionObject.cursor() as cursor:
             cursor.execute(sql_query2)

        # Connection is not autocommit by default, so we must commit to save changes
        connectionObject.commit()
        
        # Fetch all the records from SQL query output
        results = cursor.fetchall()
        
        # Convert results into pandas dataframe
        df2 = pd.DataFrame(results)
        
        print(f'Successfully retrieved records')
        print(df2)
        return df2
              
    except Exception as e:
        print(f'Error encountered: {e}')   



### function to insert Location data
def  insert_location_data():
    Location_ID = int(input("Enter Location ID To Update: "))
    Location_County = input("Enter Location County: ")
    Location_Address = input("Enter Location Address: ")
    Location_City = input("Enter Location City: ")
    Location_Zip = input("Enter Location Zip: ")
    Location_VictimsNbr = int(input("Enter Location Victims Number: "))
    Location_Type = input ("enter Location Type: ")
    Location_Tag = input ("Enter Location Tag: ")
    Related_Disaster = input ("enter Related Disaster: ").lower()
    q="select * from location where Location_ID='Location_ID'"
    cursor.execute(q)
    row=cursor.fetchone()
    
    if(row==None):
        print("New Location record created")
        sql_1 = """INSERT INTO location (Location_ID, Location_County, Location_Address, 
        Location_City, Location_Zip, Location_VictimsNbr, Location_Type, Location_Tag, Related_Disaster)
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        val_1 = (Location_ID, Location_County, Location_Address,
         Location_City, Location_Zip, Location_VictimsNbr, Location_Type, Location_Tag, Related_Disaster)
        cursor.execute(sql_1, val_1)
        connectionObject.commit()
        connectionObject.close()
        print(f'Successfully inserted records')


###########################################################
# Code related to Volunteer table: Retrieve-Insert-Update # 
###########################################################
#### Volunteer Details
# function to view volunteers data
def view_volunteer_data():
    try:
        with connectionObject.cursor() as cursor:
             cursor.execute(sql_query3)

        # Connection is not autocommit by default, so we must commit to save changes
        connectionObject.commit()
        
        # Fetch all the records from SQL query output
        results = cursor.fetchall()
        
        # Convert results into pandas dataframe
        df3 = pd.DataFrame(results)
        
        print(f'Successfully retrieved records')
        print(df3)
        return df3
              
    except Exception as e:
        print(f'Error encountered: {e}')   

### function to insert Volunteers data
def  insert_volunteer_data():
    Volunteer_FirstName = input("Enter Volunteer First Name: ")
    Volunteer_LastName = input("Enter Volunteer Last Name: ")
    Volunteer_FullName = (Volunteer_FirstName + ' ' + Volunteer_LastName)
    Volunteer_Age = int(input("Enter Volunteer Age: "))
    Volunteer_Expertise = input("Enter Volunteer Expertise: ")
    Volunteer_Certification = input ("enter Volunteer Certification: ")
    Volunteer_Location = int(input ("Enter Volunteer Location: "))

    q4="select * from Volunteers where Volunteer_FullName = 'Volunteer_FullName'"
    cursor.execute(q4)
    row=cursor.fetchone()
    if(row==None):
        
        sql4 = """INSERT INTO Volunteers (Volunteer_FullName, Volunteer_FirstName,
                Volunteer_LastName, Volunteer_Age, Volunteer_Expertise, 
                Volunteer_Certification, Volunteer_Location)
                  VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        val4 = (Volunteer_FullName, Volunteer_FirstName, Volunteer_LastName,
               Volunteer_Age, Volunteer_Expertise, Volunteer_Certification, Volunteer_Location)
        cursor.execute(sql4, val4)
        connectionObject.commit()
        connectionObject.close()
        print(f'Successfully inserted new volunteer record')
 ### function to update Disaster data record

def  update_volunteer_data():
    cursor      = connectionObject.cursor()
    full_name=input("Enter the volunteer full name to update: ")
    q="select * from Volunteers where Volunteer_FullName =%s"
    cursor.execute(q,full_name)
    record = cursor.fetchone()
    print(record)
    while True:

        print('''
            
            
            1 = edit age   
            2 = edit expertise
            3 = edit certification
            4 = edit location 
            5 = Exit''')

        feature = input("Enter which feature of the data do you want to edit: ")
        

        
        if (feature == "1"):
            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                full_name=input("Enter the Full name to update: ")
                update_value = int(input ("Enter the age new value: "))
                
                sql = "UPDATE  Volunteers set Volunteer_Age= %s Where Volunteer_FullName=%s"
                data=(update_value,full_name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass
        elif (feature == "2"):
            try:
                 #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                full_name=input("Enter the Full name to update: ")
                update_value = input ("Enter the expertise new value: ")
                
                sql = "UPDATE  Volunteers set Volunteer_Expertise= %s Where Volunteer_FullName=%s"
                data=(update_value,full_name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass

        elif (feature == "3"):

            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                full_name=input("Enter the Full name to update: ")
                update_value = input ("Enter the certification new value: ")
                
                sql = "UPDATE  Volunteers set Volunteer_Certification =%s Where Volunteer_FullName=%s"
                data=(update_value,full_name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass



        elif (feature == "4"):
            try:
                #This sets a spot in the database connection (cursor) for targeted retrieval
                cursor      = connectionObject.cursor()
                full_name=input("Enter the Full name to update: ")
                update_value = int(input ("Enter the volunteer location new value: "))
                
                sql = "UPDATE  Volunteers set Volunteer_Location= %s Where Volunteer_FullName=%s"
                data=(update_value,full_name)
                cursor.execute(sql,data)
                
                connectionObject.commit() 
                print("Record Updated successfully ")
                # total number of rows updated
                print("Total rows updated: %d" % cursor.rowcount)
            except Exception as e:
                print(e)
            pass
        
        elif(feature == "5"):
            connectionObject.close()
            print("THANK YOU !")
            break
               

 ### function to delete volunteer data record

def delete_volunteer_record():
    #This to view the data
    view_volunteer_data()
    #This sets a spot in the database connection (cursor) for targeted retrieval
    
    cursor      = connectionObject.cursor() 
    full_name=  input("Enter the full name data record to delete:")

    try:
        delete_sql = "DELETE FROM Volunteers WHERE Volunteer_FullName= %s"
        cursor.execute(delete_sql,full_name)
        connectionObject.commit() #capture the result of the commit and use it to check the result
        print ("Disaster ",full_name, "  deleted.")
        print(cursor.rowcount, "record(s) deleted")
    except Exception as e:
        print (e)
        pass




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
    # disaster details
    if action == '1':
        print('You have selected 1 - catastrophe details')
        print("1 to view the data")
        print("2 to insert a new data record")
        print("3 to update a data record")
        print("4 to delete a data record")
        print("X to exit")
        name = input ("Choose an operation to perform: ").lower()
        if (name =="1"):
            for row in view_data():
                thisrow = "  --> "
                for item in row:
                    thisrow += str(item) + "  "
                print (thisrow)
        elif(name == "2"):
            insert_disaster_data()()
        elif(name == "3"):
            update_disaster_data()
        elif(name == "4"):
            delete_record()
        elif(name == "X"):
            connectionObject.close()
        
    elif action == '2':
        print('You have selected 2 - Location details')
        print("1 to view the data")
        print("2 to insert a new data record")
        print("3 to update a data record")
        print("4 to delete a data record")
        print("X to exit")
        name = input ("Choose an operation to perform: ").lower()
        if (name =="1"):
            for row in view_location_data():
                thisrow = "  --> "
                for item in row:
                    thisrow += str(item) + "  "
                print (thisrow)
        elif(name == "2"):
            insert_location_data()()
        elif(name == "3"):
            update_location_data()
        elif(name == "4"):
            delete_location_record()
        elif(name == "X"):
            connectionObject.close()
    
    elif action == '3':
        print('You have selected 2 - Volunteer details')
        print("1 to view the data")
        print("2 to insert a new data record")
        print("3 to update a data record")
        print("4 to delete a data record")
        print("X to exit")
        name = input ("Choose an operation to perform: ").lower()
        if (name =="1"):
            for row in view_volunteer_data():
                thisrow = "  --> "
                for item in row:
                    thisrow += str(item) + "  "
                print (thisrow)
        elif(name == "2"):
            insert_volunteer_data()()
        elif(name == "3"):
            update_volunteer_data()
        elif(name == "4"):
            delete_volunteer_record()
        elif(name == "X"):
            connectionObject.close()
        
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

