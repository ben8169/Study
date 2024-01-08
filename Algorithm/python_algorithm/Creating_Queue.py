import queue


Q = queue.Queue(maxsize=10)
S = queue.LifoQueue(maxsize=10)


for i in range(1, 11):
    Q.put(i)
    S.put(i)

print("Queue: ", Q.queue)
print("LifoQueue: ", S.queue)

Q.get()
S.get()

print("Queue: ", Q.queue)
print("LifoQueue: ", S.queue)