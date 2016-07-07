from marshmallow import Schema, fields, post_load
from test import User

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)


if __name__ == '__main__':
    user_data = {
            'name': 'Kasheem',
            'email': 'kasheem@python.com'
            }
    shcema = UserSchema()
    result = shcema.load(user_data)
    print result.data
