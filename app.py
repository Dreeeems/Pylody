from flask import Flask, render_template, request, url_for, redirect
from db.model import db, Music
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  
app.config['UPLOAD_FOLDER_IMAGES'] = 'static/images'
app.config['UPLOAD_FOLDER_AUDIO'] = 'static/audio'
app.config['ALLOWED_EXTENSIONS_IMAGES'] = {'jpg', 'jpeg', 'png', 'gif', 'webp'}
app.config['ALLOWED_EXTENSIONS_AUDIO'] = {'mp3', 'wav', 'ogg'}


db.init_app(app)

def allowed_file(filename, file_type):
    print(filename,file_type)
    if file_type == 'image':
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS_IMAGES']
    elif file_type == 'audio':
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS_AUDIO']
    return False

def save_file(file, file_type):
    if file:
        print(f"File {file_type} received : {file.filename}")
        if file_type == 'image':
            if allowed_file(file.filename, 'image'):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename))
                return filename
        elif file_type == 'audio':
            if allowed_file(file.filename, 'audio'):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER_AUDIO'], filename))
                return filename
    print(f"No file {file_type} found.")
    return None

def delete_file(file,file_type):
    if file:
            if file_type =="image":
             os.remove("./static/"+file)
            if file_type == "audio":
             os.remove("./static/"+file)

    else :
        return "No file",404
        

        

@app.route('/')
def home():
    musics = Music.query.all()
    return render_template('home.html', musics=musics)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        artist = request.form.get("artist")
        image = request.files.get("image")  
        song = request.files.get("music")
        image_filename = save_file(image, 'image')
        song_filename = save_file(song, 'audio')

        if image_filename and song_filename:
            new_music = Music(
                name=name,
                artist=artist,
                image=f"images/{image_filename}",
                song=f"audio/{song_filename}"
            )
            db.session.add(new_music)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "Error during Upload", 400
    else:
        return render_template('add_music.html')
    

@app.route('/delete/<int:id>',methods=["POST"])
def remove(id):
    
    
    removed_music = Music.query.filter_by(id=id).first()
    print(removed_music)
    if removed_music is None:
        return "Music not found",404
    delete_file(removed_music.image,"image")
    delete_file(removed_music.song,"audio")
    db.session.delete(removed_music)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get('query')
    if query:
         musics = Music.query.filter(
            Music.name.like(f'%{query}%') | Music.artist.like(f'%{query}%')
        ).all()
         return render_template('home.html', musics=musics)
    else:
        musics = []
        return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
        app.run(debug=True)

