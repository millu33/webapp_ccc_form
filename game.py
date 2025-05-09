from flask import Flask
from flask import render_template, request, redirect, url_for
import json 

app = Flask(__name__)

f = open('gametree.json', 'r' )
file_contents = f.read()
game_tree = json.loads(file_contents)

#commands that runs flask framewrok: -m flask --app game run

app = Flask(__name__)
@app.route("/game/forms", methods=['GET', 'POST'])
def forms():
  if request.method == "POST":
     name = request.form['name'] 
     #I looked this up below, to know how to redirect to user onse the form is submitted to the welcome page (state=welcome)
     return redirect(url_for('game', state="welcome", name=name))
  return render_template("forms.html")

#<> signals a variable for flask
@app.route("/game/<state>")
def game(state="welcome"):
      game_state = game_tree[state]  
        
      msg = game_state["message"]
      msg_list = game_state["message_list"]
      ch = game_state["choices"]
      #looked this up below too: it lets the game funciton take the name varible as whatever the user inputs
      name = request.args.get('name')
      
      return render_template("main.html",message=msg, message_list=msg_list, choices=ch, state_id=state, name=name)

    


# @app.route("/game/<state>")
# def game(state="welcome"):

#       game_state = game_tree[state]  
        
#       msg = game_state["message"]
#       msg_list = game_state["message_list"]
#       ch = game_state["choices"]

    
#       return render_template("main.html",message=msg, message_list=msg_list, choices=ch, state_id=state)

    