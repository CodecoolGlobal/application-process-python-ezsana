import data_manager
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names()
    #mentor_names = data_manager.get_mentor_names_by_first_name('László')

    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/mentors-with-nicknames')
def mentor_nicknames():
    mentor_nicknames = data_manager.mentor_nicknames()
    return render_template('mentor_nicknames.html', mentor_nicknames=mentor_nicknames)


@app.route('/carol')
def carol():
    girl_with_hat = data_manager.carol()
    return render_template('carol.html', girl_with_hat=girl_with_hat)


@app.route('/girl_with_adipiscingenimmi')
def adipiscingenimmi():
    girl_with_email = data_manager.adipiscingenimmi()
    return render_template('girl_with_adipiscingenimmi.html', girl_with_email=girl_with_email)

@app.route('/markus')
def markus():
    new_guy = data_manager.markus()
    return render_template('markus.html', new_guy=new_guy)


@app.route('/jemima')
def jemima():
    girl = data_manager.jemima()
    return render_template('jemima.html', girl=girl)


if __name__ == '__main__':
    app.run(debug=True)
