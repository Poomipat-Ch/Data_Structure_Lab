from Queue import Queue


if __name__ == "__main__":
    q = Queue(['A','B','C','D'])
    for i in range(q.size()+1):
        print(q.dequeue())