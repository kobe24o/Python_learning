def genAB():
    print("start")
    yield 'A'
    print("continue")
    yield 'B'
    print("end")

ans1 = [x*2 for x in genAB()]
# 输出以下内容
# start
# continue
# end

for x in ans1:
    print(x)
# 输出
# AA
# BB

ans2 = (x*2 for x in genAB())
# 无输出

for x in ans2:
    print(x)
# 输出
# start
# AA
# continue
# BB
# end

import itertools
gen = itertools.count(5, 0.5)
print(next(gen))
print(next(gen))
print(next(gen))
# 5
# 5.5
# 6.0

gen = itertools.takewhile(lambda n : n < 6, itertools.count(5, 0.5))
print(list(gen)) # [5, 5.5]