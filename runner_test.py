import unittest
from runner import Runner
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = Runner('tester')
        for k in range(10):
            obj.walk()
        # print('Суммарное расстояние равно', obj.distance)
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = Runner('testrunner')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj_w = Runner('oW')
        for i in range (10):
            obj_w.walk()

        obj_r = Runner('oR')
        for i in range(10):
            obj_r.run()
        self.assertNotEqual(obj_r.distance, obj_w.distance)


if __name__ == "__main__":
    unittest.main()

# m = RunnerTest()
