# The Simple Triage and Rapid Treatment (STaRT) application will be used by community-based organizations who are prepared
# to serve as a crucial resource capable of performing many of the emergency functions needed in the immediate post-disaster
# period or in emergency cases. 

# This application was developed by MS students in HMI program at Kennesaw State University.
# Students' names are: Farah Muttardy, Richard Ogniewski, Elie Tannouri

# Add administrators (individuals who can add/edit catastrophes details, locations, and volunteers data)
admins = {'STaRTadmin1':'MOT123','STaRTadmin2':'MOT123'}

# Like the admins above, we have a dictionary of volunteers. Dictionaries use curly brackets with colons to associate keys with values. 
# In this case, each volunteer  Id  is a key. The values are first and last name ,expertise, date of birth, and location. 

volunteers = {'12-21':['Alex Smith''med tech', '1-28-1975', 'Powder Springs '],
            '12-22':['Sally Thomson','CNA', '3-5-1995', 'Marietta'],
            '12-23':['Jeff Carpenter','Certified Nurse', '4-22-1997','Marietta']}

# Another dicitionary is the locations. The key to each location is area, the list includes: zip code, type of location 
# (residential, commercial, park), Hurricane name, tagged (Yes/No), number of victims found
locations = {'Powder Springs': '30127, residential, Hugo, Yes, 1',
            'Marietta': '30061, commercial, Katrina, No, 10'}

# Another dicitionary is the catastrophe names. The key to each catastrophe is the catastrophe name. The list includes:
# Date of occurence, type of disaster (fire, hurricane, tornado), state

catastrophes = {'Katrina':['Louisiana'],
                'Hugo':['Florida']}            

#Now we define 1st function. Allows admin to add catastrophe details, locations, and volunteer data.
def enterCatastrophes():
    CatastropheName = input('Catastrophe name: ')
    CatastropheState = input('Catastrophe state: ')
    #This checks through the keys of the catastrophe dictionary to see if the name entered exactly matches any one in there.
    if CatastropheName in catastrophes:
        print('Adding another state for'+CatastropheName)
        catastrophes[CatastropheName].append(CatastropheState)
        print(str(CatastropheName)+' now has these states:')
        print(catastrophes)
    else:
        catastrophes.update({CatastropheName:[CatastropheState]})
        # to add a new element to dictionary use dictionary name and .update
        print(catastrophes)
        #print('Student not found. Please check your spelling or go back and add if new.')

#def enterLocations():

#def enterVolunteers():

def main():
    print("User: " + login)
    #Here we present STaRT main menu options once an admin logs in successfully.
    print(""" 
    Welcome to STaRT Application - an Application for tracking disaster discovery
    [1] - Enter Catastrophe Details
    [2] - Enter Locations Details
    [3] - Enter Volunteer Details
    [4] - Exit
    """)

    action = input('What would you like to do? (Enter a number) ')
    #Here we process their choice of what they want to do.
    if action == '1':
        print('1 selected - enter catastrophe details')
        enterCatastrophes()
    elif action == '2':
        print('2 selected - enter location details')
        enterLocations()
    elif action == '3':
         print('3 selected - enter volunteer details')
        enterVolunteers()
    elif action == '4':
        print('4 selected - Exit')
        exit()
    else:
    print('Valid option not selected.')

login = input('User: ')

if login in admins:
    password = input('Password: ')
    if admins[login] == password:
        print('Welcome,',login)
        #now run the code
        while True:
            main()
    else:
        print('Invalid password.')
else:
    print('Invalid user.')
