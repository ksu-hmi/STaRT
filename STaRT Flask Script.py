from flask import Flask, render_template, request,redirect
import pymysql

#set the mysql workbench connection
def connection():
    s = '127.0.0.1' #Your server(host) name 
    d = 'Start2'# your database name 
    u = '' #Your login user
    p = '' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

app=Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    username="STaRTadmin1"
    password="MOT123"
    inputName = request.form['myName']
    inputPassword = request.form['password']
    if inputName == username and inputPassword == password:
         return redirect('/disaster/')


@app.route('/')
def home():
    return render_template("home.html",myName="Type your username in the box and click submit!")

@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/disaster/')
def disaster():
    Disaster = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Disaster")
    for row in cursor.fetchall():
        Disaster.append({"Disaster_Name": row[0], "Disaster_Type": row[1], "Disaster_Reason": row[2], "Disaster_Country": row[3],"Disaster_State":row[4],"Disaster_Date":row[5]})
    conn.close()
    return render_template("disasterslist.html", Disasters = Disaster)

@app.route('/adddisaster', methods = ['GET','POST'])
def adddisaster():
    if request.method == 'GET':
        return render_template("adddisaster.html", Disaster= {})
    if request.method == 'POST':
        Disaster_Name = str(request.form["Disaster_Name"])
        Disaster_Reason = str(request.form["Disaster_Reason"])
        Disaster_Type = str(request.form["Disaster_Type"])
        Disaster_Country = str(request.form["Disaster_Country "])
        Disaster_State = str(request.form["Disaster_State "])
        Disaster_Date = str(request.form["Disaster_Date"])
       
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO disaster(Disaster_Name, Disaster_Type, Disaster_Reason, Disaster_Country , Disaster_State , Disaster_Date) VALUES (%s, %s, %s, %s, %s, %s)", (Disaster_Name, Disaster_Type, Disaster_Reason, Disaster_Country , Disaster_State , Disaster_Date))
        conn.commit()
        conn.close()
        
        return redirect('/')
@app.route('/updatedisaster/<int:Disaster_Name>',methods = ['GET','POST'])
def updatedisaster(Disaster_Name):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM disaster WHERE Disaster_Name = %s", (Disaster_Name))
        for row in cursor.fetchall():
            cr.append({"Disaster_Name": row[0], "Disaster_Type": row[1], "Disaster_Reason": row[2], "Disaster_Country": row[3],"Disaster_State": row[4], "Disaster_Date":row[5]})
        conn.close()
        return render_template("adddisaster.html", Disaster= cr[0])
    if request.method == 'POST':
        Disaster_Type= str(request.form["Disaster_Type"])
        Disaster_Reason = str(request.form["Disaster_Reason"])
        Disaster_Country = str(request.form["Disaster_Country "])
        Disaster_State =str(request.form["Disaster_State "])
        Disaster_Date= str(request.form["Disaster_Date"])
        cursor.execute("UPDATE disaster SET Disaster_Type = %s, Disaster_Reason= %s, Disaster_Country= %s ,Disaster_State=%s,Disaster_Date=%s WHERE Disaster_Name = %s", ( Disaster_Type, Disaster_Reason, Disaster_Country, Disaster_State, Disaster_Date))
        conn.commit()
        conn.close()
        return redirect('/')
@app.route('/deletedisaster <int:Disaster_Name>')
def deletedisaster(Disaster_Name):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM disaster WHERE Disaster_Name= %s", (Disaster_Name))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
