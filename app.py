#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set a secret key to use when validating form data
app.config["SECRET_KEY"] = "your secret key"

#Function to request student data from the api
#Input: url
#Output: JSON student data
def get_student_data(url):
    #make a request
    response = requests.get(url)

    #convert format to json
    response_json = response.json()

    return response_json

def get_unique_majors():
    url = "http://127.0.0.1:5000/api/students/all"
    
    student_list = get_student_data(url)

    unique_majors = []

    for student in student_list:
        if student["major"] not in unique_majors:
            unique_majors.append(student["major"])
    unique_majors.sort()
    return unique_majors

#create a route for the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #get the student data
    #make a request to the student data api url
    url = "http://127.0.0.1:5000/api/students/all"

    student_data = get_student_data(url)

    #send the student data to the index.html page
    return render_template('index.html', student_data=student_data)

@app.route('/majors', methods=['GET'])
def majors():
    major_list = get_unique_majors()

    return render_template('majors.html', major_list=major_list)

@app.route('/majors', methods=['POST'])
def majors_post():

    major = request.form.get('major')

    if not major:
        flash("You must select a Major")
    else:
        url = "http://127.0.0.1:5000/api/students/all"
        student_list = get_student_data(url)
        result_list = []

        for students in student_list:
            if students["major"] == major:
                result_list.append(students)




    major_list = get_unique_majors()
    return render_template('majors.html', major_list=major_list, result_list=result_list)

app.run(port=5005)
