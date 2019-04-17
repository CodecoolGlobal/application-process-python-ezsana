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

@app.route('/mentors')
def mentors_schools():
    mentors_and_schools = data_manager.m_s()
    return render_template('mentors.html', mentors_and_schools=mentors_and_schools)

@app.route('/all-school')
def all_schools():
    all_of_schools = data_manager.all_school()
    return render_template('schools.html', all_of_schools=all_of_schools)

@app.route('/mentors-by-country')
def mentors_by_country():
    m_by_c = data_manager.by_country()
    return render_template('countries_mentors.html', m_by_c=m_by_c)

@app.route('/contacts')
def contacts():
    schools_contact = data_manager.contacts()
    return render_template('contacts.html', schools_contact=schools_contact)

@app.route('/applicants')
def applicants():
    app = data_manager.applicant()
    print(app)
    return render_template('applicants.html', app=app)


@app.route('/applicants-and-mentors')
def app_and_ment():
    am = data_manager.app_and_mentors()
    print(am)
    return render_template('applicants-mentors.html', am=am)

if __name__ == '__main__':
    app.run(debug=True)
