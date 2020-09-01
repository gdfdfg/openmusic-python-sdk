'''
Created by yong.huang on 2016.11.04
'''
from top.api.base import RestApi


class HifiveOrderPublishRequest(RestApi):
    def __init__(self, domain='hifive-gateway-test.hifiveai.com', port=80,method="POST"):
        RestApi.__init__(self, domain, port,method)
        self.clientId = None
        self.orderId = None
        self.workId = None

    def getapiname(self):
        return 'OrderPublish'
