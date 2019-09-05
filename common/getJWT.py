from common.getRealDynamicParam import getRealDynamicParam
import json
import requests


class GetJWT:
    s = requests.session()

    def __init__(self):
        self.method = "post"
        self.url = "http://auth-demo.b8.dr.dianrong.io/auth-server/api/internal/jwt/query-by-trusted-application?appName=xiaowang&appSecret=thisispassword&aid=17225903"
        self.header = ""
        self.query_param_template = ""
        self.body_param_template = ""
        self.path_param_template = ""
        self.file_param_template = ""
        self.channel_id = ""
        self.product_code = ""
        self.sub_product_code = ""
        self.market_channel_code = ""
        self.publice_params = ""

    def getJWT(self):
        re = self.s.request(method=self.method, url=self.url, headers=self.header, params=self.query_param_template,
                            data=self.body_param_template)
        content = json.loads(re.text)
        JWT =getRealDynamicParam(content, "authenticationJwt")

        return JWT


if __name__ == '__main__':
    GetJWT().getJWT()
