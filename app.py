from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymusic.db'
db = SQLAlchemy(app)


# music_list = [
#     {
#         "id": 1,
#         "music_title": "roi manitou",
#         "music_artist": "fally ipupa",
#         "music_image": "/static/images/fally-ipupa.jpeg"
#     },
#     {
#         "id": 2,
#         "music_title": "skol mandra manda",
#         "music_artist": "koffi olomide",
#         "music_image": "/static/images/fally-ipupa.jpeg"
#     }
# ]


class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    album_image = db.Column(db.String, nullable=False)


@app.route('/')
def index():
    music_list = Music.query.all()
    return render_template('index.html', music_item=music_list)


@app.route('/add_music', methods=['POST', 'GET'])
def add_music():
    if request.method == "POST":
        title = request.form.get("title")
        artist = request.form.get("artist")
        album_image = request.form.get("album_image")

        new_music = Music(title=title, artist=artist, album_image=album_image)

        db.session.add(new_music)
        db.session.commit()
        
    return render_template('add_music.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
