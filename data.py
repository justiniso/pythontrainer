from __future__ import print_function

import collections  # Container or Sized
import inspect  # getdoc
import keyword
import numbers  # Number
import pkgutil
import pydoc_data.topics


if not isinstance(__builtins__, dict):
    __builtins__ = vars(__builtins__)

DATA = {}
DATA['functions'] = dict((k, inspect.getdoc(v)) for k, v in __builtins__.items()
                         if k[0].islower()
                         and k not in ('copyright', 'credits', 'license'))

DATA['datatypes'] = dict(('{0}.{1}'.format(k, attr), inspect.getdoc(method))
                         for k, v in __builtins__.items()
                         if isinstance(v, type) and
                         issubclass(v, (collections.Sized, numbers.Number))
                         # if k[0].islower() and (hasattr(v, '__len__')
                         #                      or hasattr(v, '__bool__'))
                         for attr, method in vars(v).items()
                         if attr[0].islower())
DATA['keywords'] = dict((k, pydoc_data.topics.topics[k])
                        for k in set(keyword.kwlist) & set(pydoc_data.topics.topics))

DATA['exceptions'] = dict((k, v) for k, v in __builtins__.items()
                          if k[0].isupper()
                          and type(v) == type
                          and issubclass(v, BaseException))
DATA['modules'] = [i[1] for i in pkgutil.iter_modules()
                   if i[1][0] != '_']


def main():
    import pprint
    pprint.pprint(DATA['keywords'])


if __name__ == '__main__':
    main()
