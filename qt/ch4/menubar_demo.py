# _*_ coding: utf-8 _*_
# @Time : 2022/5/8 20:24
# @Author : Michael
# @File : menubar_demo.py
# @desc :
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QAction, QApplication


class MenuBarDemo(QMainWindow):
    def __init__(self):
        super(MenuBarDemo, self).__init__()
        layout = QHBoxLayout()
        bar = self.menuBar() # 获取菜单栏

        file = bar.addMenu('文件') # 创建菜单栏文件菜单
        file.addAction('新建') # 在文件菜单中添加新建菜单

        save = QAction('保存', self) # 创建保存菜单
        save.setShortcut('Ctrl+S') # 设置快捷键
        file.addAction(save) # 在文件菜单中添加保存菜单

        edit = file.addMenu('编辑') # 在文件菜单中创建编辑菜单
        edit.addAction('复制') # 在编辑菜单中添加复制菜单
        edit.addAction('粘贴') # 在编辑菜单中添加粘贴菜单

        quit = QAction('退出', self) # 创建退出菜单
        quit.setShortcut('Ctrl+Q') # 设置快捷键
        file.addAction(quit) # 在文件菜单中添加退出菜单

        file.triggered[QAction].connect(self.processTrigger) # 菜单触发事件

        self.setLayout(layout)
        self.setWindowTitle('菜单栏demo')
    def processTrigger(self, q):
        print(q.text(), '被点击了')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MenuBarDemo()
    win.show()
    sys.exit(app.exec_())