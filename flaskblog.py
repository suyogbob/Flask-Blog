from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Lyra Dawn',
        'title': 'Angels',
        'content': 'Assemble and defend',
        'date_posted': 'January 2, 2019'
    },
    {
        'author': 'Josu Vess',
        'title': 'Zombies',
        'content': 'Begin the march',
        'date_posted': 'January 3, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
