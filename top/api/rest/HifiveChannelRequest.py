'''
Created by yong.huang on 2016.11.04
'''
from top.api.base import RestApi
class HifiveChannelRequest(RestApi):
	def __init__(self,domain=None,port=80):
		domain = domain or 'hifive-gateway-test.hifiveai.com';
		RestApi.__init__(self,domain, port)
		self.clientId = None

	def getapiname(self):
		return 'Channel'
