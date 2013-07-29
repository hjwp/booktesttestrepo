import antigravity

from django.contrib.auth.models import User

from lists.stuff import things

class Klassey(things.Thing):

    def method1(self):
        # amend method 1
        return 2

    def method2(self, b):
        # do things
        return b + 2

