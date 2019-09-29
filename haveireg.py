import sys, os, importlib.util
import getopt

def load_all(dir="plugins"):
    modules = []
    list_modules=os.listdir(dir)
    list_modules.remove('__init__.py')
    for module_name in list_modules:
        if module_name.split('.')[-1]=='py':
            spec = importlib.util.spec_from_file_location('my_module', dir+os.sep+module_name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules.append(module)
    return modules

def verifyCellphone(phone, modules):
    for module in modules:
        testReg = module.TestReg(phone)
        if testReg.verifyCellphone():
            print("[+] {0} {1}".format(testReg.name, testReg.website))


def verifyEmail(email, modules):
    for module in modules:
        testReg = module.TestReg(email)
        if testReg.verifyEmail():
            print("[+] {0} {1}".format(testReg.name, testReg.website))

def verifyUsername(username, modules):
    for module in modules:
        testReg = module.TestReg(username)
        if testReg.verifyUsername():
            print("[+] {0} {1}".format(testReg.name, testReg.website))


if __name__ == "__main__":
    help_show = '''
HaveIReg is a tool to find out the websites which one may register.
It is a fantatic tool to gather the information.
You can get info from three methods (cellphone, emial, username)

Usage: python haveireg.py [options] [params]

Options:
  -v, --version     Show the version of HaveIReg
  -h, --help        Show the help info
  -c, --cellphone   Search with cellphone
                    E.g. python haveireg.py -c 13945111233 
  -e, --mail        Search with email
                    E.g. python haveireg.py -e 123456789@qq.com 
  -u, --username    Search with username
                    E.g. python haveireg.py -u Robert 
    '''
    modules = load_all()
    try:
        options, args = getopt.getopt(sys.argv[1:], "vhc:e:u:",
                                      ["version", "help", "cellphone=", "email=", "username="])
    except getopt.GetoptError:
        print('Get options Error')
        print(help_show)
        sys.exit(1)
    for key, value in options:
        if key in ['-h', '--help']:
            print(help_show)
        elif key in ['-v', '--version']:
            print('HaveIReg version 0.1')
        elif key in ['-c', '--cellphone']:
            verifyCellphone(value, modules)
        elif key in ['-e', '--email']:
            verifyEmail(value, modules)
        elif key in ['-u', '--username']:
            verifyUsername(value, modules)
