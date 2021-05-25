from flask_sqlalchemy import SQLAlchemy
from app import db





class projecttopic(db.Model):
    __tablename__ = 'projecttopic'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String())
    project = db.Column(db.String())
    createdon = db.Column(db.DateTime)
    # compdatetime = db.Column(db.DateTime)

    def __init__(self, topic, project,createdon):
        self.topic = topic
        self.project = project
        self.createdon = createdon
        # self.compdatetime = compdatetime

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'project': self.project,
            'createdon':self.createdon,
            #  'compdatetime':self.compdatetime,
        }


# class todolog(db.Model):
#     __tablename__ = 'todolog'

#     id = db.Column(db.Integer, primary_key=True)
#     log = db.Column(db.String())
#     textid =  db.Column(db.Integer, db.ForeignKey('todo.id'), nullable=False)
#     createdon = db.Column(db.DateTime)

#     def __init__(self, textid, log,createdon, compdatetime):
#         self.textid = textid
#         self.log = log
#         self.createdon = createdon


#     def __repr__(self):
#         return '<id {}>'.format(self.id)

#     def serialize(self):
#         return {
#             'id': self.id,
#             'textid': self.textid,
#             'log': self.log,
#             'createdon':self.createdon,

#         }

# class todolog(db.Model):
#     __tablename__ = 'todolog'

#     id = db.Column(db.Integer, primary_key=True)
#     log = db.Column(db.String())
#     text =  db.Column(db.String())
#     createdon = db.Column(db.DateTime)

#     def __init__(self, text, log,createdon):
#         self.text = text
#         self.log = log
#         self.createdon = createdon


#     def __repr__(self):
#         return '<id {}>'.format(self.id)

#     def serialize(self):
#         return {
#             'id': self.id,
#             'text': self.text,
#             'log': self.log,
#             'createdon':self.createdon,

#         }

