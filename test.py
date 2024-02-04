a=100
b=1

try:
    if b<10:
        raise Exception("b cannot be less then 10")
    print(a/b)
except Exception as e:
    print(e)
except ZeroDivisionError:
    print("除数为0")
else:
    print("没有异常")