import requests
import WeatherData

def sendLineNotify(msg):
    url = 'https://notify-api.line.me/api/notify'
    token = 'bDdLChdJvNjdM2ju5pSRDgVyFTEK7XH5vPZurhUOnlm'
    # token = 'IwO0zNSJ1wlvCd2O7Ntx1tE0JUyggzYHlPHGPpqYSM9'
    headers = {
        'Authorization': 'Bearer ' + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {
        'message' : msg
    }
    r = requests.post(url, headers = headers, data = data)
    print(r.status_code)

if __name__ == '__main__':
    message = WeatherData.mergeData()
    sendLineNotify(message)




