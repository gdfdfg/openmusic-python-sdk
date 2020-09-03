'''
Created by yong.huang on 2016.11.04
'''
from top.api.base import RestApi


class HifiveSearchMusicRequest(RestApi):
    def __init__(self, domain=None, port=80, method=None):
        domain = domain or 'hifive-gateway-test.hifiveai.com';
        method = method or 'POST';
        RestApi.__init__(self, domain, port, method)
        self.clientId = None
        self.keyword = None
        self.language = None
        self.price = None
        self.tagId = None
        self.bpm = None
        self.duration = None
        self.Page = None
        self.PageSize = None

    def getapiname(self):
        return 'SearchMusic'
