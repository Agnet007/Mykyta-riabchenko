import UI
class ConsoleUI(UI):
  def __init__(self):
    inputs = {}
  def listen(self):
    while 1:
      command = input("Input > ")
      if command in self.inputs:
        self.inputs[command]()
