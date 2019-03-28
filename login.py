#coding:utf-8
from key_md5.key_md5 import key_md5
from ciphertext.ciphertext import creat_pw
userpwd=''
while 1:
    username = str(input('用户名\n'))
    with open('D:\\login.txt','r+') as f:
        string=f.readlines()
        if username+'\n' in string:
            userpwd=creat_pw()
            if (key_md5(userpwd)+ '\n') in string:
                print('登录成功\n')
                exit()
            else:
                while 1:
                    print('密码输入错误')
                    userpwd=creat_pw()
                    if (key_md5(userpwd)+ '\n') in string:
                        print('登录成功')
                        exit()
        else:
            print('请注册用户')
            username=str(input('输入用户名\n'))
            f.write(username+'\n')
            userpwd = creat_pw()
            f.write(key_md5(userpwd) + '\n')
