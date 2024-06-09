from flask import render_template, url_for
from . import app, models


@app.route('/')
@app.route("/accueil")
def accueil():
    return render_template('accueil.html', title='Bienvenue sur notre site')


@app.route('/tous_events')
def allEvents():
    liste_events = models.vue_event_disc_pays.query.all()
    return render_template('tous_events.html', title='Nos évènements', liste_e=liste_events)
