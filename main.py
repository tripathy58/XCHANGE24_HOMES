

from getpass import getuser
import pymysql
from flask import Flask, render_template, session, redirect, request, flash, json, url_for, jsonify,abort
import re
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
import os
from flask_mail import *
from random import *
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key'

app.config.from_pyfile('config.py')

mysql = MySQL()

mysql.init_app(app)

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

# for otp verification

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ashishtripathy58@gmail.com'
app.config['MAIL_PASSWORD'] = 'mtodxrbxrfmpbiaa'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = 'ashish'
mail = Mail(app)


otp = randint(0000, 9999)
otp2 = randint(0000, 9999)
otp3 = randint(0000, 9999)


conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'wepe', 'mp4'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


  
# # app name
# @app.errorhandler(404)
  
# # inbuilt function which takes error as parameter
# def not_found(e):
  
# # defining function
#   return render_template("404.html")

# at the application level
# not the blueprint level
@app.errorhandler(404)
def page_not_found(e):
    # if a request is in our blog URL space
    if request.path.startswith('/blog/'):
        # we return a custom blog 404 page
        return render_template("blog/404.html"), 404
    else:
        # otherwise we return our generic site-wide 404 page
        return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500

@app.errorhandler(405)
def method_not_allowed(e):
    # if a request has the wrong method to our API
    if request.path.startswith('/api/'):
        # we return a json saying so
        return jsonify(message="Method Not Allowed"), 405
    else:
        # otherwise we return a generic site-wide 405 page
        return render_template("405.html"), 405


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM user_login WHERE email = "' +
                   session['email']+'" ')
        user = cursor.fetchone()
        cursor.execute('''SELECT *,image2,substring_index(substring_index(image2, ',', -1), ',', 1) photo 
FROM ads WHERE status = "Enable" 
                     ''')
        location = cursor.fetchall()
    # cursor.execute('SELECT * FROM ads WHERE status = "Enable" ')
        cursor.execute('''SELECT *,image2,
        substring_index(substring_index(image2, ',', -1), ',', 1) photo 
        FROM ads WHERE status = "Enable" ''')
        ads = cursor.fetchall()

        if request.method == 'POST':
            location = request.form['location']
            cursor.execute("UPDATE user_login SET location=%s WHERE email = '" +
                    session['email']+"' ",(location))
            
            conn.commit()
            flash('Location Set Successfully','success')
            return redirect('/')
        

        if request.method == 'POST':
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            if confirm_password != password:
                flash("password doesn't match")
                return render_template("home_.html")
            else:
                cursor.execute('UPDATE user_login SET password = %s WHERE email = "' +
                            session['email'] + '" ', (password))
                conn.commit()
                flash('Password Changed Successfully')
                return redirect('/user_profile')
        return render_template('home_.html', ads=ads,user=user, location=location)
    else:
        cursor.execute('''SELECT *,image2,
        substring_index(substring_index(image2, ',', -1), ',', 1) photo 
        FROM ads WHERE status = "Enable" ''')
        ads = cursor.fetchall()
        
        return render_template('home_.html', ads=ads)


@app.route('/product_details_/<string:id>', methods=['GET', 'POST'])
def product_details(id):
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM user_login WHERE email = "' +
                   session['email']+'" ')
        user = cursor.fetchone()
        cursor.execute("""SELECT *, image2,
    substring_index(substring_index(image2, ',', -1), ',', 1) photo,
        substring_index(substring_index(image2, ',', -2), ',', 1) photo2,
    substring_index(substring_index(image2, ',', -3), ',', 1) photo3,
    substring_index(substring_index(image2, ',', -4), ',', 1) photo4,
    substring_index(substring_index(image2, ',', -5), ',', 1) photo5

    
    FROM ads WHERE id = %s """, (id))
        pds = cursor.fetchall()
        cursor.execute(
            'SELECT * FROM ads WHERE city = (SELECT city FROM ads WHERE id=%s) ', (id))
        img = cursor.fetchall()
        return render_template('product_details_.html', pds=pds, img=img, user=user)
    else:
        cursor.execute("""SELECT *, image2,
    substring_index(substring_index(image2, ',', -1), ',', 1) photo,
        substring_index(substring_index(image2, ',', -2), ',', 1) photo2,
    substring_index(substring_index(image2, ',', -3), ',', 1) photo3,
    substring_index(substring_index(image2, ',', -4), ',', 1) photo4,
    substring_index(substring_index(image2, ',', -5), ',', 1) photo5

    
    FROM ads WHERE id = %s """, (id))
        pds = cursor.fetchall()
        cursor.execute(
            'SELECT * FROM ads WHERE city = (SELECT city FROM ads WHERE id=%s) ', (id))
        img = cursor.fetchall()
        return render_template('product_details_.html', pds=pds, img=img)

