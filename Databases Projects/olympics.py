import csv
import os
import MySQLdb

"""
Python script that loads CSV file into MySQL Database. Originally a Python file.
"""


def main():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='*SerMarSer10*',
                           db='olympicsdb')
    c = conn.cursor()

    participant_insert = 'INSERT INTO Participant (year, medal, event, athlete_id) VALUES (%s, %s, %s, %s);'
    location_insert = 'INSERT INTO Location (year, city) VALUES (%s, %s);'
    athlete_insert = 'INSERT INTO Athlete (athlete, country, gender) VALUES (%s, %s, %s);'
    event_insert = 'INSERT INTO Event (event, discipline, sport) VALUES (%s, %s, %s);'

    with open('COSC330 Group Choices - Olympics.csv', encoding='utf8') as mfile:
        csvreader = csv.DictReader(mfile)
        for row in csvreader:
            try:
                c.execute(athlete_insert, [row['Athlete'], row['Country'], row['Gender']])
                athlete_id = c.lastrowid
            except MySQLdb.IntegrityError:
                c.execute('SELECT athlete_id FROM Athlete WHERE athlete=%s AND country=%s AND gender=%s;',
                          [row['Athlete'], row['Country'], row['Gender']])
                athlete_id = c.fetchone()[0]
            try:
                c.execute(participant_insert, [row['Year'], row['Medal'], row['Event'], athlete_id])

            except MySQLdb.IntegrityError:
                pass
            try:
                c.execute(location_insert, [row['Year'], row['City']])
            except MySQLdb.IntegrityError:
                pass

            try:
                c.execute(event_insert, [row['Event'], row['Discipline'], row['Sport']])

            except MySQLdb.IntegrityError:
                pass

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
