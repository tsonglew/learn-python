import datetime as dt
from marshmallow import Schema, fields, pprint

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


if __name__ == '__main__':
    user = User(name='Kasheem', email='kasheem@python.com')
    schema = UserSchema()
    # USAGE OF ONLY PARAMETER
    # summary_schema = UserSchema(only=('name', 'email'))
    result = schema.dump(user)
    pprint(result.data)
    # pprint(json_result.data)

    #COLLECTIONS
    user1 = User(name='Mick', email='mick@python.com')
    user2 = User(name='Keith', email='keith@stones.com')
    users = [user1, user2]
    schema = UserSchema(many=True)
    result = schema.dump(users)
    pprint(result.data)
