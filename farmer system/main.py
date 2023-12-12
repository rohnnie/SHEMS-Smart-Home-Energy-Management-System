from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify  
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from sqlalchemy import text,create_engine
import sqlalchemy



# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='rohanutsav'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@127.0.0.1/shems'
db=SQLAlchemy(app)
engine = create_engine("mysql://root:@127.0.0.1/shems")
conn=engine.connect()

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

class Product(db.Model):
    fid=db.Column(db.Integer,primary_key=True)
    type1 = db.Column(db.String(10), nullable=False)
    Product_Models=db.Column(db.String(100))
    
class Typee(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))


class Adddevice(db.Model):
    pid=db.Column(db.Integer,primary_key=True)
    bid=db.Column(db.String(50),db.ForeignKey('register.rid'), nullable=False)
    Location_unit_number=db.Column(db.Integer)
    Type=db.Column(db.String(50))
    Product=db.Column(db.String(50))
    Color=db.Column(db.String(300))
    price=db.Column(db.Integer)
    energys=db.relationship('EnergyData', backref='adddevice')

class EnergyData(db.Model):
    eid=db.Column(db.Integer,primary_key=True)
    pid=db.Column(db.Integer,db.ForeignKey('adddevice.pid'), nullable=False)
    timeinterval=db.Column(db.DateTime)
    eventlabel=db.Column(db.String(50))
    value=db.Column(db.Integer)

class ConsumptionPrices(db.Model):
    cid=db.Column(db.Integer,primary_key=True)
    Zip_Code=db.Column(db.Integer)
    Timenoted=db.Column(db.DateTime)
    Price=db.Column(db.Integer)

class Trig(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fid=db.Column(db.String(100))
    action=db.Column(db.String(100))
    timestamp=db.Column(db.String(100))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))
    registers=db.relationship('Register', backref='user')


class Register(db.Model):
    uid=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rid=db.Column(db.Integer,primary_key=True)
    Unit_Number=db.Column(db.String(50))
    City=db.Column(db.String(50))
    State=db.Column(db.Integer)
    Zip_Code=db.Column(db.String(50))
    Area=db.Column(db.String(50))
    Bedrooms=db.Column(db.String(50))
    Occupants=db.Column(db.String(50))
    adds=db.relationship('Adddevice', backref='register')



@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/LocationDetails')
@login_required
def LocationDetails():
    query=conn.execute(text(f"SELECT * FROM register where uid={current_user.get_id()}"))
   # query=Register.query.filter_by(uid=current_user.get_id()).all()
    return render_template('LocationDetails.html',query=query)

@app.route('/Devices')
def Devices():
    m=conn.execute(text(f"SELECT * FROM register where uid={current_user.get_id()}"))
    res=[row[0] for row in m]
    res1=[]
    for x in res:
        query=conn.execute(text(f"SELECT * FROM Adddevice where bid={x}"))
        for y in query:
            res1.append(y)
    return render_template('Devices.html',query=res1)

@app.route('/adddevice',methods=['POST','GET'])
@login_required
def adddevice():
    type1=conn.execute(text(f"SELECT * FROM Typee"))
    num=conn.execute(text(f"SELECT * FROM Register"))
    if request.method=="POST":
        Location_unit_number=request.form.get('Location_unit_number')
        Type=request.form.get('Type')
        Product=request.form.get('Product')
        Color=request.form.get('Color')
        price=request.form.get('price')
        l1=conn.execute(text(f"Select * from Register where Unit_Number={Location_unit_number}"))
        res=[row[0] for row in l1][0]
        #l=Register.query.filter_by(Unit_Number=Location_unit_number).first()
        print(res,Type,Product,Color,price)
        products=conn.execute(text(f"INSERT INTO Adddevice(bid,Location_unit_number,Type,Product,Color,price) VALUES ({res},{Location_unit_number},\"{Type}\", {Product}, \"{Color}\",{price})"))
        #products=Adddevice(bid=l.rid,Location_unit_number=Location_unit_number,Type=Type,Product=Product,Color=Color,price=price)
        #db.session.add(products)
        conn.execute(text(f"COMMIT"))
        #db.session.commit()
        flash("Product Added","info")
        return redirect('/Devices')
    return render_template('adddevice.html',type1=type1, num=num)

@app.route('/prod/<type1>')
def city(type1):
    #model=conn.execute(text(f"SELECT * FROM Product where type1={type1}"))
    model = Product.query.filter_by(type1=type1).all()
    print(model)
    modelarray = []
    for a in model:
        mObj = {}
        mObj['fid'] = a.fid
        mObj['Product_Models'] = a.Product_Models
        modelarray.append(mObj)

    return jsonify({'Models' : modelarray})

