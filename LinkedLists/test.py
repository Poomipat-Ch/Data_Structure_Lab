from LinkedList import LinkedList


if __name__ == "__main__":
    ll = LinkedList()
    ll.append('A')
    ll.append('B')
    ll.append('C')
    print(ll)
    print(ll.removeHead().data)
    print(ll.size())
    ll.addHead('A')
    print(ll)
    print(ll.size())
    print(ll.isIn('A'))
