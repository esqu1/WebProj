from flask import Flask, request, render_template
import requests
app = Flask(__name__)


@app.route("/", methods=['GET'])
def display():
	return render_template('index.html', results = generateResults())

def generateResults():
	body = []
	if request.method == 'GET':
		name = request.args.get('name')
		if name == None:
			body = None
			pass
		for el in req(name)["result_data"]:
			title = el["title"]
			address = el["address"]
			description = el["description"]
			link = el["http_link"]
			body.append(title)

		print body
		return body
  
def req(name):
    r = requests.get("https://api.pennlabs.org/buildings/search?q=%s" % name)
    return r.json()

if __name__ == "__main__":
    app.run()
