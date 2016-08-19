class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    print users
    print sorted(users, key=lambda u: u.user_id)

def sort_attrget():
    from operator import attrgetter
    # attrgetter could get more than one parameter
    print sorted(users, key=attrgetter('user_id'))

if __name__ == '__main__':
    users = [User(23), User(3), User(99)]
    sort_notcompare()
    sort_attrget()
