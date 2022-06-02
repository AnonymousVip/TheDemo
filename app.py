from flask import Flask,jsonify
from flask import request
app = Flask(__name__)

@app.route("/")
def home():
	filename = request.args.get('fn');
	success = True;
	json = {
	'success':success,
	'text':"Hello Bois"
	}
	return jsonify(json);
	
if __name__ == "__main__":
	print('Starting hello-world server...');
	app.run(host='0.0.0.0', port=8080);
