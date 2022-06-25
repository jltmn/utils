from functools import wraps
import os
import inspect
from types import FrameType
from typing import cast


def who_called_me(f):
   """Gets who called this function"""

   @wraps(f)
   def wrap(*args, **kw):
      fcode = cast(FrameType, cast(
            FrameType, inspect.currentframe()).f_back).f_code
      func = fcode.co_name
      filepath = fcode.co_filename
      rel_path = os.path.relpath(filepath)
      lineno = fcode.co_firstlineno

      print('   * func: {fname} | called from: {caller} [{p} : {line}]'.format
            (fname=f.__name__, caller=func, p=rel_path, line=lineno))

      return f(*args, **kw)
   return wrap
