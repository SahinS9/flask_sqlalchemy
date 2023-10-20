from flask import Flask
from flask import render_template
from views import *
from models import User, Task

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
app.app_context().push()

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)
