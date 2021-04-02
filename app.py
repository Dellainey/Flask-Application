
import os
import json
import pickle
 
from flask import Flask, request, Response

class Model(object):
    def __init__(self, vectorizer, model):
        self.vectorizer = vectorizer
        self.model = model
 
    def prediction(self, input):
        msg = input['msg']
        message = self.vectorizer.transform([msg])
        answer = self.model.predict(message)
        return int(answer[0])
 
# Load the model
  
model = Model(
   vectorizer = pickle.load(open('model/vectorizer.pickle','rb')),
   model = pickle.load(open('model/sentiment_model.pickle','rb'))
)
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
   target = os.environ.get('TARGET', 'World')
   return 'Hello {}!\n'.format(target)
 
@app.route('/predict', methods=['POST'])
def predict():
   sentiment = request.get_json()
   return Response(json.dumps(model.prediction(sentiment)),  mimetype='application/json')
  
if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))  