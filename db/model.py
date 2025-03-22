from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=True)
    song = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Music {self.name}>'
