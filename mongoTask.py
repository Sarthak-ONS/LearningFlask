from flask import Flask, request, jsonify
import urllib.parse
import pymongo

app = Flask(__name__)

username = urllib.parse.quote_plus('myUsername')
password = urllib.parse.quote_plus('myPassword')

client = pymongo.MongoClient(
    f"mongodb+srv://{username}:{password}@flutterfame.v340e8u.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# print(db)

database = client['API_Task']

myCollection = database['CRUD_Task']


# Write a program to insert a record in sql table via api database
@app.route('/insertIntoMongoDB', methods=['GET', 'POST'])
def create_record():
    if request.method == 'POST':
        a = request.json['name']
        b = request.json['age']
        myCollection.insert_one({
            "name": str(a),
            "age": b
        })
        return jsonify((str("Executed Successfully")))


# Write a program to Update a record in sql table via api database
@app.route('/updateRecord', methods=['GET', 'POST'])
def update_record():
    a = request.json['currentName']
    b = request.json['currentAge']
    c = request.json['newName']
    d = request.json['newAge']
    updateMap = {"$set" : {
        "name": str(c),
        "age": d
    }}
    myCollection.update_one(filter={"name": str(a), "age": b},update=updateMap)

    return jsonify("Executed Successfully")


# Write a program to delete a record in sql table via api database
@app.route('/deleteRecord', methods=['GET', 'POST'])
def delete_record():
    a = request.json['name']
    b = request.json['age']
    myCollection.remove({"name": str(a), "age": b})
    return jsonify("Successfully Removed")


# Write a program to Fetch a record in sql table via api database
@app.route('/fetchRecord', methods=['GET', 'POST'])
def fetch_record():
    a = request.json['name']
    b = request.json['age']
    myCollection.find({"name": str(a), "age": b})
    return jsonify("Record Fetched Successfully")


if __name__ == '__main__':
    app.run(debug=False, port=4896)

# Sarthak Agarwal
# agarwalsarthak456@gmail.com
# Class Task for 20 August Live Class ------- FOR MongoDB ONLY ----------
