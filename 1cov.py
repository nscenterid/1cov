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
print('Berikut kami tampilkan data Terbaru :')
print()
print(icov_data(jumlah_sembuh))
print('Update time', time())
