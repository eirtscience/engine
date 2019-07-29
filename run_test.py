import unittest

import run

class RunTest(unittest.TestCase):
    def test_run_script(self):
        self.assertTrue(run.run_script(),True)

    def test_calculate(self):
        self.assertEqual(run.calculate(3,6),9)
        self.assertEqual(run.calculate(3,4),7)
        self.assertEqual(run.calculate(7,10),17)




if __name__=="__main__":
    unittest.main()
