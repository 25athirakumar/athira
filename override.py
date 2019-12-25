import time
class Robot:
    def action(self):
        time.sleep(1.0)
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        time.sleep(2.0)
        print('Hello world')

class DummyRobot(Robot):
    def start(self):
        time.sleep(1.5)
        print('Started.')

r = HelloRobot()
d = DummyRobot()

r.action()
d.action()
d.start()