from flask import Flask, jsonify, request
import requests
import redis
import json

app = Flask(__name__)


#ONLY FOR DEMO. In production app this sensitive values will go in a secret manager 
VIRUSTOTAL_API_KEY = "dummy-key"  
redis_client = redis.Redis(host='redis.database', port=6379, db=0) 

def check_malicious_domain(domain):
    try:
        #ONLY FOR DEMO. In production app this dynamic values will go in a config map 
        url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        headers = {
            "x-apikey": VIRUSTOTAL_API_KEY,
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            #print(data)
            reputation = data['data']['attributes']['reputation']
            print (reputation)
            return reputation < 0
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



@app.route("/api/is_malicious", methods=["POST","OPTIONS"])
def is_malicious():
    domain = request.json.get("domain")
    #result = check_malicious_domain(domain)

    # Check if the result is cached in Redis
    cached_result = redis_client.get(domain)
    if cached_result is not None:
        print('Cache hit')
        result = json.loads(cached_result)
    else:
        print('Cache miss')
        result = str(check_malicious_domain(domain))
        print(result)
        # Store the result in Redis with 1 hour expiry
        redis_client.set(domain, json.dumps(result), 3600) 

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
