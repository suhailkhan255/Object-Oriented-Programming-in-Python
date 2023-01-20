"""Duck typing is not a feature of any programming lang
it is a concept Which can be applied on any Dynamic language"""


class Duck:
    def talk(self):
        print("Quack Quack")
class Human:
    def talk(self):
        print("hi ")

def callTalk(obj):
    obj.talk()

d=Duck()
callTalk(d)

h= Human()
callTalk(h)