@app.route('/status_', methods=['GET', 'POST'])
def status():
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM user_login WHERE email = "' +
                   session['email']+'" ')
        user = cursor.fetchone()
        cursor.execute(
            'SELECT * FROM status WHERE date BETWEEN CURDATE() - INTERVAL 1 DAY AND CURRENT_DATE ORDER BY id DESC ')
        status = cursor.fetchall()

        return render_template('status_.html', status=status,user=user)
    else:
        cursor.execute(
            'SELECT * FROM status WHERE date BETWEEN CURDATE() - INTERVAL 1 DAY AND CURRENT_DATE ORDER BY id DESC ')
        status = cursor.fetchall()

        return render_template('status_.html', status=status)

@app.route('/set_location', methods=['GET', 'POST'])
def set_location():
        location = cursor.execute('''SELECT *,image2,substring_index(substring_index(image2, ',', -1), ',', 1) photo 
FROM ads WHERE status = "Enable"
 AND locality = (SELECT location FROM user_login     )
                     ''')
        # location = cursor.fetchall()
        return jsonify(location)

    # return render_template('home_.html', status=status)

@app.route('/register_', methods=['GET', 'POST'])
def register_():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        cursor.execute('SELECT * FROM user_login WHERE email = %s', (email))
        account = cursor.fetchone()

        if account:
            msg = 'Account already exists! Please LOGIN'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
            return render_template("register_.html")
        elif len(password) <= 6 and re.match(r'[A-Za-z0-9^@]+', password):
            msg = 'Password minimum 6 characters and must contain one upper case letter,special character and numbers!'
            return render_template("register_.html")
        elif confirm_password != password:
            msg = "password doesn't match"
            return render_template("register_.html")
        elif not email or not password or not name or not confirm_password:
            msg = 'Please fill out the form!'
            return render_template("register_.html")

        elif email and password and confirm_password:
            cursor.execute(
                'INSERT INTO user_login (name, email, password) VALUES (%s, %s, %s)',
                (name, email, password))
            conn.commit()
            msg = 'Successfully registered. Login To Continue...'

            return 'Success'
        else:
            msg = 'Wrong Crenditals'

    return render_template('register_.html', msg=msg)


@app.route('/login_', methods=['GET', 'POST'])
def login_():

    if request.method == 'POST' and 'email' in request.form:
        email = request.form['email']

        cursor.execute(
            'SELECT * FROM user_login WHERE email = %s ', (email))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            msg = Message(subject='OTP', sender='XCHANGE24 HOMES',
                          recipients=[email])
            msg.body = str(
                otp) + '\n This one time password is only use for login to the website.'
            mail.send(msg)
            # flash('OTP has been sent to your registered Email. Please Check your Inbox.')
            return 'Sent successfully'
        # else:
        #     flash('Incorrect email/password! Please Register First')

    if request.method == 'POST' and 'email' in request.form:
        email = request.form['email']

        cursor.execute(
            'SELECT * FROM admin_login WHERE email = %s ', (email))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            msg = Message(subject='OTP', sender='XCHANGE24 HOMES',
                          recipients=[email])
            msg.body = str(
                otp2) + '\n This one time password is only use for login to the website.'
            mail.send(msg)
            return 'Sent successfully'
        # else:
        #     flash('Incorrect email/password! Please Register First')

    if request.method == 'POST' and 'email' in request.form:
        email = request.form['email']

        cursor.execute(
            'SELECT * FROM employee WHERE email = %s ', (email))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            msg = Message(subject='OTP', sender='XCHANGE24 HOMES',
                          recipients=[email])
            msg.body = str(
                otp3) + '\n This one time password is only use for login to the website.'
            mail.send(msg)
            flash('Successfully Loggedin','success')
            return 'Sent successfully'
        else:
            flash('Incorrect email/password! Please Register First','error')
    return render_template('login_.html', )


@app.route('/admin_login_', methods=['GET', 'POST'])
def admin_login_():
    if request.method == 'POST' and 'email' in request.form:
        email = request.form['email']

        cursor.execute(
            'SELECT * FROM admin_login WHERE email = %s ', (email))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            msg = Message(subject='OTP', sender='XCHANGE24 HOMES',
                          recipients=[email])
            msg.body = str(
                otp2) + '\n This one time password is only use for login to the website.'
            mail.send(msg)
            return 'Sent successfully'
    return render_template('dashboard_.html')


