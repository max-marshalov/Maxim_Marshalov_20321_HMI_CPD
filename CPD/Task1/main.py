##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 4:26:01 pm
 # @copyright SMTU
 #
import asyncio
from views.App import App
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = App(loop)
    try:
        loop.run_forever()
    except Exception as e:
        loop.close()
        print(e)
