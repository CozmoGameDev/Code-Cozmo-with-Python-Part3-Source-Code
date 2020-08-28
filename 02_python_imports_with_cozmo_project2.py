# This project will make show us how imports can be used with Cozmo
# Language:Python


import cozmo
import sys
import time


def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(4.2)
    a = input("Type in something for cozmo to say(expect Nothing):")
    if a == "Nothing":
        sys.exit('"Nothing" is not an option')
    else:
        robot.say_text(a).wait_for_completed()
    time.sleep(3)
    print("SDK Program completed. No need of keeping it running")
    time.sleep(2)
    print("Shutting down connection...")
    time.sleep(2.5)
    sys.exit("Connection shutdown!")


cozmo.run_program(cozmo_program)
