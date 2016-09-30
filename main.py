from flask import Flask, request
import requests
app = Flask(__name__)


@app.route("/", methods=['GET'])
def display():
	#return render_template('index.html')
	body = """
	<header>
      <nav class="light-blue lighten-1" role="navigation">
	<div class="nav-wrapper container">
	  <a href="/" class="brand-logo">Building Search</a>
	  <a href="#" data-activates="nav-mobile" class="button-collapse"><i class="material-icons">menu</i></a>
	</div>
      </nav>
    </header> <!-- Some header code I took from my personal site. -->
<div class="container">
	<h1>Search Results</h1>
	"""
	head = """
<!DOCTYPE HTML>
<head>
	<!-- Compiled and minified CSS -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/css/materialize.min.css">

	<!-- Compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/js/materialize.min.js"></script>
          
</head>
<body>
	"""
	if request.method == 'GET':
		name = request.args.get('name')
		if name == None:
			body += """
			Enter the name of a building below!
			<form action="/" method="GET">
				<input type="text" name="name">
			</form>
			"""
		body += '<ul class="collection">'
		for el in req(name)["result_data"]:
			title = el["title"]
			address = el["address"]
			description = el["description"]
			link = el["http_link"]
			body += '<li class="collection-item">%s</li>' % title
		body += '</ul>'

		return head + body + "</div></body>"
    

"""
			<table border="2">
				<tr>
					<th><b>Title</b></th>
			<td>%s</td>
		</tr>
		<tr>
			<th><b>Address</b></th>
			<td>%s</td>
		</tr>
		<tr>
			<th><b>Description</b></th>
			<td>%s</td>
		</tr>
		<tr>
			<th><b>Website</b></th>
			<td><a href="%s" target="_blank">%s</a></td>
		<tr>
	</table><br>
				""" #% (title, address, description, link, link)



def req(name):
    r = requests.get("https://api.pennlabs.org/buildings/search?q=%s" % name)
    return r.json()

if __name__ == "__main__":
    app.run()
