class Mixin(object):
    pass

def register(cls):
    return type(
            cls.__name__,
            (Mixin, cls),
            {}
            )

class View(object):
    def method(self):
        print "method() from View()"

@register
class ChildView(View):
    def method(self):
        super(ChildView, self).method()
