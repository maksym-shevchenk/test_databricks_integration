def func_1_1():
    print('func_1_1')
    return 1.1

def func_1_2(a='defaul arg'):
    print('func_1_2', f'{a=}')
    return a

if __name__=='__main__':
    func_1_1()
    func_1_2()
    func_1_2(12345)