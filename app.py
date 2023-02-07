from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def get_data():
   data = [
      {'id': 1, 'year': 2000},
      {'id': 2, 'year': 2005},
      {'id': 3, 'year': 2021},
   ]
   return data

if __name__ == "__main__":
   app.run(debug=True)