from flask import Flask, jsonify      # Import Flask to create the web app, jsonify for JSON responses
from flask_cors import CORS           # Import CORS to enable cross-origin requests

# Create the Flask app instance
app = Flask(__name__)
CORS(app)                             # Enable CORS for the entire app

# Define an HTTP GET route on the root ('/')
@app.route('/')
def hello():
    # Return a JSON response with a message
    return jsonify(message="CIAO DA K8S!!!!!!!!e ehheheheee")

# Start the Flask app only if the file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Listen on all interfaces, port 5000, with debug mode
