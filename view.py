from rami import app, db
from flask import url_for, render_template, request
from forms import DataForm, newForm
from model import Data

forms = [] # Array that holds all the forms ever created


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html', forms=forms) #Renders all forms on /index.html


'''
This method will create a new form and add it the forms array
Then it will return refresh the screen.
'''
@app.route('/addform', methods=['GET','POST'])
def addform():
    with app.app_context(): #Needed since forms is a global variable
        if request.method == "POST": 
            forms.append(newForm())

        return render_template('index.html', forms=forms)