@app.route('/password_login_', methods=['GET', 'POST'])
def password_login_():

    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor.execute(
            'SELECT * FROM user_login WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            flash('Successfully Loggedin','success')
            return redirect('/')
        
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor.execute(
            'SELECT * FROM admin_login WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            flash('Successfully Loggedin','success')
            return redirect('/dashboard_')
        # else:
        #     flash('Incorrect email/password.')
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor.execute(
            'SELECT * FROM employee WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            flash('Successfully Loggedin','success')
            return redirect('/employee_product_')
        else:
            flash('Incorrect email/password!','error')
            return redirect('/')

    return render_template('home_.html')


@app.route('/admin_password_login_', methods=['GET', 'POST'])
def admin_password_login_():
    cursor.execute("SELECT  COUNT(id ) AS no_of_user FROM user_login ")
    user = cursor.fetchone()
    cursor.execute("SELECT  COUNT(id ) AS total_ads FROM ads ")
    total_ads = cursor.fetchone()
    cursor.execute(
        "SELECT  COUNT(id ) AS total_ads_enable FROM ads WHERE status = 'Enable' ")
    total_ads_enable = cursor.fetchone()
    cursor.execute(
        "SELECT  COUNT(id ) AS total_ads_disable FROM ads WHERE status = 'Disable' ")
    total_ads_disable = cursor.fetchone()
    cursor.execute('SELECT * FROM user_login')
    user_detail = cursor.fetchall()
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor.execute(
            'SELECT * FROM admin_login WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            flash('Successfully Loggedin.','success')
            return redirect('/dashboard_')
        else:
            flash('Incorrect email/password.','error')
    return render_template('dashboard_.html', user=user, total_ads=total_ads, user_detail=user_detail, total_ads_enable=total_ads_enable, total_ads_disable=total_ads_disable)


@app.route('/verify_', methods=['GET', 'POST'])
def verify_():
    msgg = ''
    if request.method == 'POST':
        user_otp = request.form['otp']
        if otp == int(user_otp):
            flash('Verified. Logged In','success')
            return redirect('/')
    
        elif otp2 == int(user_otp):
            flash('Verified. Logged In','success')
            return redirect('/dashboard_')

        elif otp3 == int(user_otp):
            flash('Verified. Logged In','success')
            return redirect('/employee_product_')
        else:
            flash('Invalid Otp.Check Your Inbox for correct OTP.','error')
            return redirect('/')

    return render_template('home_.html')

@app.route('/admin_verify_', methods=['GET', 'POST'])
def admin_verify_():
    msgg = ''
    if request.method == 'POST':
        user_otp = request.form['otp']
        
        if otp2 == int(user_otp):
            flash('Verified. Logged In Successfully.','success')
            return redirect('/dashboard_')

        
        else:
            flash('Invalid Otp.Check Your Inbox for correct OTP.','error')
            return redirect('/dashboard_')

    return render_template('dashboard_.html')

@app.route('/user_profile', methods=['GET', 'POST'])
def user_profile():
    cursor.execute('SELECT * FROM user_login WHERE email = "' +
                   session['email']+'" ')
    user = cursor.fetchone()
    cursor.execute('SELECT * FROM review WHERE email = "' +
                   session['email']+'" ')
    review = cursor.fetchall()
    msg = ''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        address1 = request.form['address1']
        address2 = request.form['address2']
        pin = request.form['pin']
        city = request.form['city']

        cursor.execute("UPDATE user_login SET name=%s,email=%s,mobile=%s,address1=%s,address2=%s,pin=%s,city=%s WHERE email = %s ",
                       (name, email, mobile, address1, address2, pin, city, email))
        conn.commit()
        flash('Updated successfully','success')
        return redirect('/user_profile')
    return render_template('user_profile.html', user=user, review=review)


@app.route('/user_upload_photo', methods=['GET', 'POST'])
def user_upload_photo():
    if request.method == 'POST':
        image = request.files.getlist('image[]')
        # print(image)
        for file in image:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cursor.execute("UPDATE user_login SET  image=%s WHERE email='" +
                       session['email'] + "'", [filename])

        conn.commit()

        flash('Image successfully uploaded','success')
        return redirect('/user_profile')
    return render_template('user_profile.html')


@app.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()
    cursor.execute('SELECT * FROM review  ')
    review = cursor.fetchall()
    cursor.execute(
        'SELECT * FROM status WHERE date BETWEEN CURDATE() - INTERVAL 1 DAY AND CURRENT_DATE ORDER BY id DESC ')
    status = cursor.fetchall()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']

        cursor.execute("UPDATE admin_login SET name=%s,email=%s,mobile=%s WHERE email = %s ",
                       (name, email, mobile,  email))
        conn.commit()
        flash('Details Updated successfully','success')
        return redirect('/admin_profile')
    return render_template('admin_profile.html', admin=admin, review=review, status=status)


@app.route('/admin_upload_photo', methods=['GET', 'POST'])
def admin_upload_photo():
    if request.method == 'POST':
        image = request.files.getlist('image[]')
        # print(image)
        for file in image:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cursor.execute("UPDATE admin_login SET  image=%s WHERE email='" +
                       session['email'] + "'", [filename])

        conn.commit()

        flash('Profile photo successfully uploaded','success')
        return redirect('/admin_profile')
    return render_template('admin_profile.html')


@app.route('/employee_profile', methods=['GET', 'POST'])
def employee_profile():
    cursor.execute('SELECT * FROM employee WHERE email = "' +
                   session['email']+'" ')
    employee = cursor.fetchone()
    cursor.execute('SELECT * FROM review  ')
    review = cursor.fetchall()
    cursor.execute(
        'SELECT * FROM status WHERE date BETWEEN CURDATE() - INTERVAL 1 DAY AND CURRENT_DATE ORDER BY id DESC ')
    status = cursor.fetchall()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']

        cursor.execute("UPDATE employee SET name=%s,email=%s,mobile=%s WHERE email = %s ",
                       (name, email, mobile,  email))
        conn.commit()
        flash('Details Updated successfully','success')
        return redirect('/employee_profile')
    return render_template('employee_profile.html', employee=employee, review=review, status=status)


@app.route('/employee_upload_photo', methods=['GET', 'POST'])
def employee_upload_photo():
    if request.method == 'POST':
        image = request.files.getlist('image[]')
        # print(image)
        for file in image:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cursor.execute("UPDATE employee SET  image=%s WHERE email='" +
                       session['email'] + "'", [filename])

        conn.commit()

        flash('Profile photo successfully uploaded','success')
        return redirect('/employee_profile')
    return render_template('employee_profile.html')


@app.route('/edit_status/<string:id>', methods=['GET', 'POST'])
def edit_status(id):
    if request.method == 'POST':
        image = request.files.getlist('image[]')
        text = request.form['text']
        date = request.form['date']
        for file in image:

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)

                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))
        cursor.execute(
            'UPDATE status SET image=%s,text=%s,date=%s WHERE id=%s', (filename, text, date, id))
        conn.commit()

        flash('Status updated successfully','success')
        return redirect('/admin_profile')


@app.route('/write_review', methods=['GET', 'POST'])
def write_review():
    cursor.execute('SELECT * FROM user_login WHERE email = "' +
                   session['email']+'" ')
    user = cursor.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        about = request.form['about']
        message = request.form['message']

        cursor.execute("INSERT INTO review(name,email,date,about,message) VALUES(%s,%s,%s,%s,%s)  ",
                       (name, email, date, about, message))
        conn.commit()
        mail.send_message('New review recived' + email,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=name + "\n" + email + "\n" + message
                          )
        ms = Message('Xchange24 Homes', sender='username@gmail.com',
                     recipients=[email])
        ms.body = str('Dear \n' + name + '\n'+'Thanks for your valuable feedback \n' +
                      'Your review was recorded successfully.Our team will contact you soon. ')
        mail.send(ms)
        flash('Thanks for your valuable feedback! Our team will contact you soon.','success')
        return redirect('/user_profile')
    return render_template('write_review.html', user=user)


@app.route('/delete_review/<string:id>', methods=['POST', 'GET'])
def delete_reviews(id):
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()

    cursor.execute('DELETE FROM review WHERE id = {0}'.format(id))
    conn.commit()
    flash('1 review deleted','success')
    return redirect('/admin_profile')


@app.route('/logout')
def logout():

    if 'loggedin' in session:
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)
        flash('Loggedout Successfully','success')
        return redirect('/')


