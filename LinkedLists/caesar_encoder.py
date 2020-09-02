from LinkedList import LinkedList


text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encoder(data):
    ll_in = data
    ll_out = LinkedList()
    t = ll_in.removeHead()
    while t.next != None:
        ll_out.append(text[(ord(t.data) - 65) - 3])
        t = t.next
    ll_out.append(text[(ord(t.data) - 65) - 3])
    return ll_out

def decoder(data):
    ll_in = data
    ll_out = LinkedList()
    t = ll_in.removeHead()
    while t.next != None:
        ll_out.append(text[(ord(t.data) - 65) + 3 if ord(t.data) - 65 + 3 < len(text) else (ord(t.data) - 65) + 3 - len(text)])
        t = t.next
    ll_out.append(text[(ord(t.data) - 65) + 3])
    return ll_out




if __name__ == "__main__":
    inp = input("Enter Input : ")
    ll = LinkedList()
    for i in inp:
        ll.append(i)
    print("".join(str(encoder(ll)).split(',')))
    #print("".join(str(decoder(ll)).split(',')))

    