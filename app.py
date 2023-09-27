import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/food')
def fetch_food():
    # Database connection parameters
    db_config = {
        'host': 'commitdb.cilaxpjy0njq.us-east-1.rds.amazonaws.com',
        'user': 'admin',
        'password': 'Aa123456',
        'database': 'commit'
    }

    # Connect to the database
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Query to fetch data from the "food" table
        query = 'SELECT * FROM food'
        cursor.execute(query)
        result = cursor.fetchall()

        # Format the data as HTML
        html = '<html><head><title>Food Table</title></head><body>'
        html += '<h1>Food Table</h1><table border="1">'
        html += '<tr><th>ID</th><th>Name</th><th>Description</th><th>Price</th></tr>'
        for row in result:
            html += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>'
        html += '</table></body></html>'

        return html

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

