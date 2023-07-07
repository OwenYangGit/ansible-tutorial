# Example code for test grafana contact point with webhook type
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook')
def index():
    message = request.get_json()
    print(json.dumps(message ,indent=2))
    # notify logic
    # maybe send to slack , send to email or anything communication tools
    return 'Grafana Webhook Notify'

app.run(host='0.0.0.0', port=5000)