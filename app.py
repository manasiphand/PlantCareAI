from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "PlantCare AI Running Successfully"

if _name_ == "_main_":
    app.run(debug=True)
