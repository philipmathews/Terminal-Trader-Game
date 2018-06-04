import requests
import json

class Markit:
	def __init__(self,):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input=%s"
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=%s"

	def company_search(self,string):
		full_url= self.lookup_url % string
		r=requests.get(full_url)
		c=r.content
		e=json.loads(c)
		return e
	
	def get_quote(self,string):
		full=self.quote_url % string
		f= requests.get(full)
		t=f.content
		w=json.loads(t)
		return w