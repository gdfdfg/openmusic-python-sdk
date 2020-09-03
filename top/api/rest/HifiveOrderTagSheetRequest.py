'''
Created by yong.huang on 2016.11.04
'''
from top.api.base import RestApi


class HifiveOrderTagSheetRequest(RestApi):
    def __init__(self, domain=None, port=80):
        domain = domain or 'hifive-gateway-test.hifiveai.com';
        RestApi.__init__(self, domain, port)
        self.clientId = None
        self.tagId = None
        self.recoNum = None
        self.language = None
        self.type = None

    def getapiname(self):
        return 'OrderTagSheet'
