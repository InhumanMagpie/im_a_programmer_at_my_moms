from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/tms_sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
