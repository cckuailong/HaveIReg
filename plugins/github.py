import requests, re, warnings
warnings.filterwarnings("ignore")

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/26"
        self.name = "Github"
        self.website = "https://github.com/"
        self.category = "IT"
        self.iconUrl = ""
        self.desc = '''
        作为开源代码库以及版本控制系统，Github拥有140多万开发者用户。随着越来越多的应用程序转移到了云上，Github已经成为了管理软件开发以及发现已有代码的首选方法
        '''

        self.cellphoneUrl = ""
        self.emailUrl = "https://github.com/signup_check/email"
        self.usernameUrl = "https://github.com/signup_check/username?suggest_usernames=true"

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        judge_true = "already taken"
        url = "https://github.com/signup_check/email"
        s = requests.session()
        r = s.get("https://github.com/join?source=header-home", verify=False)
        token = re.search(r"signup_check/email\" csrf=\"(.*?)\"", r.text).group(1)
        data = {"authenticity_token": (None, token), "value": (None, self.content)}
        resp = s.post(url, files=data)
        if judge_true in resp.text:
            return True
        else:
            return False

    def verifyUsername(self):
        judge_true = "is not available"
        url = "https://github.com/signup_check/username?suggest_usernames=true"
        s = requests.session()
        r = s.get("https://github.com/join?source=header-home", verify=False)
        token = re.search(r"usernames=true\" csrf=\"(.*?)\"", r.text).group(1)
        data = {"authenticity_token": (None, token), "value": (None, self.content)}
        resp = s.post(url, files=data)
        if judge_true in resp.text:
            return True
        else:
            return False