@app.route('/admin_logout')
def admin_logout():

    if 'loggedin' in session:
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)
        flash('Loggedout Successfully','success')
        return redirect('/dashboard_')


@app.route('/update_login_details', methods=['GET', 'POST'])
def update_login_details():
    cursor.execute("SELECT  COUNT(id ) AS no_of_user FROM user_login ")
    user = cursor.fetchone()
    cursor.execute("SELECT  COUNT(id ) AS total_ads FROM ads ")
    total_ads = cursor.fetchone()
    if request.method == 'POST':
        email = request.form['email']
        cursor.execute(
            'UPDATE admin_login SET email = %s WHERE password = "Ashish@143" ', (email))
        return redirect('/dashboard')
    return render_template('dashboard.html', user=user, total_ads=total_ads)



@app.route('/dashboard_', methods=['GET', 'POST'])

def dashboard():
    
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
        admin = cursor.fetchone()
        cursor.execute("SELECT  COUNT(id ) AS no_of_user FROM user_login ")
        user = cursor.fetchone()
        cursor.execute("SELECT  COUNT(id ) AS total_ads FROM ads ")
        total_ads = cursor.fetchone()
        cursor.execute(
            "SELECT  COUNT(id ) AS total_ads_enable FROM ads WHERE status = 'Enable' ")
        total_ads_enable = cursor.fetchone()
        cursor.execute(
            "SELECT  COUNT(id ) AS total_ads_disable FROM ads WHERE status = 'Disable' ")
        total_ads_disable = cursor.fetchone()
        cursor.execute('SELECT * FROM user_login')
        user_detail = cursor.fetchall()
        if request.method == 'POST':
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            if confirm_password != password:
                flash("password doesn't match")
                return render_template("dashboard_.html")
            else:
                cursor.execute('UPDATE admin_login SET password = %s WHERE email = "' +
                            session['email'] + '" ', (password))
                conn.commit()
                flash('Password Changed Successfully','success')
                return redirect('/dashboard_')

        return render_template('dashboard_.html', admin=admin, user=user, total_ads=total_ads, user_detail=user_detail, total_ads_enable=total_ads_enable, total_ads_disable=total_ads_disable)
    else:
        
        return render_template('dashboard_.html')

