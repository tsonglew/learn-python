from marshmallow import pprint
from test import UserSchema

user_data = {
        'created_at': '2016-07-07T05:26:03.869245',
        'email': u'kasheem@python.com',
        'name': u'Kasheem'
        }

schema = UserSchema()
result = schema.load(user_data)
pprint(result.data)
