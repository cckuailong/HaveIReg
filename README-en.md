# HaveIReg
[中文 Readme](https://github.com/cckuailong/HaveIReg/blob/master/README.md)
### What is it
1. HaveIReg is a tool to find out the websites which one may register.
2. It is a fantatic tool to gather the information.
3. You can get info from three methods (cellphone, emial, username)
### How to use it
```
Usage: python haveireg.py [options] [params]
```
```
Options:
  -v, --version     Show the version of HaveIReg
  -h, --help        Show the help info
  -c, --cellphone   Search with cellphone
                    E.g. python haveireg.py -c 13945111233 
  -e, --mail        Search with email
                    E.g. python haveireg.py -e 123456789@qq.com 
  -u, --username    Search with username
                    E.g. python haveireg.py -u Robert 
```
### What's more
It is a tool with plugin. You can customize your own plugin
to search following the models of template/template.py