@app.route('/triggers')
@login_required
def triggers():
    # query=db.engine.execute(f"SELECT * FROM `trig`") 
    query=conn.execute(text(f"SELECT * FROM Trig"))
    return render_template('triggers.html',query=query)

@app.route('/gettype',methods=['POST','GET'])
@login_required
def gettype():
    if request.method=="POST":
        gettype=request.form.get('typee')
        query=Typee.query.filter_by( name = gettype ).first()
        if query:
            flash("Device Type Already Exist","warning")
            return redirect('/gettype')
        dep=Typee(name=gettype)
        db.session.add(dep)
        db.session.commit()
        flash("Device Type Added","success")
    return render_template('gettype.html')



@app.route("/delete/<string:rid>",methods=['POST','GET'])
@login_required
def delete(rid):
    # db.engine.execute(f"DELETE FROM `register` WHERE `register`.`rid`={rid}")
    post=Register.query.filter_by(rid=rid).first()
    db.session.delete(post)
    db.session.commit()
    flash("Slot Deleted Successful","warning")
    return redirect('/LocationDetails')


@app.route("/edit/<string:rid>",methods=['POST','GET'])
@login_required
def edit(rid):
    # product=db.engine.execute("SELECT * FROM `product`") 
    if request.method=="POST":
        Unit_Number=request.form.get('Unit_Number')
        City=request.form.get('City')
        State=request.form.get('State')
        Zip_Code=request.form.get('Zip_Code')
        Area=request.form.get('Area')
        Bedrooms=request.form.get('Bedrooms')
        Occupants=request.form.get('Occupants')     
        # query=db.engine.execute(f"UPDATE `register` SET `Unit_Number`='{Unit_Number}',`City`='{City}',`State`='{State}',`Zip_Code`='{Zip_Code}',`Area`='{Area}',`Occupants`='{Occupants}',`Bedrooms`='{Bedrooms}'")
        post=Register.query.filter_by(rid=rid).first()
        print(post.Unit_Number)
        post.uid={current_user.get_id}
        post.Unit_Number=Unit_Number
        post.City=City
        post.State=State
        post.Zip_Code=Zip_Code
        post.Area=Area
        post.Bedrooms=Bedrooms
        post.Occupants=Occupants
        db.session.commit()
        flash("Slot is Updates","success")
        return redirect('/LocationDetails')
    posts=Register.query.filter_by(rid=rid).first()
    product=Product.query.all()
    return render_template('edit.html',posts=posts,product=product)


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        print(username,email,password)
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)

        # new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")

        # this is method 2 to save data in db
        newuser=User(username=username,email=email,password=encpassword)
        db.session.add(newuser)
        db.session.commit()
        flash("Signup Succes Please Login","success")
        return render_template('login.html')

          

    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","warning")
            return render_template('login.html')    

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))



@app.route('/register',methods=['POST','GET'])
@login_required
def register():
    product=Product.query.all()
    if request.method=="POST":
        Unit_Number=request.form.get('Unit_Number')
        City=request.form.get('City')
        State=request.form.get('State')
        Zip_Code=request.form.get('Zip_Code')
        Area=request.form.get('Area')
        Bedrooms=request.form.get('Bedrooms')
        Occupants=request.form.get('Occupants')    
        uid=current_user.get_id()
        query=Register(uid=uid,Unit_Number=Unit_Number,City=City,State=State,Zip_Code=Zip_Code,Area=Area,Bedrooms=Bedrooms,Occupants=Occupants)
        db.session.add(query)
        db.session.commit()
        # query=db.engine.execute(f"INSERT INTO `register` (`Unit_Number`,`City`,`State`,`Zip_Code`,`Bedrooms`,`Area`,`Occupants`) VALUES ('{Unit_Number}','{City}','{State}','{Zip_Code}','{Bedrooms}','{Area}','{Occupants}')")
        # flash("Your Record Has Been Saved","success")
        return redirect('/LocationDetails')
    return render_template('Location.html',product=product)

@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'

@app.route('/views',methods=['POST','GET'])
@login_required
def views():
    return render_template('views.html')

@app.route("/enery_consumption_per_device")
@login_required
def enery_consumption_per_device():
    return render_template('enery_consumption_per_device.html')

@app.route("/total_enerygy_consumption")
@login_required
def total_enerygy_consumption():
    return render_template('enery_consumption_per_device.html')



app.run(debug=True)    
