# class Deck:

#     def __init__(self):
#         affiliation1 = ''
#         affiliation2 = ''
#         pods1 = []
#         pods2 = []
from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

POD_NAME = 0
POD_COUNT = 1


DECKS = [ { 'affiliation1' : 'scum', 'affiliation2' : 'navy', 'pods1' : [("the hunter's flight", 2), ('masterful manipulations', 2), ("the hutt's menagerie", 1)], 'pods2' : [('defending the trench', 2), ("the empire's elite", 2), ('guarding the wing', 1)] }, { 'affiliation1' : 'rebel', 'affiliation2' : 'jedi', 'pods1' : [("heroes of the rebillion", 2), ('the rebel fleet', 1)], 'pods2' : [("a hero's trial", 2), ('may the force be with you', 2), ('the secret of shantipole', 2), ("a heroe's journey", 1)]} ]


@app.route("/")
@app.route("/home")
def home():
    return render_template( 'home.html' )


if __name__ == '__main__':
    app.debug = True
    app.run( port = 5066 )
