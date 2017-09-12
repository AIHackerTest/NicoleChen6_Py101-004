import sys
import requests
import json

history_list = []
unit = 'c'
i = 0

api_keys = {}
api_keys['jiechen'] = 'imo4a446ywejinhm'

def weather_info(location, unit):
    result = requests.get('https://api.seniverse.com/v3/weather/daily.json', params={
            'key': 'aavbujnax07w0irk',
            'location': location,
            'language': 'zh-Hans',
            'unit': unit
        }, timeout=5)
    return result.json()

def show_weather(result, i): # 处理JSON格式信息
    daily = result['results'][0]['daily'][i]
    date = daily['date']
    text_day = daily['text_day']
    text_night = daily['text_night'] #合并
    high, low = daily['high'], daily['low']
    wind_direction = daily['wind_direction']
    wind_scale = daily['wind_scale'] #合并
    weather_str = f'{date}\n{order}白天{text_day},夜晚{text_night}。\
        \n最高气温{high}度,最低气温{low}度\n{wind_direction}风{wind_scale}级。\n'
    return weather_str # ATTR.dict github


while True:
    order = input('请输入指令或您要查询的城市名：')
    try:# 显示查询信息，并保存到history列表中
        result = weather_info(order, unit)
        weather_str = show_weather(result, i)
        print(weather_str)
        history_list.append(weather_str)

    except KeyError:
        if order in ['h', 'help']:
            print(
            '''
                输入城市名，查询该城市的天气；
                输入 help, 获取帮助文档；
                输入 history, 获取查询历史；
                输入 quit, 退出天气查询系统。
            '''
            )
        elif order in ['history']:
            for info in history_list:
                print(info)

        elif order in ['quit', 'q']:
            print("退出查询系统！")
            break

        else:
            print('没有该城市信息!请输入help查看帮助文档。')
