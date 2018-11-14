import json
import MySQLdb
import MySQLdb.cursors
import flask
"""
This program allows for a user to perform search queries on the database using a webapp. 
"""

app = flask.Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


@app.route('/year/<title>')
def city(title):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='*SerMarSer10*',
                           db='OlympicsDB',
                           cursorclass=MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('Select * FROM Location WHERE city LIKE %s;', [title])
    if c.rowcount > 0:
        rs = c.fetchall()
        return flask.render_template('city.html', title=title, data=[r for r in rs])
    else:
        return flask.render_template('nocity.html', title=title)


@app.route('/json/year/<title>')
def json_year(title):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='*SerMarSer10*',
                           db='OlympicsDB',
                           cursorclass=MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('Select * FROM Location WHERE city LIKE %s;', [title])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    s = json.dumps({'City': result_list})
    return s



#

if __name__ == '__main__':
    app.run()
