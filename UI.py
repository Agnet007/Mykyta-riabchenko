import abc
class UI():
  @abc.abstractmethod
  def listen(self): pass
  @abc.abstractmethod
  def addInputhMethod(self, props, func): pass
  @abc.abstractmethod
  def show(self, data : str): pass
  
