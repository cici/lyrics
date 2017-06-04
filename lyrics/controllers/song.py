from flask import Blueprint
from flask import render_template
from lyrics.models import Song, Writer, Performer

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

@main_blueprint.route("/")
def home():

    latest_songs = Song.query.order_by(
        Song.id.desc()
    ).limit(5).all()

    writerList = Writer.query.order_by(Writer.id.asc()).all()
    performerList = Performer.query.order_by(Performer.id.asc()).all()

    return render_template("index.html", 
                           song_list=latest_songs, 
                           writers=writerList, 
                           performers=performerList) 

@main_blueprint.route("/test")
def test():
    return render_template("test.html")
