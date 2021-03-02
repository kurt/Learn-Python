import unittest
import Queue as Q

 
# other things to do: initialize one queue and pass to each test method. Also see the size of memory of a Queue and speed of tests

class TestCase(unittest.TestCase):
    def setUp(self):
        self.q = Q.Queue(1)
        res = self.q.empty()
        assert res

    def testInsert(self):
        res = self.q.enqueue(10)
        self.assertEqual(self.q.data[0], 10)

    def testSize(self):
        q = Q.Queue(2)
        q.enqueue(1)
        q.enqueue(1)
        self.assertEqual(q.size , 2)

    def testMaxSize(self):
        q= Q.Queue(100)
        self.assertEqual(q.max, 100)

    @unittest.expectedFailure
    def testInitialFail(self):
        q= Q.Queue(-7)        

    @unittest.expectedFailure
    def testCreateVoid(self):
        q = Q.Queue(0) 

    def testDequeue(self):
        q = Q.Queue(4)
        q.enqueue(11)
        result = q.dequeue()
        self.assertEqual(11, result)
    
    def testInsertFull(self):
        self.q.enqueue(10)
        res = self.q.enqueue(22)
        self.assertEqual(res, False)
        res = self.q.dequeue()
        self.assertEqual(res, 10)

    def testDeleteEmpty(self):
        res = self.q.dequeue()
        self.assertEqual(res, None)

    def testEmpty(self):
        res = self.q.empty()  
        self.assertEqual(res, True)

    def testFull(self):
        self.q.enqueue(202)
        res = self.q.full()  
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()
