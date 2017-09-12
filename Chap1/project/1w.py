weather_dict = {}

with open('weather_info.txt') as f:
    data = f.readlines()
for line in data:
        key,value = line.strip().split(',')
        weather_dict[key] = value

history_dict = {}

def get_help():
    print ('''
    输入想要查询的城市名，查询该城市的天气；
    输入‘帮助’，获得帮助；
    输入‘历史’，获得历史查询信息；
    输入‘退出’，退出程序
    ''')

def get_quit():
    exit(0)

def get_history():
    print('这是您查询过的城市天气：')
    for key,values in list(history_dict.items()):
        print("{}的天气是{}" .format(key,value))

while True:
    user_input = input('请输入指令或查询的城市名：')
    if user_input in weather_dict.keys():
        weather_report = weather_dict[user_input]
        print ('%s: 天气%s' %(user_input, weather_report))
        history_dict[user_input] = weather_report

    else:
        if user_input == '帮助':
            get_help()
        elif user_input == '历史':
            get_history()
        elif user_input == '退出':
            exit(0)
        else:
            print('请输入正确的指令或城市名')
