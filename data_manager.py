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

# Mentors and schools page [/mentors]
# On this page you should show the result of a query that returns the name of the mentors plus the
# name and country of the school (joining with the schools table) ordered by the mentors id column
# columns: mentors.firstname, mentors.last_name, schools.name, schools.country_

@database_common.connection_handler
def m_s(cursor):
    cursor.execute("""
                    select mentors.first_name, mentors.last_name, schools.name, schools.country
                    from mentors 
                    left join schools
                    on mentors.city = schools.city
                    order by mentors.id""")
    m_and_s = cursor.fetchall()
    return m_and_s

# All school page [/all-school]
# On this page you should show the result of a query that returns the name of the
# mentors plus the name and country of the school (joining with the schools table)
# ordered by the mentors id column. BUT include all the schools, even if there's no mentor
# yet (in that cell, "No data" should be displayed)!
# columns: mentors.firstname, mentors.last_name, schools.name, schools.country_

@database_common.connection_handler
def all_school(cursor):
    cursor.execute("""
                        select mentors.first_name, mentors.last_name, schools.name, schools.country
                        from mentors 
                        right join schools
                        on mentors.city = schools.city
                        order by mentors.id""")
    m_and_s = cursor.fetchall()
    return m_and_s


# Mentors by country page [/mentors-by-country]í
#On this page you should show the result of a query that returns the number
#of the mentors per country ordered by the name of the countries
#columns: country, count

@database_common.connection_handler
def by_country(cursor):
    cursor.execute("""
                    select schools.country, count(mentors.last_name) as count
                    from schools
                    left join mentors
                    on mentors.city = schools.city
                    group by schools.country
                    order by schools.country""")
    count_mentors = cursor.fetchall()
    return count_mentors

# Contacts page [/contacts]
# On this page you should show the result of a query that returns the name of the school
# plus the name of contact person at the school (from the mentors table) ordered by the name of the school
# columns: schools.name, mentors.firstname, mentors.last_name_

@database_common.connection_handler
def contacts(cursor):
    cursor.execute("""
                    select schools.name, concat(mentors.first_name, ' ', mentors.last_name) as fullname
                    from schools
                    inner join mentors
                    on schools.contact_person = mentors.id """)
    contact = cursor.fetchall()
    return contact