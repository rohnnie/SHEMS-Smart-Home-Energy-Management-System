from flask import Flask,render_template,request,session,redirect,url_for,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user


# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='harshithbhaskar'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@127.0.0.1/farmers'
db=SQLAlchemy(app)

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

class Farming(db.Model):
    fid=db.Column(db.Integer,primary_key=True)
    t_id = db.Column(db.Integer, db.ForeignKey('typee.tid'), nullable=False)
    Product_Models=db.Column(db.String(100))
    
class Typee(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    Type=db.relationship('Farming')


class Addagroproducts(db.Model):
    Location_unit_number=db.Column(db.String(50))
    Type=db.Column(db.String(50))
    pid=db.Column(db.Integer,primary_key=True)
    Product=db.Column(db.String(50))
    Color=db.Column(db.String(300))
    price=db.Column(db.Integer)



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

class Register(db.Model):
    rid=db.Column(db.Integer,primary_key=True)
    Unit_Number=db.Column(db.String(50))
    City=db.Column(db.String(50))
    State=db.Column(db.Integer)
    Zip_Code=db.Column(db.String(50))
    Area=db.Column(db.String(50))
    Bedrooms=db.Column(db.String(50))
    Occupants=db.Column(db.String(50))


@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/farmerdetails')
@login_required
def farmerdetails():
    # query=db.engine.execute(f"SELECT * FROM `register`") 
    query=Register.query.all()
    return render_template('farmerdetails.html',query=query)

@app.route('/agroproducts')
def agroproducts():
    # query=db.engine.execute(f"SELECT * FROM `addagroproducts`") 
    query=Addagroproducts.query.all()
    return render_template('agroproducts.html',query=query)

@app.route('/addagroproduct',methods=['POST','GET'])
@login_required
def addagroproduct():
    type1=Typee.query.all()
    if request.method=="POST":
        Location_unit_number=request.form.get('Location_unit_number')
        Type=request.form.get('Type')
        Product=request.form.get('Product')
        Color=request.form.get('Color')
        price=request.form.get('price')
        products=Addagroproducts(Location_unit_number=Location_unit_number,Type=Type,Product=Product,Color=Color,price=price)
        db.session.add(products)
        db.session.commit()
        flash("Product Added","info")
        return redirect('/agroproducts', type1=type1)
   
    return render_template('addagroproducts.html')

@app.route('/triggers')
@login_required
def triggers():
    # query=db.engine.execute(f"SELECT * FROM `trig`") 
    query=Trig.query.all()
    return render_template('triggers.html',query=query)

@app.route('/gettype',methods=['POST','GET'])
@login_required
def gettype():
    if request.method=="POST":
        gettype=request.form.get('typee')
        query=Typee.query.filter_by( name = gettype ).first()
        if query:
            flash("Farming Type Already Exist","warning")
            return redirect('/gettype')
        dep=Typee(name=gettype)
        db.session.add(dep)
        db.session.commit()
        flash("Farming Addes","success")
    return render_template('gettype.html')



@app.route("/delete/<string:rid>",methods=['POST','GET'])
@login_required
def delete(rid):
    # db.engine.execute(f"DELETE FROM `register` WHERE `register`.`rid`={rid}")
    post=Register.query.filter_by(rid=rid).first()
    db.session.delete(post)
    db.session.commit()
    flash("Slot Deleted Successful","warning")
    return redirect('/farmerdetails')


@app.route("/edit/<string:rid>",methods=['POST','GET'])
@login_required
def edit(rid):
    # farming=db.engine.execute("SELECT * FROM `farming`") 
    if request.method=="POST":
        Unit_Number=request.form.get('Unit_Number')
        City=request.form.get('City')
        State=request.form.get('State')
        Zip_Code=request.form.get('Zip_Code')
        Area=request.form.get('Area')
        Bedrooms=request.form.get('Bedrooms')
        Occupants=request.form.get('Occupants')     
        # query=db.engine.execute(f"UPDATE `register` SET `farmername`='{farmername}',`adharnumber`='{adharnumber}',`age`='{age}',`gender`='{gender}',`phonenumber`='{phonenumber}',`address`='{address}',`farming`='{farmingtype}'")
        post=Register.query.filter_by(rid=rid).first()
        print(post.Unit_Number)
        post.Unit_Number=Unit_Number
        post.City=City
        post.State=State
        post.Zip_Code=Zip_Code
        post.Area=Area
        post.Bedrooms=Bedrooms
        post.Occupants=Occupants
        db.session.commit()
        flash("Slot is Updates","success")
        return redirect('/farmerdetails')
    posts=Register.query.filter_by(rid=rid).first()
    farming=Farming.query.all()
    return render_template('edit.html',posts=posts,farming=farming)


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
    farming=Farming.query.all()
    if request.method=="POST":
        Unit_Number=request.form.get('Unit_Number')
        City=request.form.get('City')
        State=request.form.get('State')
        Zip_Code=request.form.get('Zip_Code')
        Area=request.form.get('Area')
        Bedrooms=request.form.get('Bedrooms')
        Occupants=request.form.get('Occupants')     
        query=Register(Unit_Number=Unit_Number,City=City,State=State,Zip_Code=Zip_Code,Area=Area,Bedrooms=Bedrooms,Occupants=Occupants)
        db.session.add(query)
        db.session.commit()
        # query=db.engine.execute(f"INSERT INTO `register` (`farmername`,`adharnumber`,`age`,`gender`,`phonenumber`,`address`,`farming`) VALUES ('{farmername}','{adharnumber}','{age}','{gender}','{phonenumber}','{address}','{farmingtype}')")
        # flash("Your Record Has Been Saved","success")
        return redirect('/farmerdetails')
    return render_template('farmer.html',farming=farming)

@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'


app.run(debug=True)    
