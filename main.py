from flask import Flask, render_template, request, flash
from pymongo import MongoClient

app = Flask(__name__)

app.secret_key = 'secret_key_for_session'

client = MongoClient("mongodb://localhost:27017/")
db = client["Form"]
form_collection = db["details"]

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        address = request.form['address']
        github = request.form['github']
        cv = request.form['cv']
        image = request.form['image']

        details = {
            "name": name,
            "email": email,
            "phone": phone,
            "gender": gender,
            "address": address,
            "github": github,
            "cv": cv,
            "image": image
        }
        form_collection.insert_one(details)
        flash("Thanks for connecting with me.")
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)