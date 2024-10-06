import unittest
import runner_test, runner_and_tournament

generalTest = unittest.TestSuite()
generalTest.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
generalTest.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_and_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(generalTest)