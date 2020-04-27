import threading
import time


def target(second):
    # 线程的名字就是通过threading.current_thread().name获得，主线程的名字为MainThreat，子线程的名字为Thread-num
    print(f'threat {threading.current_thread().name} is running')
    print(f'threat {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'threat {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is running')
for i in [1, 5]:
    # 使用threading.Tread()类新建了两个线程，target参数就是刚才定义的target函数，args通过列表的形式传递
    thread = threading.Thread(target=target, args=[i])
    # 新建线程声明之后，使用start()方法即可开始线程的运行
    thread.start()
print(f'Threading {threading.current_thread().name} is ended')

threads = []
for i in [1, 5]:
    thread = threading.Thread(target=target, args=[i])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
