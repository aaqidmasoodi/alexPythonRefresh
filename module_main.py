# where we will be importing out module "module_my"
import module_my  # importing a module by name
# Importing modules always runs it ... all of it
from module_my import PI
'''
in this import the entire module i.e module_my is still run
but you will only be able to access the only PI nothing else.
'''

from module_my import *  # like java use can use the * to import everthing \
# and you would not have to use the module
# but this method is not encourage

# print(PI)
# add(4, 6)

# print(module_my.PI)
# module_my.add(5, 6)
