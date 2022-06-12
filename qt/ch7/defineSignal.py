# _*_ coding: utf-8 _*_
# @Time : 2022/6/11 15:32
# @Author : Michael
# @File : defineSignal.py
# @desc :

from PyQt5.QtCore import QObject, pyqtSignal

class QTypeSignal(QObject):
    sendmsg = pyqtSignal(object)
    def __init__(self):
        super(QTypeSignal, self).__init__()
    def run(self):
        self.sendmsg.emit('hello michael')

class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self, msg):
        print("QSlot get msg: ", msg)

if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeSlot()
    print('连接信号与槽')
    send.sendmsg.connect(slot.get)
    send.run()

    print('断开信号与槽')
    send.sendmsg.disconnect(slot.get)
    send.run()