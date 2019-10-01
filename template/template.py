import requests, re, warnings
warnings.filterwarnings("ignore")

class TestReg():
    def __init__(self, content):
        self.content = content
        self.author = "cckuailong"
        self.date = "2019/09/30"
        self.name = ""
        self.website = ""
        self.category = ""
        self.iconUrl = ""
        self.desc = '''
        
        '''

        self.cellphoneUrl = ""
        self.emailUrl = ""
        self.usernameUrl = ""

    def verifyCellphone(self):
        return False

    def verifyEmail(self):
        return False

    def verifyUsername(self):
        return False

testReg = TestReg("15846007767")
testReg.verifyCellphone()