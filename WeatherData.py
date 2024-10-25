import requests
import json

def getTimeData():
    r = requests.get('https://www.cwb.gov.tw/Data/js/GT/TableData_GT_T_68.js?T=2023061602-4&_=1686854847242')

    # time data
    time_start = r.text.find('C')+4
    time_end = r.text.find(',')-1
    time_data = "<" + r.text[time_start:time_end].replace("<br>", " ") + ">"
    return time_data

def getWeatherData():
    r = requests.get('https://www.cwb.gov.tw/Data/js/GT/TableData_GT_T_68.js?T=2023061602-4&_=1686854847242')

    # weather data
    weather_start = r.text.find('6800200')+9
    weather_end = r.text.find('}', weather_start, 350)+1

    weather_data = r.text[weather_start:weather_end].replace("'", "\"").replace("-", "no data ")
    weather_dic = json.loads(weather_data)

    weather_data = "       溫度 : " + weather_dic['C_T'] + "°C\n體感溫度 : " + weather_dic['C_AT'] + "°C\n相對濕度 : " + weather_dic['RH'] + "%\n    時雨量 : " + weather_dic['Rain'] + "mm\n        日出 : " + weather_dic['Sunrise'] + "\n        日落 : " + weather_dic['Sunset']
    return weather_data

def mergeData():
    mergeData = "\n" + getTimeData() + "\n===============\n" + getWeatherData()
    return mergeData

                





                