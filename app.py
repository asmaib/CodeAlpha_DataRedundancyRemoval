from flask import Flask, request, jsonify
import pymongo
from urllib.parse import quote_plus

app = Flask(__name__)


username = quote_plus("asmaibb")
password = quote_plus("100Asma100!")
cluster = "codealphaprojecttask1.yxz6gkx.mongodb.net"
authSource = "admin"
authMechanism = "SCRAM-SHA-1"

uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=CodeAlphaProjectTask1&authSource={authSource}&authMechanism={authMechanism}"


client = pymongo.MongoClient(uri)
db = client["redundancy_db"]
collection = db["data_entries"]











#-------------------------------------------------------------------------------------------------------------------------
#client = MongoClient("mongodb+srv://asmaibb:100Asma100!@codealphaproject.pmr6zot.mongodb.net/?retryWrites=true&w=majority&appName=CodeAlphaProject")

#client = MongoClient("mongodb+srv://asmaibb:<db_password>@codealphaprojecttak1.gr3kncf.mongodb.net/?retryWrites=true&w=majority&appName=CodeAlphaProjectTak1")
#db = client['redundancy_db']      
#collection = db['data_entries']   
#-------------------------------------------------------------------------------------------------------------------------


@app.route("/")
def home():
    return "API is running. Use POST /add to submit data."

@app.route("/add", methods=["POST"])
def add_data():
    new_data = request.json.get("data")

    if not new_data:
        return jsonify({"status": "error", "message": "No data provided"}), 400

    
    if collection.find_one({"data": new_data}):
        return jsonify({"status": "duplicate", "message": "This data already exists in the database."}), 409

    
    collection.insert_one({"data": new_data})
    return jsonify({"status": "success", "message": "Data added successfully.", "data": new_data}), 201

if __name__ == "__main__":
    app.run(debug=True)
