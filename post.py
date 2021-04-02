#make a POST request
import requests
dictToSend = {'msg':'I am very very happy today'}
res = requests.post('http://localhost:8080/predict', json=dictToSend)
print (f'response from server: {res.text}')
dictFromServer = res.json()