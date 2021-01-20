from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/login')
def show_login_form():
    return render_template('login_form.template.html')

# if you recieve a POST request for the '/login' url
# use the function below


@app.route('/login', methods=["POST"])
def process_login_form():
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print("data recieved")
    return "Welcome, " + username


@app.route('/calculate')
def show_calculator_form():
    return render_template('calculator.template.html')


@app.route('/calculate', methods=["POST"])
def process_calculator_form():
    print(request.form)
    n1 = int(request.form.get('number1'))
    n2 = int(request.form.get('number2'))
    return str(n1 + n2)


@app.route('/bmi')
def show_bmi_form():
    return render_template('bmi.template.html')


@app.route('/bmi', methods=["POST"])
def process_bmi_form():
    print(request.form)
    weight = float(request.form.get('weight'))
    height = float(request.form.get('height'))
    bmi = round(weight / height**2, 2)
    return render_template('bmi_results.template.html', bmi=bmi)


@app.route('/survey')
def show_survey_form():
    return render_template('survey.template.html')

@app.route('/survey', methods=["POST"])
def process_survey_form():
    print(request.form)
    fullname = request.form.get('fullname')
    gender = request.form.get('gender')
    activities = request.form.getlist('activities')
    # check if the user has selected any activities
    if not activities:
        print("The user didn't select any activities")
    print(activities)
    return render_template('survey_results.template.html', fullname=fullname,
                           gender=gender, activities=activities)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
