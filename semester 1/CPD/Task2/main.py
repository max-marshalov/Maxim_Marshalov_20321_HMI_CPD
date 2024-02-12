##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-04 10:42:00 am
 # @copyright SMTU
 #
from tests.TestRunner import TestRunner
from services.GameService import GameService
if __name__ == "__main__":
   testRunner = TestRunner()
   testRunner.run()
   game = GameService(10)
   game.run()
