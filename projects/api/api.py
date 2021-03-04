from flask import Flask,render_template
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/utkarsh")
def utkarsh():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# if __name__ == "__api__":
#      app.run(debug=True)
app.run()