@app.route('/get_month_data', methods=['GET', 'POST'])
def get_month_data():
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()
    cursor.execute("SELECT  COUNT(id ) AS no_of_user FROM user_login ")
    user = cursor.fetchone()
    cursor.execute("SELECT  COUNT(id ) AS total_ads FROM ads ")
    total_ads = cursor.fetchone()
    cursor.execute(
        "SELECT  COUNT(id ) AS total_ads_enable FROM ads WHERE status = 'Enable' ")
    total_ads_enable = cursor.fetchone()
    cursor.execute(
        "SELECT  COUNT(id ) AS total_ads_disable FROM ads WHERE status = 'Disable' ")
    total_ads_disable = cursor.fetchone()
    cursor.execute('SELECT * FROM user_login')
    user_detail = cursor.fetchall()
    if request.method == 'POST':
        month = request.form['month']

        cursor.execute(
            'SELECT MONTHNAME(date) as current_month, COUNT(id) AS total_product FROM ads WHERE month = %s ', (month))
        month_data = cursor.fetchall()
        conn.commit()
        flash('Details fetched Successfully','success')

    return render_template('dashboard_.html', admin=admin, month_data=month_data, user=user, total_ads=total_ads, user_detail=user_detail, total_ads_enable=total_ads_enable, total_ads_disable=total_ads_disable)


@app.route('/admin_product_', methods=['GET', 'POST'])
def admin_product():
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                    session['email']+'" ')
        admin = cursor.fetchone()
        cursor.execute('''SELECT *,image2,
        substring_index(substring_index(image2, ',', -1), ',', 1) photo 
        FROM ads ''')
        ads = cursor.fetchall()

        cursor.execute('''SELECT *,image2,
        substring_index(substring_index(image2, ',', -1), ',', 1) photo 
        FROM ads WHERE status="Enable" ''')
        enable = cursor.fetchall()

        cursor.execute('''SELECT *,image2,
        substring_index(substring_index(image2, ',', -1), ',', 1) photo 
        FROM ads WHERE status="Disable" ''')
        disable = cursor.fetchall()

        cursor.execute('SELECT DISTINCT city FROM location')
        location = cursor.fetchall()
        cursor.execute('SELECT DISTINCT locality FROM location')
        locality = cursor.fetchall()

        return render_template('admin_product_.html', admin=admin, ads=ads, location=location, locality=locality, enable=enable, disable=disable)
    else:
        flash('Login to access this page!','error')
        return render_template('dashboard_.html')

@app.route('/employee_product_', methods=['GET', 'POST'])
def employee_product_():
    cursor.execute('SELECT * FROM employee WHERE email = "' +
                   session['email']+'" ')
    employee = cursor.fetchone()
    cursor.execute('''SELECT *,image2,
    substring_index(substring_index(image2, ',', -1), ',', 1) photo 
    FROM ads ''')
    ads = cursor.fetchall()

    cursor.execute('''SELECT *,image2,
    substring_index(substring_index(image2, ',', -1), ',', 1) photo 
    FROM ads WHERE status="Enable" ''')
    enable = cursor.fetchall()

    cursor.execute('''SELECT *,image2,
    substring_index(substring_index(image2, ',', -1), ',', 1) photo 
    FROM ads WHERE status="Disable" ''')
    disable = cursor.fetchall()

    cursor.execute('SELECT DISTINCT city FROM location')
    location = cursor.fetchall()
    cursor.execute('SELECT DISTINCT locality FROM location')
    locality = cursor.fetchall()
    if request.method == 'POST':
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if confirm_password != password:
            flash("password doesn't match")
            return render_template("dashboard_.html")
        else:
            cursor.execute('UPDATE admin_login SET password = %s WHERE email = "' +
                           session['email'] + '" ', (password))
            conn.commit()
            flash('Password Changed Successfully','success')
            return redirect('/employee_profile')
    return render_template('employee_product_.html', ads=ads, employee=employee, enable=enable, disable=disable, location=location, locality=locality)


@app.route('/admin_product_details_/<string:id>', methods=['GET', 'POST'])
def admin_product_details(id):
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()

    # cursor.execute('SELECT *, images.photo FROM ads INNER JOIN images ON ads.uniid=images.uni WHERE id=%s ',(id))

    # cursor.execute('SELECT * FROM ads WHERE id= %s', (id))
    cursor.execute("""SELECT *, image2,
  substring_index(substring_index(image2, ',', -1), ',', 1) photo,
    substring_index(substring_index(image2, ',', -2), ',', 1) photo2,
  substring_index(substring_index(image2, ',', -3), ',', 1) photo3,
  substring_index(substring_index(image2, ',', -4), ',', 1) photo4,
  substring_index(substring_index(image2, ',', -5), ',', 1) photo5,
  substring_index(substring_index(image2, ',', -6), ',', 1) photo6,
  substring_index(substring_index(image2, ',', -7), ',', 1) photo7,
  substring_index(substring_index(image2, ',', -8), ',', 1) photo8,
  substring_index(substring_index(image2, ',', -9), ',', 1) photo9,
  substring_index(substring_index(image2, ',', -10), ',', 1) photo10

  
FROM ads WHERE id = %s """, (id))
    # cursor.execute("select rent,title,locality, image2, substring_index(image2, ',', 1) photo1,substring_index(image2, ',', -1) photo2, substring_index(image2, ',', -2) photo3 from ads where id=%s;",(id))
    ads = cursor.fetchall()

    return render_template('admin_product_details_.html', admin=admin, ads=ads)


