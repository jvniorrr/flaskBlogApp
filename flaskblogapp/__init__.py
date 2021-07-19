
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = '435008ad6a1ac234c80c94824d33b091'
# using 3 back slashes gives a local db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# create a DB instance
db = SQLAlchemy(app)


from flaskblogapp import routes