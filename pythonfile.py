import antigravity

from django.contrib.auth.models import User

from lists.stuff import things

class Klassey(things.Thing):

    def method2(self, b):
        # do things
        return b + 2

class NuKlass(object):

    def method1(self):
        # amend method 1
        # it's a litltle longer
        a = 2
        a = a + 3
        b = a
        return 2

