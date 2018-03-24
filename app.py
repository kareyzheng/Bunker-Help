from flask import Flask, request, render_template, send_from_directory
import json
import pymysql.cursors

app = Flask(__name__)


def get_database_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        db='todo_database',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/', methods=['GET'])
def index():
    conn = get_database_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `todo`"
            cursor.execute(sql)
            data = cursor.fetchall()
    except Exception as e:
        print('ERROR', e)
        conn.close()
        return 'failure reading database', 500

    conn.close()
    return render_template('index.html', data=data)


@app.route('/style.css')
def serve_stylesheet():
    return send_from_directory('static/css/', 'style.css')


@app.route('/mech.js')
def serve_js():
    return send_from_directory('static/js/', 'javascript.js')


@app.route('/favicon.ico')
def serve_icon():
    return send_from_directory('static/img/', 'favicon.ico')


@app.route('/todo/create', methods=['POST'])
def create():
    new_item = request.headers['Content']
    conn = get_database_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO `todo` (`item`) VALUES (%s);"
            cursor.execute(sql, (new_item))
        conn.commit()
    except Exception as e:
        print('ERROR', e)
        conn.close()
        return str({'result': 'failure'}), 500

    conn.close()
    return str({'result': 'success'})


@app.route('/todo/read', methods=['GET'])
def read():
    conn = get_database_connection()
    read_response = {'result': 'success'}
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `todo`;"
            read_response['data'] = cursor.fetchall(sql)
    except Exception as e:
        print('ERROR', e)
        conn.close()
        return str({'result': 'failure'}), 500

    conn.close()
    return str(json.dumps(read_response, indent=4))


@app.route('/todo/update', methods=['PUT'])
def update():
    new_item = request.headers['contents']
    item_num = int(request.headers['item_number'])
    conn = get_database_connection()
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE `todo` SET `item`=%s WHERE `id`=%i;" % new_item, item_num
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("ERROR", e)
        conn.close()
        return str({'result': 'failure'})

    conn.close()
    return str({'result': 'success'})


@app.route('/todo/delete', methods=['DELETE'])
def delete():
    conn = get_database_connection()
    item_del = int(request.headers['item_number'])
    try:
        with conn.cursor() as cursor:
            sql = 'DELETE FROM `todo` WHERE `id`=%i;' % item_del
            cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("ERROR", e)
        conn.close()
        return str({'result': 'failure'})

    conn.close()
    return str({'result': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')