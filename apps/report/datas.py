import json
import re
import zlib
import json
import base64
import requests
url='http://cloud.longgood.com.tw/api/'
cookie_string=""
class TData():
	def get_report_view(self):
		result=self.check_majesty()
		

		return result
	def get_report_json(self):
		result=self.check_majesty()
		json_data=json.dumps(result,indent=2)
		
		return json_data

	def check_majesty(self):
		r=self.go_cloud("get_managed_activity")
		try:
			json_data=r.json()
		except:
			pass
		try:
			json_string=r.text()
			json_data=json.loads(json_string)
		except:
			pass		
		try:
			json_data=r.json()
			return self.data_parsing(json_data)
		except:
			pass
		
		try:
			json_string=r.text
			json_data=json.loads(json_string)
			result=self.data_parsing(json_data)
			return result
		except:
			pass
		return ["error"]
	def data_parsing(self,json_data):
			result=[]
			for d in json_data:
				key=d["key"]
				data=key.split("_")
				device=data[0]
				date=data[1]
				raw_url=self.get_url(key,".csv.lzma")
				json_url=self.get_url(key,".json")
				
				dic={"device":device,"date":date,"raw":raw_url,"json":json_url}
				result.append(dic)
			return result
				
				
				
	def go_cloud(self,purpose):
		global url,cookie_string
		json_string={
		"token":"7c4a8d09ca3762af2l9c9520943d6D1274f8941b",
		"accountId":"itriblueocean",
		"password":"itriblueoceanno1"
		}
		json_data=json.dumps(json_string)
		
		session=requests.Session()
		r = session.post(url+purpose, json=json_string)
			
			#r = requests.post(url, j)
			
		
		return r

	def __get_compress_and_encode(self,target):
		compressed_data = zlib.compress(str.encode(target))
		encoded_data = base64.b32encode(compressed_data)
		result = encoded_data.decode("utf-8")
		return result

	def get_url(self,filename,subname=".csv.lzma"):
		result=self.__get_compress_and_encode(filename+subname)
		serverurl="http://cloud.longgood.com.tw/download/"
		
		return serverurl+result

