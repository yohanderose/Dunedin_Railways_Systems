from flask import Flask, render_template

app = Flask(__name__)

    """
    Here is the flask control room!
    Each address 'route' triggers a method that returns the relevant page

    Debug is set to True so changes will show up without restarting.

    We're using flask and bootstrap so check out the html files
    to get familiar with why it works.

    Run this and see how it looks!
    """

@app.route('/')
def volunteer():
    return render_template('volunteer.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)
