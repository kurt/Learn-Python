import Queue as Q


def test1():
    q = Q.Queue(1)
    res = q.empty()
    if not res:
        print("Test 1 Failed")
        return
    res = q.enqueue(10)
    if not res:
        print("Test 1 Failed")
        return
    x = q.dequeue()
    if x != 10:
        print("Test 1 Failed")
        return
    res = q.empty()
    if not res:
        print("Test 1 Failed")
        return
    print("Test 1 OK!")

def test2():
    # This tests to make sure the queue does not store more than allowed
    q = Q.Queue(1)
    res = q.empty()
    if not res:
        print("Test 2 Failed - a")
        return
    res = q.enqueue(10)
    if not res:
        print("Test 2 Failed - b")
        return
    res = q.enqueue(12)
    res = q.enqueue(12)
    res = q.enqueue(23)
    a = q.dequeue()
    b = q.dequeue()
    c = q.dequeue()
    if a == 23 and b == 12 and c == 12:
        print("Test 2 Failed - c")
        return
    if a != 10:
        print("Test 2 Failed - d")
    print("Test 2 OK!")


# Call Tests
test1()
test2()
