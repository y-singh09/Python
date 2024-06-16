import json

def report(json_path):
    with open(json_path,'r')as file:
        weather_data=json.load(file)
    return weather_data

if __name__=="__main__":
    json_path='weather_data.json'
    try:
        weather_data=report(json_path)
        print("City:",weather_data['city'])
        print("Temperature:",weather_data['temperature'])
        print("Condition:",weather_data['condition'])
    except FileNotFoundError:
        print('File Not Found')
    except KeyError:
        print("KEy Error")


