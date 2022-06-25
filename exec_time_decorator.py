import time
from functools import wraps, partial


def exec_time(f=None, *, measure='time', precision=3):
   """Decorator for function execution time measurement"""

   if f is None:
      return partial(exec_time, measure=measure, precision=precision)

   if measure == 'time':
      time_func = time.time
   elif measure == 'cpu':
      time_func = time.process_time
   else:
      time_func = time.time
      print('[exec_time] wrong measurement value, using default')


   @wraps(f)
   def wrap(*args, **kw):
      ts = time_func()
      result = f(*args, **kw)
      te = time_func()

      print('   * func: {fname} | exec time{cpu}: {time} ms'.format
            (fname=f.__name__, cpu=' (CPU)' if measure=='cpu' else '', time=round((te-ts)*1000, precision)))

      return result
   return wrap
   
