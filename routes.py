from flask import render_template, url_for
from . import app, models


@app.route('/')
@app.route("/accueil")
def accueil():
    liste_events = models.vue_event_disc_pays.query.all()
    if liste_events:
        liste_events[0].is_active = True
    return render_template('accueil.html', title='Bienvenue sur notre site', liste_e=liste_events)


@app.route('/tous_events')
def allEvents():
    liste_events = models.vue_event_disc_pays.query.all()
    return render_template('tous_events.html', title='Nos évènements', liste_e=liste_events)


@app.route('/sportifs/<int:id_event>')
def sportifs_by_event(id_event):
    sportifs = models.vue_sportif_disc_pays.query.filter_by(id_event = id_event).all()
    return render_template('sportifs.html', title='Sportifs participant à {id_event}', sportifs=sportifs)