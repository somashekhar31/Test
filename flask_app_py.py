"""
OpenCV REST API to be uploaded to pythonanywhere
"""

# Import required packages:
from flask import Flask, request, jsonify, render_template
import urllib.request

app = Flask(__name__)



@app.errorhandler(400)
def bad_request(e):
    # return also the code error
    return jsonify({"status": "not ok", "message": str(e)}), 400


@app.errorhandler(404)
def not_found(e):
    # return also the code error
    return jsonify({"status": "not found", "message": "route not found"}), 404


@app.errorhandler(500)
def not_found(e):
    # return also the code error
    return jsonify({"status": "internal error", "message": "internal error occurred in server"}), 500



@app.route('/detect', methods=['POST', 'GET'])
def detect_human_faces():
    if request.method == 'GET':
        data = request.args.get('data')
        if data:
            # Process the data from the GET request
            # ...
            #return render_template('index.html',, text="Hi"),200
            return jsonify({"status": "ok", "result": str(data)}), 200
        else:
            return jsonify({"status": "bad request", "message": "Parameter data is not present"}), 400

    elif request.method == 'POST':
        if request.files['data']:
            file = request.files['data']
            k = file.read().decode('utf-8')
            # Process the data from the POST request
            # ...
            return render_template('index.html', text="Hi"),200
        else:
            return jsonify({"status": "bad request", "message": "Parameter data is not "}), 400

    else:
        return jsonify({"status": "failure", "message": "PUT method not supported for API"}), 405

@app.route('/', methods=["GET"])
def info_view():
    return render_template('index.html', text="Hi")


if __name__ == "__main__":
    app.run(debug=True)
