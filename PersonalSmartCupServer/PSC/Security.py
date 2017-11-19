import hashlib

import os

import time

timeout = 600  # 10分钟

path = os.path.split(os.path.realpath(__file__))[0]
file = path + '/config.txt'

verifiedDevices = []
verifiedIPs = []


# 使用ctrl+/快速注释
# def getkey():
#     with open(file, 'r') as f:
#         config = f.read().split('\n')
#         return config[2]
#
#
# def iskey(key):
#     with open(file, 'r') as f:
#         config = f.read().split('\n')
#         if config[1] == 'alreadysetkey':
#             if key == config[2]:
#                 return 'keycorrect'
#             else:
#                 return 'keywrong'
#         else:
#             return 'notInitialize'
#
#
# def setkey(key):
#     with open(file, 'w') as f:
#         config = f.read().split('\n')
#         if config[1] != 'alreadysetkey':
#             with open(file, 'w') as f:
#                 f.write('配置文件 请勿删除\nalreadysetkey\n' + key)


# def isverify(ip, remove=False):
#     print(verifiedIPs)
#     for i in verifiedIPs:
#         if time.time() - float(i.split(' ')[1]) > timeout:
#             verifiedIPs.remove(i)
#         if i.split(' ')[0] == ip:
#             if remove:
#                 verifiedIPs.remove(i)
#             return True
#     else:
#         return False
#
#
# def verify(user,key, ip):
#     tmp = iskey(key)
#     if tmp == 'keycorrect':
#         isverify(ip)
#         verifiedIPs.append(ip + ' ' + str(time.time()))
#         return tmp
#     else:
#         return tmp

def isverify():
    return True


def verify():
    return 'keycorrect'
