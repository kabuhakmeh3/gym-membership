import requests, json

def getgender(name):
    url = 'https://api.genderize.io?name='
    lookup = url + name
    try:
        req = requests.get(lookup)
        result = json.loads(req.text)
        
        if result['gender'] is not None:
            gender = result['gender']
        else:
            gender = 'unknown'
        return gender
    except:
        return 'unknown'
