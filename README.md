# HaveIReg 
[English Readme](https://github.com/cckuailong/HaveIReg/blob/master/README-en.md)
### 简介
1. HaveIReg用于查找出特定用户在哪些网站注册过
2. 用于信息收集
3. 可以根据三种方式进行查询（电话，邮件，昵称[用户名])
### 使用方法
```
使用: python haveireg.py [选项] [参数]
```
```
选项:
  -v, --version     显示版本
  -h, --help        显示帮助信息
  -c, --cellphone   根据电话查找
                    E.g. python haveireg.py -c 13945111233 
  -e, --mail        根据邮件查找
                    E.g. python haveireg.py -e 123456789@qq.com 
  -u, --username    根据用户名查找
                    E.g. python haveireg.py -u Robert 
```
### 附
HaveIReg支持插件化操作，用户可以根据template/template.py模板，加入自定义的插件到Plugins中
