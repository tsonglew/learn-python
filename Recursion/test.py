class View(object):
    def method(self):
        pass

class ChildView(View):
    def method(self):
        super(ChildView, self).method()

class Mixin(object):
    pass

def register(cls):
    return type(
            'DecoratedView',
            (Mixin, cls),
            {}
            )
