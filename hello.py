#coding=utf-8
#!/usr/bin/python
import os

temp = '你好,世界'
#先按原来的编码格式解码为万国码
temp_unicode = temp.decode('utf-8')
#再将解码获得的万国码编码为gbk
temp_gbk = temp_unicode.encode('gbk')
#再打印的时候想以GBK的方式显示，windows的终端刚好是GBK的编码，两者匹配
#temp_gbk就是编成的GBK内容，print(temp_gbk)就是以gbk的方式显示出来了
print(temp_gbk)
os.system("pause")