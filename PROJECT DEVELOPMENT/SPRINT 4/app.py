from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re
app = Flask(__name__)
app.secret_key = 'zumakkazu'

#conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PORT=31498;UID=pln17877;PWD=qLKg9nf0PdYAPg55;",'','')


@app.route('/')
def homer():
    return render_template('login.html')

@app.route('/dash')
def dashbod():
    return render_template('dashboard.html')

@app.route('/loggedin',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        #account = ibm_db.fetch_assoc(stmt)
        account = username+password
        print (account)
        if username=='kaavya':
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg = msg)
        elif account:
            session['loggedin'] = True
            session['id'] = account
            userid= username
            session['username'] = username
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg = msg)
            # if(username=='boo'):
            #     print("yes")
            #     return render_template('dashboard.html', msg = 'Trueee')
            # print('No')
            # print(username)
            # return render_template('login.html', msg = 'Incorrect Try again or Signup')

@app.route('/register', methods =['GET', 'POST'])
def registet():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # sql = "SELECT * FROM users WHERE username =?"
        # stmt = ibm_db.prepare(conn, sql)
        # ibm_db.bind_param(stmt,1,username)
        # ibm_db.execute(stmt)
        # account = ibm_db.fetch_assoc(stmt)
        account =''
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            # insert_sql = "INSERT INTO users VALUES (?, ?, ?)"
            # prep_stmt = ibm_db.prepare(conn, insert_sql)
            # ibm_db.bind_param(prep_stmt, 1, username)
            # ibm_db.bind_param(prep_stmt, 2, email)
            # ibm_db.bind_param(prep_stmt, 3, password)
            # ibm_db.execute(prep_stmt)
            msg = 'You have successfully registered !'
            return render_template('dashboard.html',msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')


@app.route('/apply',methods =['GET', 'POST'])
def apply():
    msg = ''
    return render_template('apply.html', msg = msg)

    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        qualification= request.form['qualification']
        skills = request.form['skills']
        jobs = request.form['s']
        # sql = "SELECT * FROM users WHERE username =?"
        # stmt = ibm_db.prepare(conn, sql)
        # ibm_db.bind_param(stmt,1,username)
        # ibm_db.execute(stmt)
        # account = ibm_db.fetch_assoc(stmt)
        # print(account)
        # if account:
        #     msg = 'there is only 1 job position! for you'
        #     return render_template('apply.html', msg = msg)
        # insert_sql = "INSERT INTO job VALUES (?, ?, ?, ?, ?)"
        # prep_stmt = ibm_db.prepare(conn, insert_sql)
        # ibm_db.bind_param(prep_stmt, 1, username)
        # ibm_db.bind_param(prep_stmt, 2, email)
        # ibm_db.bind_param(prep_stmt, 3, qualification)
        # ibm_db.bind_param(prep_stmt, 4, skills)
        # ibm_db.bind_param(prep_stmt, 5, jobs)
        # ibm_db.execute(prep_stmt)
        msg = 'Action successfully performed !'
        session['loggedin'] = True
        TEXT = "Hello sandeep,a new appliaction for job position" +jobs+"is requested"
        #sendmail(TEXT,"sandeep@thesmartbridge.com")
        #sendgridmail("sandeep@thesmartbridge.com",TEXT)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('apply.html', msg = msg)


@app.route('/display')
def display():
    print(session["username"],session['id'])

    # cursor = mysql.connection.cursor()
    # cursor.execute('SELECT * FROM job WHERE userid = % s', (session['id'],))
    # account = cursor.fetchone()
    account='selfdefinedradei'
    print("accountdislay",account)
    return render_template('display.html',account = account)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)