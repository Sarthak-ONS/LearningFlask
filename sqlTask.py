from flask import Flask, request, jsonify
import mysql.connector as conn

mdb1 = conn.connect(host="localhost", user="root", password="ascas")

app = Flask(__name__)

mydb = conn.connect(host="localhost", user="root", passwd="root")

myCursor = mydb.cursor()
print(mydb)


# Write a program to insert a record in sql table via api database
@app.route('/insertIntoSQL', methods=['GET', 'POST'])
def create_record():
    if request.method == 'POST':
        a = request.json['name']
        b = request.json['age']
        myCursor.execute('Create database if not exists LearnAPITask')
        myCursor.execute('Create table if not exists LearnAPITask.OldPersons(name varchar(10), age int(10))')
        print(f'Insert into LearnAPITask.OldPersons values("{a}",{b})')
        myCursor.execute(f'Insert into LearnAPITask.OldPersons values("{a}",{b})')
        return jsonify((str("Executed Successfully")))


# Write a program to Update a record in sql table via api database
@app.route('/updateRecord', methods=['GET', 'POST'])
def update_record():
    a = request.json['currentName']
    b = request.json['currentAge']
    c = request.json['newName']
    d = request.json['newAge']
    myCursor.execute(f'Update LearnAPITask.OldPersons set name = "{c}"and age={d} where name="{a}", age={b}')

    return jsonify("Executed Successfully")


# Write a program to delete a record in sql table via api database
@app.route('/deleteRecord', methods=['GET', 'POST'])
def delete_record():
    a = request.json['name']
    b = request.json['age']
    x = f'delete from LearnAPITask.OldPersons where name = "{a}"and age = {b} '
    print(x)
    myCursor.execute(x)
    return jsonify("Successfully Removed")


# Write a program to Fetch a record in sql table via api database
@app.route('/fetchRecord', methods=['GET', 'POST'])
def fetch_record():
    a = request.json['name']
    b = request.json['age']
    q = f' Select  *  from  LearnAPITask.OldPersons where name = "{a}"and age={b}'
    print(q)
    x = myCursor.execute(q)
    return jsonify(str(x))


if __name__ == '__main__':
    app.run(debug=False, port=4896)

# Sarthak Agarwal
# agarwalsarthak456@gmail.com
# Class Task for 20 August Live Class ------- FOR SQL ONLY ----------
