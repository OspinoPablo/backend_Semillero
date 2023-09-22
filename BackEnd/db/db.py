from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/AppSemillero' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False