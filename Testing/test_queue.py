import Queue as Q
import sys

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

def fill_queue(q):
    for i in range(q.max):
        q.enqueue(i)
    return q
 

# Call Tests
test1()
test2()
q = Q.Queue(100)
qb = fill_queue(q)
q2 = Q.Queue(1)

print("Q of 100 elems",sys.getsizeof(qb))
print("Q of 1 elem",sys.getsizeof(q2))
# print the elements of qb
for i in range(qb.max):
    print(qb.dequeue())

