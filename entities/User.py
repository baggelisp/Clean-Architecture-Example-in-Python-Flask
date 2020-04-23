class User(object):

    def __init__(self, id, name, username, email, phone):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone

    @classmethod
    def from_dict(cls, adict):
        user = User(
            id=adict['id'],
            name=adict['name'],
            username=adict['username'],
            email=adict['email'],
            phone=adict['phone'],
        )

        return user

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def __repr__(self):
        return "%r" % (self.__dict__)

