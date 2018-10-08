import threading
import tensorflow as tf
import numpy as np
import time

def MyLoop(coord, worker_id):
    while not coord.should_stop():
        if np.random.rand() < 0.1:
            print("Stoping from id: %d\n" % worker_id)
            coord.request_stop()
        else:
            print("Working on id: %d\n" % worker_id)
        time.sleep(1)

coord = tf.train.Coordinator()

threads = [threading.Thread(target=MyLoop, args=(coord, i)) for i in range(5)]
for t in threads:
    t.start()
coord.join(threads)

# import time
# import threading
#
# # 假定这是你的银行存款:
# balance = 0
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