@app.route('/employee_product_details_/<string:id>', methods=['GET', 'POST'])
def employee_product_details_(id):
    cursor.execute('SELECT * FROM employee WHERE email = "' +
                   session['email']+'" ')
    employee = cursor.fetchone()

    # cursor.execute('SELECT *, images.photo FROM ads INNER JOIN images ON ads.uniid=images.uni WHERE id=%s ',(id))

    # cursor.execute('SELECT * FROM ads WHERE id= %s', (id))
    cursor.execute("""SELECT *, image2,
  substring_index(substring_index(image2, ',', -1), ',', 1) photo,
    substring_index(substring_index(image2, ',', -2), ',', 1) photo2,
  substring_index(substring_index(image2, ',', -3), ',', 1) photo3,
  substring_index(substring_index(image2, ',', -4), ',', 1) photo4,
  substring_index(substring_index(image2, ',', -5), ',', 1) photo5,
  substring_index(substring_index(image2, ',', -6), ',', 1) photo6,
  substring_index(substring_index(image2, ',', -7), ',', 1) photo7,
  substring_index(substring_index(image2, ',', -8), ',', 1) photo8,
  substring_index(substring_index(image2, ',', -9), ',', 1) photo9,
  substring_index(substring_index(image2, ',', -10), ',', 1) photo10

  
FROM ads WHERE id = %s """, (id))
    # cursor.execute("select rent,title,locality, image2, substring_index(image2, ',', 1) photo1,substring_index(image2, ',', -1) photo2, substring_index(image2, ',', -2) photo3 from ads where id=%s;",(id))
    ads = cursor.fetchall()
    return render_template('employee_product_details_.html', ads=ads, employee=employee)


@app.route('/employee_', methods=['GET', 'POST'])
def employee():
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                    session['email']+'" ')
        admin = cursor.fetchone()
        cursor.execute('SELECT * FROM employee')
        employee = cursor.fetchall()
        cursor.execute(
            ' SELECT COUNT(id) AS total_product FROM ads WHERE listed_by = (SELECT name FROM employee WHERE id = %s) ', (id))
        total = cursor.fetchone()

        if request.method == 'POST':
            name = request.form['name']
            mobile = request.form['mobile']
            email = request.form['email']
            password = request.form['password']
            image = request.files.getlist('image[]')

            for file in image:

                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)

                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
            cursor.execute('INSERT INTO employee(name,mobile,email,password,image) VALUES(%s,%s,%s,%s,%s)',
                        (name, mobile, email, password, filename))
            conn.commit()
            flash('Employee added successfully !','success')
            return redirect('/employee_')
        return render_template('employee_.html', admin=admin, employee=employee, total=total)
    else:
        flash('Login to access this page','error')
        return render_template('dashboard_.html')
@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()
    cursor.execute('SELECT * FROM employee')
    employee = cursor.fetchall()
    if request.method == 'POST':
        listed_by = request.form['listed_by']
        month = request.form['month']
        cursor.execute(
            'SELECT COUNT(id) AS total_product FROM ads WHERE listed_by = %s ', (listed_by))
        total_data = cursor.fetchall()
        cursor.execute(
            'SELECT COUNT(id) AS total_product, MONTHNAME(date) as current_month FROM ads WHERE listed_by = %s AND month = %s ', (listed_by, month))
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM employee WHERE name = %s ', (listed_by))
        emp_report = cursor.fetchall()
        conn.commit()
        flash('Details fetched successfully','success')

    return render_template('employee_.html', admin=admin, data=data, employee=employee, emp_report=emp_report, total_data=total_data)


@app.route('/edit_employee/<string:id>', methods=['GET', 'POST'])
def update(id):
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        password = request.form['password']

        cursor.execute(
            "UPDATE employee SET name = %s, mobile = %s, email = %s, password = %s WHERE id= %s", (name, mobile, email, password, id))
        conn.commit()
        flash('Employee details Updated Successfully','success')
        return redirect('/employee_')
    return render_template('employee_.html', admin=admin)


@app.route('/delete_employee/<string:id>', methods=['POST', 'GET'])
def delete_doctors(id):
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()

    cursor.execute('DELETE FROM employee WHERE id = {0}'.format(id))
    conn.commit()
    flash('Employee deleted.','success')
    return redirect('/employee_')


