from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Replace these values with your Google Cloud SQL credentials
DB_HOST = '34.101.194.111'
DB_USER = 'dafafikra'
DB_PASSWORD = 'Dafafikra123'
DB_NAME = 'myfirstdb'

# Connect to the Google Cloud SQL database
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
db_cursor = db_connection.cursor()

# Routes for CRUD operations
@app.route('/users', methods=['GET'])
def get_users():
    db_cursor.execute("SELECT * FROM firsttable")
    users = db_cursor.fetchall()
    user_list = []
    for user in users:
        user_dict = {
            'id': user[0],
            'name': user[1],
            'age': user[2],
            'gender': user[3]
        }
        user_list.append(user_dict)
    return jsonify(user_list)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    if name and age and gender:
        insert_query = "INSERT INTO firsttable (name, age, gender) VALUES (%s, %s, %s)"
        values = (name, age, gender)
        db_cursor.execute(insert_query, values)
        db_connection.commit()
        return jsonify({"message": "User added successfully"})
    else:
        return jsonify({"error": "Missing data"}), 400

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    if name and age and gender:
        update_query = "UPDATE firsttable SET name = %s, age = %s, gender = %s WHERE id = %s"
        values = (name, age, gender, user_id)
        db_cursor.execute(update_query, values)
        db_connection.commit()
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"error": "Missing data"}), 400

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    delete_query = "DELETE FROM firsttable WHERE id = %s"
    values = (user_id,)
    db_cursor.execute(delete_query, values)
    db_connection.commit()
    return jsonify({"message": "User deleted successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)