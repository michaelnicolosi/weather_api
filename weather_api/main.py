import requests 
import json
from flask import Flask, render_template

app = Flask(__name__)


# api-endpoint 
URL = "http://api.openweathermap.org/data/2.5/weather?zip=20102,us&units=imperial&APPID=54ab13db85eaf0fb3fa258c129243908"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json()


@app.route('/')
def hello_world():
    return render_template('home.html', name = data)

if __name__ == "__main__":
    app.run(debug=True)



 
  
