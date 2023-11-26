import requests
import json
url='http://52.197.148.115/get_gait'
#url="http://localhost/get_gait"
def post_json(score=0.80):
    json_data={
        "Token": "Ac69b674cCxj/6ej3j;6DCc623e2A",
        "User":
        {
           "ID": "LG123456789",
           "Name":  "龍骨王",
           "BirthDay": "1994/01/02",
           "Gender": 1,
        },
        "Activity":
        {
           "ExecuteTime": "2023/03/23 15:25:24",
           "ActivityName": "83HarvestCarrots",
           "Score": 1,
        },
        "Custom":
        {   
           "ExecutionLevel": score,
           "ReportURL": "https://www.longgood.com.tw/",
           "JsonFile": "https://drive.google.com/uc?export=download&id=1X_bFlZCto6HdYus0CXDJizouZjN2YLtJ",
           "RawFile": "https://drive.google.com/uc?export=download&id=1rTDHHViBAiXSRy4DMlHuil3sQmQMM0bA",
        }
    }
    json_data=json.dumps(json_data)
    print("URL:",url)
    
    print("jsondata:",type(json_data),",",json_data)
    r = requests.post(url, json=json_data)
    print(r)
	#print(f"Status Code: {r.status_code}, Response: {r.json()}")



if __name__ == '__main__':
	i=0.5
	post_json(1/(i+1))