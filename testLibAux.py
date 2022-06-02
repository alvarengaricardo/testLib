def line(a, b=""):
  #  s = str(type(a))
    return 'a: ' + str(a) + ' b: ' + str(b) + ' Result: '
   # return (s[8:-2]) + ': ' + str(a) + ' b: ' + str(b) + ' Result: '
   # return 'a: ' + str(a) + ' b: ' + str(b) + ' Result: '

def line2(ff, a, b, expected, received):
    return('Function: ' + str(ff.__name__) + ' a: ' + str(a) + ' b: ' + str(b) + ' expected: ' + str(
        expected) + ' received: ' + str(received) + ' Result: ')