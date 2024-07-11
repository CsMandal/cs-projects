import requests
par = {
    'amount':10,
    'type':'boolean'
}
response = requests.get('https://opentdb.com/api.php',params=par)
response.raise_for_status()
data = response.json()
question_data = data['results']
