from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
	return 'Hello from CS-406 API', 200


@app.route('/login', methods=['GET', 'POST'])
def login():
	# For now, just return a simple text response.
	# In a real app you'd validate credentials here.
	return 'Login page', 200


if __name__ == '__main__':
	# Use port 8080 to be compatible with common cloud runtimes.
	app.run(host='0.0.0.0', port=8080)

