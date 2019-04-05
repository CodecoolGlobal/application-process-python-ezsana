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
def get_mentor_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors;
                   """)
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def mentor_nicknames(cursor):
    cursor.execute("""
                        SELECT nick_name FROM mentors
                        where city = 'Miskolc';
                       """)
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def carol(cursor):
    cursor.execute("""
                        SELECT first_name, last_name, phone_number FROM applicants
                        where first_name = 'Carol';
                       """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def adipiscingenimmi(cursor):
    cursor.execute("""
                        SELECT CONCAT(first_name,' ', last_name) as fullname, phone_number FROM applicants
                        where email like '%@adipiscingenimmi.edu';
                       """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def markus(cursor):
    cursor.execute("""
                        SELECT * FROM applicants
                        where application_code = 54823;
                       """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def jemima(cursor):
    cursor.execute("""
                        SELECT phone_number FROM applicants
                        where first_name = 'Jemima' and last_name = 'Foreman';
                       """)
    names = cursor.fetchall()
    return names