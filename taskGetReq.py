from flask import Flask, jsonify, request
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user="root", passwd="root")

myCursor = mydb.cursor(dictionary=True)
print(mydb)


@app.route("/testFun")
def test():
    get_name = request.args.get("name")
    mobile_number = request.args.get("mobile_number")
    print(get_name)
    return jsonify(str(f"This is my First function for get, {get_name}, {mobile_number}"))


@app.route("/fetchData")
def fetch_data():
    table_name = request.args.get("tableName")
    database_name = request.args.get("db")
    myCursor.execute(f"Select * from {database_name}.{table_name}")
    data = myCursor.fetchall()
    for i in myCursor.fetchall():
        print(i)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
