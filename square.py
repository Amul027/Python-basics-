daf(target=f_square,args=(5,))
        t1 = threading.thread(target=f_cube, args=(10,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()ef t_square(n)
    print("squre=",n*n)
    def f_cube(m):
        print("cub=",n*n*n)
        print("cub=",n*n*n*)
        t1 = threading.thre