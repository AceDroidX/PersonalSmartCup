import SQLite
import Security


def command(netcmd, sock, addr):
    ip = addr[0]
    port = addr[1]
    # 发送别忘了\n
    if netcmd[0] == 'keepAlive':
        sock.send('keepAlive\n'.encode('utf-8'))
        # print('--->' + addr.__str__() + '>' + 'keepAlive')
    elif netcmd[0] == 'verify':
        tmp = Security.verify(netcmd[1], ip)
        sock.send(('verify ' + tmp + '\n').encode('utf-8'))
        print('--->' + addr.__str__() + '>' + 'verify ' + tmp)
    elif netcmd[0] == 'isSmartCup':
        sock.send('SmartCup\n'.encode('utf-8'))
        print('--->' + addr.__str__() + '>' + 'SmartCup')
    elif netcmd[0] == 'setkey':
        if Security.isverify(addr):
            sock.send(Security.setkey(netcmd[1]).encode('utf-8'))
    elif netcmd[0] == 'state':
        if Security.isverify(ip):
            pass
    elif netcmd[0] == 'readAllRecords':
        tmp = ""
        for i in SQLite.readAllDrinkRecords():
            tmp += i
            pass
    elif netcmd[0] == 'test':
        if Security.isverify(ip):
            pass