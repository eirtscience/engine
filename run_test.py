import unittest

import run

class RunTest(unittest.TestCase):
    def test_run_script(self):
        self.assertTrue(run.run_script(),True)




if __name__=="__main__":
    unittest.main()
