from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_API_URL = "http://backend-service.backend:5000/api/is_malicious"  # Replace with your backend API URL

@app.route("/")
def index():
    return render_template("index.html")

def check_malicious(domain):
    try:
        response = requests.post(BACKEND_API_URL, json={"domain": domain})
        data = response.json()
        result = data.get("result")
    except Exception as e:
        result = "An error occurred while checking the domain."
    return result


@app.route("/check_domain", methods=["POST"])
def check_domain():
    domain = request.form.get("domain")
    if check_malicious(domain)=="True":
        result = 'This domain is malicious'
    else:
         result = 'This domain is not malicious'
    return render_template("result.html", domain=domain, result=result)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
