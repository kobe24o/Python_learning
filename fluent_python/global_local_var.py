# def f1(a):
#     print(a)
#     print(b)
#
# b = 5
# f1(3)

b = 5
def f2(a):
    global b
    print(a)
    print(b)
    b = 6
    print(b)

f2(3)
print(b)

# def make_avg():
#     nums = []
#     def averager(val):
#         nums.append(val)
#         total = sum(nums)
#         return total/len(nums)
#     return averager
# avg = make_avg()
# print(avg(10)) # 10.0
# print(avg(20)) # 15.0
# print(avg(30)) # 20.0


def make_avg():
    count = 0
    total = 0
    def averager(val):
        nonlocal count, total
        count += 1
        total += val
        return total/count
    return averager
avg = make_avg()
print(avg(10)) # 10.0
print(avg(20)) # 15.0
print(avg(30)) # 20.0