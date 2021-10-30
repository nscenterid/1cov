#This is a python program.
import requests
import json
print('AIO 1ndonesia Regional Cov Updates')
print('created by NSI Center)
print(' Present for Hacktoberfest 2021')
endpoint = 'https://data.covid19.go.id/public/api/update.json'
      
def icov_data():
	response = requests.get(endpoint)
	data = json.loads(response.text)
	return str(data)      
