import threading
def cal_fun(n):
    print("thread",n)
    #t1=threading.thread(target=function,args(arg))
t1 = threading.Thread(target=cal_fun,args=(10,))
t1.start()
