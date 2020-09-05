class Queue:
    
    def __init__(self, lists = None):
        self.lists = [] if lists == None else lists
    
    def enqueue(self, item):
        self.lists.append(item)
    
    def dequeue(self):
        return self.lists.pop(0) if not self.isEmpty() else -1

    def isEmpty(self):
        return self.lists == []
    
    def size(self):
        return len(self.lists)

    def __str__(self):
        if self.size() > 0:
            return str(self.lists)
        else:
            return 'Empty'


text_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_lower = text_upper.lower()

def encodemsg(q1, q2):
    for i in range(q1.size()):
        shift = q2.dequeue()
        chrmsg = q1.dequeue()
        q2.enqueue(shift)
        q1.enqueue(text_upper[(ord(chrmsg) - ord('A')) + (-26 + shift)] if ord(chrmsg) < ord('Z') else text_lower[(ord(chrmsg) - ord('a')) + (-26 + shift)])
    if q1.size() > q2.size() and q1.size() % q2.size() != 0 or q2.size() > q1.size() and q2.size() % q1.size() != 0:
        q2.enqueue(q2.dequeue())
    print(f'Encode message is :  {q1}')

def decodemsg(q1, q2):
    for i in range(q1.size()):
        shift = q2.dequeue()
        chrmsg = q1.dequeue()
        q2.enqueue(shift)
        q1.enqueue(text_upper[(ord(chrmsg) - ord('A')) - shift] if ord(chrmsg) < ord('Z') else text_lower[(ord(chrmsg) - ord('a')) - shift])
    q2.enqueue(q2.dequeue())
    print(f'Decode message is :  {q1}')

if __name__ == "__main__":
    n = input('Enter String and Code : ').split(',')
    q1 = Queue([i for i in n[0] if i != ' '])
    q2 = Queue([int(i) for i in n[1]])
    encodemsg(q1, q2)
    decodemsg(q1, q2)