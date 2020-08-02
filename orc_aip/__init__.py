from aip import AipOcr

# 文档https://ai.baidu.com/ai-doc/OCR/3k3h7yeqa

class ORC(object):
    def __init__(self,app_id = '',api_key = '',secret_key = ''):
        """ 你的 APPID AK SK """
        self.APP_ID = app_id
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

        self.Options={"language_type":"ENG"}
        # options["language_type"] = "CHN_ENG"
        # options["detect_direction"] = "true"
        # options["detect_language"] = "true"
        # options["probability"] = "true"


    def get_text_of_img(self,img:str):
        v_codes = self.client.basicGeneral(img, self.Options)
        print(v_codes)
        # 如果识别到验证码
        if "words_result_num" in v_codes.keys() and v_codes["words_result_num"] >= 1:
            v_code = ''
            # 清洗验证码
            for i in v_codes["words_result"][0]["words"]:
                # 符合的字母存下来
                if i >= 'a' and i <= 'z' or i >= '0' and i <= '9' or i >= 'A' and i <= 'Z':
                    v_code += i
            return v_code
        # 识别失败
        return None

if __name__=="__main__":
    orc=ORC()
    with open("vcode.png","rb") as f:
        v_code=orc.get_text_of_img(f.read())
        print(v_code)
        f.close()