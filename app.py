from flask import Flask
from flask import send_from_directory
from flask import render_template
import csv
app = Flask(__name__)

@app.route('/films/list')
def list_films(): 
    try:
        return send_from_directory("C:\\Work\\Exercises\\workshop_part3\\html", filename="films.html")
    except FileNotFoundError:
        print("Helo!!")


@app.route('/films/table')
def table_films(): 
    try:
        with open("C:\\Work\\Exercises\\workshop_part3\\film_review.txt", "r") as csvfile:
            
            film_reader = csv.DictReader(csvfile, delimiter=',')
            film_list = []
            for row in film_reader:
                film_list.append({'Name': row['Name'], 'Stars': row['Stars']})
            return render_template('films_table_template.html', title='Film Table', films=film_list)
    except FileNotFoundError:
        print("Help!!")