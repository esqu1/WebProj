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
			d = {}
			d['title'] = el['title']
			d['address'] = el['address']
			d['description'] = el['description']
			d['link'] = el['http_link']
			d['image'] = el["campus_item_images"][0]["image_url"]
			body.append(d)
		return body
  
def req(name):
    r = requests.get("https://api.pennlabs.org/buildings/search?q=%s" % name)
    return r.json()

if __name__ == "__main__":
    app.run()
