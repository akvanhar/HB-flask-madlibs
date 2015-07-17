from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    choose_play = request.args.get("choice")
    if(choose_play == "no"):
        return render_template('goodbye.html')
    else:
        return render_template('game.html') 

@app.route('/madlib')
def show_madlib():
    animal_choices = []
    player = request.args.get("person")
    color_choice = request.args.get("color")
    noun_choice = request.args.get("noun")
    adjective_choice = request.args.get("adjective")
    animal_choices.append(request.args.get("cat"))
    animal_choices.append(request.args.get("dog"))
    animal_choices.append(request.args.get("rabbit"))
    animal_choices.append(request.args.get("goldfish"))
    animal_choices.append(request.args.get("python"))
    real_animals = []
    for animal in animal_choices:
        if animal != None:
            real_animals.append(animal)

    food_choice_1 = request.args.get("food1")
    food_choice_2 = request.args.get("food2")

    # make a list of all the various selected animals then pass that into jinja

    return render_template('madlib.html', food1 = food_choice_1, food2 = food_choice_2, person = player, color = color_choice, noun = noun_choice, adjective = adjective_choice, animals=real_animals)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
