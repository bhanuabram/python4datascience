# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:27:22 2023

@author: 902544749
"""

#__all__ = ['bar', 'baz']

waz = 5
bar = 10
def baz(): return 'baz'


# If the __all__ above is commented out,
# this code will then execute to completion,
# as the default behavior of import * is to
# import all symbols that do not begin with
# an underscore, from the given namespace.

# Reference: https://docs.python.org/tutorial/modules.html#importing-from-a-package

# NOTE: __all__ affects the from <module>
# import * behavior only. Members that are
# not mentioned in __all__ are still accessible
# from outside the module and can be imported
# with from <module> import <member>.