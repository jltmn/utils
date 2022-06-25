from functools import wraps


def debug(f):
   """Print the function params and return value"""

   @wraps(f)
   def wrap(*args, **kwargs):
      args_repr = [repr(a) for a in args]
      kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
      signature = ", ".join(args_repr + kwargs_repr)

      result = f(*args, **kwargs)

      print(f'   * func: {f.__name__} | args= ({signature}), return= {result}')

      return result
   return wrap
