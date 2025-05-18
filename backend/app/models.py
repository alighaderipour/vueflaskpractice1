from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    family = db.Column(db.String(33), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'family': self.family
        }