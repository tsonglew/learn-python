# -*- coding: utf-8 -*-


# * for positional parameter
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4))

import html

# ** for keyword parameter, attrs is a dict
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
            name=name,
            attrs=attr_str,
            value=html.escape(value))
    return element

def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)

# * parameter should be the last but one
# ** parameter should be the last one
