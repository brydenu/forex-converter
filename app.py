from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from conversion import Conversion


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# debug = DebugToolbarExtension(app)


@app.route("/")
def home():
    """Renders homepage"""

    return render_template("index.html")


@app.route("/convert")
def convert():
    """Takes information from forms, creates a new conversion object with those values"""

    # Gathers information from form fields and creates a new Conversion() object from info
    curr_from = request.args.get("from")
    curr_to = request.args.get("to")
    amount = request.args.get("amount", 0)
    c = Conversion(curr_from, curr_to)

    # Checks each field for valid inputs via Conversion properties
    # If any inputs invalid, flash message informing which one and stays on page
    err = False
    if not c.curr_from:
        flash("Invalid 'from' currency code: " + curr_from)
        err = True
    if not c.curr_to:
        flash("Invalid 'to' currency code: " + curr_to)
        err = True
    try:
        float(amount)
    except:
        flash("Invalid amount")
        err = True
    if err:
        return redirect("/")

    # If all values are valid, call convert_amount method to get formatted converted value
    if c.curr_to and c.curr_from and amount:
        conv = c.convert_amount(amount)
    else:
        conv = 0
    return render_template("converted.html", rate=c.rate, conv=conv)