@app.route('/add_item_', methods=['GET', 'POST'])
def add_item_():
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()
    cursor.execute('SELECT DISTINCT city FROM location')
    location = cursor.fetchall()
    cursor.execute('SELECT DISTINCT locality FROM location')
    locality = cursor.fetchall()

    if request.method == 'POST':
        uniid = request.form['uniid']
        title = request.form['title']
        house_type = request.form['house_type']
        bhk_type = request.form['bhk_type']
        bathroom = request.form['bathroom']
        car = request.form['car']
        tenant = request.form['tenant']
        bachelor = request.form['bachelor']
        total_floor = request.form['total_floor']
        floor_no = request.form['floor_no']
        facing = request.form['facing']
        furnishing = request.form['furnishing']
        area = request.form['area']
        city = request.form['city']
        locality = request.form['locality']
        pg = request.form['pg']
        sharing = request.form['sharing']
        owner_name = request.form['owner_name']
        owner_mobile = request.form['owner_mobile']
        owner_whatsapp = request.form['owner_whatsapp']
        rent = request.form['rent']
        listed_by = request.form['listed_by']
        date = request.form['date']
        month = request.form['month']
        year = request.form['year']
        time = request.form['time']
        description = request.form['description']
        status = request.form['status']

        cursor.execute("INSERT INTO ads(uniid,title,house_type,bhk_type,bathroom,car,tenant,bachelor,total_floor,floor_no,facing,furnishing,area,city,locality,pg,sharing,owner_name,owner_mobile,owner_whatsapp,rent,listed_by,date,month,year,time,description,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (uniid, title, house_type, bhk_type, bathroom, car, tenant, bachelor, total_floor, floor_no, facing, furnishing, area, city, locality, pg, sharing, owner_name, owner_mobile, owner_whatsapp, rent, listed_by, date, month, year, time, description, status))

        if request.method == 'POST':
            uni = request.form['uniid']
            photo = request.files.getlist('image[]')
            # image2 = request.form['image2']
            for file in photo:

                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)

                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
                    cursor.execute(
                        'INSERT INTO images(uni,photo) VALUES(%s,%s) ', (uni, filename))
                    cursor.execute(
                        'UPDATE ads SET image2 = (SELECT DISTINCT GROUP_CONCAT(photo) FROM images WHERE uni=%s) WHERE uniid = %s ', (uni, uniid))
                    # cursor.execute(" SELECT *FROM (SELECT uni,photo FROM images) AS t, PIVOT (MAX(photo) FOR attribute IN([photo1], [photo2],[photo3],[photo4],[photo5])) AS p; ")
                    # data = cursor.fetchall()
        conn.commit()
        flash('Product Added Successfully !','success')
        return redirect('/admin_product_')

    return render_template('admin_product_.html', admin=admin, location=location, locality=locality)


@app.route('/product_status_/<string:id>', methods=['POST', 'GET'])
def product_status_(id):
    error = 'None'

    if request.method == 'POST':
        status = request.form['status']
        reason = request.form['reason']

        cursor.execute(
            'UPDATE ads SET status=%s,reason=%s WHERE id = %s', (status, reason, id))
        conn.commit()
        flash('Successfully Updated !','success')
        return redirect('/admin_product_')


@app.route('/employee_product_status_/<string:id>', methods=['POST', 'GET'])
def employee_product_status_(id):

    if request.method == 'POST':
        status = request.form['status']
        reason = request.form['reason']
        disable_by = request.form['disable_by']

        cursor.execute(
            'UPDATE ads SET status=%s,reason=%s,disable_by=%s WHERE id = %s', (status, reason,disable_by, id))
        conn.commit()
        flash('Successfully Updated !','success')
        return redirect('/employee_product_')


@app.route('/delete_product/<string:id>', methods=['POST', 'GET'])
def delete_product(id):

    cursor.execute('DELETE FROM ads WHERE id = {0}'.format(id))
    conn.commit()
    flash('1 product deleted.','success')
    return redirect('/admin_product_')


@app.route('/edit_product/<string:id>', methods=['GET', 'POST'])
def edit_product(id):
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()
    cursor.execute('SELECT * FROM ads WHERE id = %s ', (id))
    product = cursor.fetchall()

    cursor.execute('SELECT DISTINCT city FROM location')
    location = cursor.fetchall()
    cursor.execute('SELECT DISTINCT locality FROM location')
    locality = cursor.fetchall()

    if request.method == 'POST':

        uniid = request.form['uniid']
        title = request.form['title']
        house_type = request.form['house_type']
        bhk_type = request.form['bhk_type']
        bathroom = request.form['bathroom']
        car = request.form['car']
        tenant = request.form['tenant']
        bachelor = request.form['bachelor']
        total_floor = request.form['total_floor']
        floor_no = request.form['floor_no']
        facing = request.form['facing']
        furnishing = request.form['furnishing']
        area = request.form['area']
        city = request.form['city']
        locality = request.form['locality']
        pg = request.form['pg']
        sharing = request.form['sharing']
        owner_name = request.form['owner_name']
        owner_mobile = request.form['owner_mobile']
        owner_whatsapp = request.form['owner_whatsapp']
        rent = request.form['rent']
        listed_by = request.form['listed_by']
        date = request.form['date']
        month = request.form['month']
        year = request.form['year']
        time = request.form['time']
        description = request.form['description']
        status = request.form['status']

        cursor.execute("INSERT INTO ads(uniid,title,house_type,bhk_type,bathroom,car,tenant,bachelor,total_floor,floor_no,facing,furnishing,area,city,locality,pg,sharing,owner_name,owner_mobile,owner_whatsapp,rent,listed_by,date,month,year,time,description,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (uniid, title, house_type, bhk_type, bathroom, car, tenant, bachelor, total_floor, floor_no, facing, furnishing, area, city, locality, pg, sharing, owner_name, owner_mobile, owner_whatsapp, rent, listed_by, date, month, year, time, description, status))

        if request.method == 'POST':
            uni = request.form['uniid']
            photo = request.files.getlist('image[]')
            # image2 = request.form['image2']
            for file in photo:

                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)

                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
                    cursor.execute(
                        'INSERT INTO images(uni,photo) VALUES(%s,%s) ', (uni, filename))
                    cursor.execute(
                        'UPDATE ads SET image2 = (SELECT DISTINCT GROUP_CONCAT(photo) FROM images WHERE uni=%s) WHERE uniid = %s ', (uni, uniid))
                    # cursor.execute(" SELECT *FROM (SELECT uni,photo FROM images) AS t, PIVOT (MAX(photo) FOR attribute IN([photo1], [photo2],[photo3],[photo4],[photo5])) AS p; ")
                    # data = cursor.fetchall()
        conn.commit()
        flash('Product Added Successfully !','success')
        return redirect('/employee_product_')

    return render_template('employee_product_.html', location=location, locality=locality)


