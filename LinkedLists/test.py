from LinkedList import LinkedList


if __name__ == "__main__":
    ll = LinkedList()
    ll.append('A')
    print(ll.isIn('A'))
    ll.append("B")
    print(ll)
    ll.insertAfter(0, 'EE')
    print(ll)
    ll.deleteAfter(0)
    print(ll)