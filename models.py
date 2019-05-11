from app import db, ma

class User(db.Model):
    user_id = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    pseudo = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class UserSchema(ma.ModelSchema):
        class Meta:
            model = User

# class Video(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     # src = db.column(db.String(50))
#     created_at = db.Column(db.DateTime)
#     view = db.Column(db.Integer)
#     enbabled = db.Column(db.Boolean)
#     user = db.Column(db.String(50), nullable=False)
# DEFINE FORMAT COLUMN / MULTIPLE VALUES