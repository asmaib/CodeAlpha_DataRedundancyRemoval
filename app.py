from flask import Flask, request, render_template
import pymongo
from urllib.parse import quote_plus

app = Flask(__name__)

# MongoDB connection
username = quote_plus("asmaibb")
password = quote_plus("000")
cluster = "codealphaprojecttask1.yxz6gkx.mongodb.net"
authSource = "admin"
authMechanism = "SCRAM-SHA-1"

uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=CodeAlphaProjectTask1&authSource={authSource}&authMechanism={authMechanism}"

client = pymongo.MongoClient(uri)
db = client["redundancy_db"]
collection = db["data_entries"]

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    color_class = ""
    show_message = False

    if request.method == "POST":
        new_data = request.form.get("data", "").strip()
        show_message = True

        if not new_data:
            message = "No data provided!"
            color_class = "error"
        elif collection.find_one({"data": new_data}):
            message = "Data already exists!"
            color_class = "warning"
        else:
            collection.insert_one({"data": new_data})
            message = "Data added successfully!"
            color_class = "success"

    return render_template("index.html", message=message, color_class=color_class, show_message=show_message)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

