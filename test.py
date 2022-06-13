import time
import timeout_decorator


@timeout_decorator.timeout(3)
def test():
    time.sleep(5)
    return 5


try:
    aaa = test()
except Exception as e:
    print("出现异常，结束进程")
    print(e)

print("哈哈哈哈哈")

if __name__ == '__main__':
    test()