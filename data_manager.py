import database_common

'''
@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names
'''

@database_common.connection_handler
def get_tables(cursor, table_name):
    cursor.execute(f"""
                    SELECT first_name, last_name FROM {table_name}""")
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def nicknames(cursor, location):
    cursor.execute(f"""
                    SELECT concat(first_name, ' ', last_name) as fullname, nick_name from mentors
                    where city = '{location}'""")
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def search_for_applicant(cursor, boxes, input_data):
    infos = [data for data in boxes if boxes[data]]
    cursor.execute(f"""
                    SELECT concat(first_name, ' ', last_name) as fullname, phone_number from applicants
                    where {infos[0]} like '%{input_data}%'""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def add_new_applicant(cursor, datas):
    new_datas = [datas[data] for data in datas]
    cursor.execute(f"""
                    INSERT into applicants
                    VALUES ('{new_datas[0]}', '{new_datas[1]}', '{new_datas[2]}', '{new_datas[3]}', '{new_datas[4]}', '{new_datas[5]}')""")


@database_common.connection_handler
def record_applicants(cursor, a_code):
    cursor.execute(f"""
                    SELECT * FROM applicants
                    where application_code = {a_code}""")
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def update_applicant_record(cursor, what, for_what, person_first_name, person_last_name):
    cursor.execute(f"""
                    UPDATE applicants
                    set {what} =  '{for_what}'
                    where first_name = '{person_first_name}' and last_name = '{person_last_name}'""")


@database_common.connection_handler
def cancel(cursor, email):
    cursor.execute(f"""
                    DELETE from applicants
                    where email like '%{email}%'""")
