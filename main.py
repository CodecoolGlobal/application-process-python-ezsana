import data_manager
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/tables')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('choose'):
            data_table = request.form.get('choose')
            requested_table_datas = data_manager.get_tables(data_table)
            return render_template('tables.html', requested_table_datas=requested_table_datas)
        if request.form.get('nickn'):
            town = request.form.get('nickn')
            requested_datas = data_manager.nicknames(town)
            return render_template('nicknames.html', requested_datas=requested_datas)
        if request.form.get('info'):
            info_box = {'id': request.form.get('id'),
                        'first_name': request.form.get('first_name'),
                        'last_name': request.form.get('last_name'),
                        'phone_number': request.form.get('phone_number'),
                        'email': request.form.get('email'),
                        'application_code': request.form.get('application_code')}#appl.code-nál nem működik, mert számot vár és str-et kap.
            appl_info = request.form.get('info')
            search = data_manager.search_for_applicant(info_box, appl_info)
            return render_template('search_applicants.html', search=search)
        if request.form.get('e_mail'):
            new_infos = {'id': request.form.get('id'),
                        'first_name': request.form.get('first_name'),
                        'last_name': request.form.get('last_name'),
                        'phone_number': request.form.get('phone_number'),
                        'email': request.form.get('e_mail'),
                        'application_code': request.form.get('application_code')}
            data_manager.add_new_applicant(new_infos)
            return redirect('/')
        if request.form.get('record_for_applicant'):
            code = request.form.get('record_for_applicant')
            record = data_manager.record_applicants(code)
            return render_template('all_record_for_one.html', record=record)
        if request.form.get('update_f_n'):
            first_name = request.form.get('update_f_n')
            last_name = request.form.get('update_l_n')
            which = request.form.get('update_which')
            changed_data = request.form.get('update_data')
            data_manager.update_applicant_record(which, changed_data, first_name, last_name)
            return redirect('/')
        if request.form.get('cancel_applicant'):
            e_mail = request.form.get('cancel_applicant')
            data_manager.cancel(e_mail)
            return redirect('/')
    return render_template('index.html')


@app.route('/nicknames')
def nick_names():
    n_n = data_manager.nicknames()
    return render_template('nicknames.html', n_n=n_n)


if __name__ == '__main__':
    app.run(debug=True)
'''
@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('László')

    return render_template('mentor_names.html', mentor_names=mentor_names)
'''