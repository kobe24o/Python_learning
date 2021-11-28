# 获取中英文人名翻译
import time
import urllib.request


def getename(ename_data='ename2cname.txt'):
    flag = "jerry.asp?id="  # 特定标记位置
    url = 'https://name.supfree.net/tom.asp?id='
    alphas = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    with open(ename_data, 'w', encoding='utf-8') as f:
        for alpha in alphas:  # 名字首字母
            req = urllib.request.Request(url + alpha)
            req.add_header('User-Agent', 'Mozilla/6.0')
            try:
                res = urllib.request.urlopen(req)
            except:
                print("error")
            # code = res.getcode()
            html = res.read().decode('ANSI')  # 有的网页是 utf-8
            contents = html.split("\n")  # 按行切分

            def gen_func():
                for x in contents:
                    yield x

            gen = gen_func()  # 生成器
            for x in gen:
                if flag in x:
                    l = x.find(flag)
                    r = x.find('"', l)
                    ename = x[l + len(flag):r]
                    print("ename: ", ename)
                    x = gen.__next__()
                    x = gen.__next__()
                    x = gen.__next__()
                    cname = x[4:-6]
                    print("cname: ", cname)
                    print('----------')
                    f.write(ename + '\t' + cname + '\n')

            time.sleep(0.05)
            res.close()
            # print('网页状态码：%s' % (code))
            # print('网页内容：' + html)


if __name__ == '__main__':
    getename()