@app.route('/employee_edit_product_/<string:id>', methods=['GET', 'POST'])
def employee_edit_product_(id):
    cursor.execute('SELECT * FROM ads WHERE id = %s ', (id))
    product = cursor.fetchall()

    cursor.execute('SELECT DISTINCT city FROM location')
    location = cursor.fetchall()
    cursor.execute('SELECT DISTINCT locality FROM location')
    locality = cursor.fetchall()

    if request.method == 'POST':

        title = request.form['title']
        house_type = request.form['house_type']
        bhk_type = request.form['bhk_type']
        bathroom = request.form['bathroom']
        car = request.form['car']
        tenant = request.form['tenant']
        bachelor = request.form['bachelor']
        total_floor = request.form['total_floor']
        floor_no = request.form['floor_no']
        facing = request.form['facing']
        furnishing = request.form['furnishing']
        area = request.form['area']
        city = request.form['city']
        locality = request.form['locality']
        pg = request.form['pg']
        sharing = request.form['sharing']
        owner_name = request.form['owner_name']
        owner_mobile = request.form['owner_mobile']
        owner_whatsapp = request.form['owner_whatsapp']
        rent = request.form['rent']
        listed_by = request.form['listed_by']
        description = request.form['description']

        cursor.execute("UPDATE ads SET title=%s,house_type=%s,bhk_type=%s,bathroom=%s,car=%s,tenant=%s,bachelor=%s,total_floor=%s,floor_no=%s,facing=%s,furnishing=%s,area=%s,city=%s,locality=%s,pg=%s,sharing=%s,owner_name=%s,owner_mobile=%s,owner_whatsapp=%s,rent=%s,listed_by=%s,description=%s WHERE id = %s ",
                       (title, house_type, bhk_type, bathroom, car, tenant, bachelor, total_floor, floor_no, facing, furnishing, area, city, locality, pg, sharing, owner_name, owner_mobile, owner_whatsapp, rent, listed_by, description, id))

        conn.commit()
        flash('Updated Successfully !','success')
        return redirect('/employee_product_')

    return render_template('employee_product_.html', product=product, location=location, locality=locality)


# for STATUS

@app.route('/add_status', methods=['GET', 'POST'])
def add_status():
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()
    msg = ''
    if request.method == 'POST':
        image = request.files.getlist('image[]')
        text = request.form['text']
        date = request.form['date']
        for file in image:

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)

                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))
        cursor.execute(
            'INSERT INTO status(image,text,date) VALUES(%s,%s,%s)', (filename, text, date))
        conn.commit()

        flash('Status added successfully','success')

        return redirect('/admin_product_')

    return render_template('admin_product.html', admin=admin, msg=msg)


@app.route('/employee_add_status', methods=['GET', 'POST'])
def employee_add_status():

    if request.method == 'POST':
        image = request.files.getlist('image[]')
        text = request.form['text']
        date = request.form['date']
        for file in image:

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)

                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))
        cursor.execute(
            'INSERT INTO status(image,text,date) VALUES(%s,%s,%s)', (filename, text, date))
        conn.commit()
        flash('Status added successfully','success')
        return redirect('/employee_product_')

    return render_template('employee_product_.html')


@app.route('/add_location', methods=['GET', 'POST'])
def add_location():
    cursor.execute('SELECT * FROM admin_login WHERE email = "' +
                   session['email']+'" ')
    admin = cursor.fetchone()
    if request.method == 'POST':
        city = request.form['city']
        locality = request.form['locality']
        cursor.execute(
            'INSERT INTO location(city,locality) VALUES(%s,%s)', (city, locality))
        conn.commit()
        flash('Status added successfully','success')
        return redirect('/admin_product_')

    return render_template('admin_product_.html', admin=admin)


@app.route('/employee_add_location', methods=['GET', 'POST'])
def employee_add_location():

    if request.method == 'POST':
        city = request.form['city']
        locality = request.form['locality']
        cursor.execute(
            'INSERT INTO location(city,locality) VALUES(%s,%s)', (city, locality))
        conn.commit()
        flash('Location added successfully','success')
        return redirect('/employee_product_')

    return render_template('employee_product_.html')


app.run(debug=True, port=5088)
