from flask import Flask, request
app = Flask(__name__)

title = "<h1>Hello this is Anshul's Azure Web App running on Linux!</h1>"

@app.route("/")
def hello():
  return title

@app.route("/echo", methods = [ 'GET' ])
def echo():
  html = "<br><p>Your message was: {message}</p>"
  return title + html.format(message=request.args.get('msg'))

if __name__ == "__main__":
  app.run(host='0.0.0.0')