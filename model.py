"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincremnt=True,
                        primary_key=True)
    
    email = db.Column(db.String, unique=True, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Represents User Object"""
        return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.model):
    """A Movie""""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    def __repr__(self):
        """Represents Movie Object"""

        return f'<Movie movie_id={self.movie_id} title={self.title} release_date={self.release_date}>'

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
