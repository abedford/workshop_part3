from flask import Flask, render_template, request
from flask import send_from_directory
from flask import redirect
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
    stars_requested = request.values.get("stars", "")
    try:
        with open("C:\\Work\\Exercises\\workshop_part3\\film_review.txt", "r") as csvfile:
            
            film_reader = csv.DictReader(csvfile, delimiter=',')
            film_list = []
            for row in film_reader:
                film_rating = row['Stars']
                if (film_rating >= stars_requested):
                    film_list.append({'Name': row['Name'], 'Stars': film_rating})
            return render_template('films_table_template.html', title='Film Table', films=film_list)
    except FileNotFoundError:
        print("Help!!")

@app.route('/films/submit', methods = ['POST', 'GET'])
def submit_films():
    if request.method == 'POST':
        form_data = request.form
        name = form_data["Name"]
        stars = form_data["Star"]
        add_new_film(name, stars)

        feedback = f"Added film {name}, {stars}"
        return render_template('new_film.html', feedback=feedback)
        
    return render_template('new_film.html')


def add_new_film(name, rating):
     with open("C:\\Work\\Exercises\\workshop_part3\\film_review.txt", "a+") as f:
            f.write("{0},{1}\r\n".format(name, rating))