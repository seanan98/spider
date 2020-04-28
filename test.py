from multiprocessing import Process, Semaphore, Lock, Queue
import time

buffer = Queue(10)    # 定义一个共享队列
empty = Semaphore(2)  # 定义信号量，代表缓冲区空余数
full = Semaphore(0)   # 定义信号量，代表缓冲区占用数
lock = Lock()


class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()  # 使用acquire 占用一个缓冲区位置，缓冲区空余数减一
            lock.acquire()  # 加锁
            buffer.get()   # 对缓冲区进行操作
            print('Consumer pop an element')
            time.sleep(1)
            lock.release()  # 释放锁
            empty.release()


class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            empty.acquire()
            lock.acquire()
            buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            lock.release()
            full.release()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
