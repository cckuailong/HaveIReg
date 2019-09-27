import os, importlib.util

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

def verifyCellphone(phone, modules):
    for module in modules:
        testReg = module.TestReg(phone)
        print(testReg.verifyCellphone())

def verifyEmail(email, modules):
    for module in modules:
        testReg = module.TestReg(email)
        print(testReg.verifyEmail())

def verifyUsername(username, modules):
    for module in modules:
        testReg = module.TestReg(username)
        print(testReg.verifyUsername())


if __name__ == "__main__":
    moudles = load_all()
