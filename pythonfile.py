import antigravity

from django.contrib.auth.models import User

from lists.stuff import things

class Klassey(things.Thing):

    def method1(self):
        return 1

    def method2(self, b):
        # do things
        return b + 2

