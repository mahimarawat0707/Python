class Student:
  @staticmethod #decorator - allows us to wrap another function in order to extend the behaviour of the wrapped function, without permenently modyfing it.

  def hello():
    print("ABC College")

s1 = Student()
s1.hello()

