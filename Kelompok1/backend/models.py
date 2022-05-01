from settings import *
import datetime
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def json(self):
        return {
            'id': self.id, 
            'title': self.title, 
            'description': self.description, 
            'author': self.author, 
            'content': self.content,
            'thumbnail': request.host + '/api/uploads/' + self.thumbnail,
            'createdAt': self.created_at,
            'modifiedAt': self.modified_at
        }
    
    def add_article(_title, _description, _author, _content, _thumbnail):
        new_article = Article(
            title=_title, 
            description=_description, 
            author=_author, 
            content=_content,
            thumbnail=_thumbnail,
            created_at=datetime.datetime.utcnow(),
            modified_at=datetime.datetime.utcnow()
        )

        db.session.add(new_article)
        db.session.commit()

    def get_all_article():
        return [Article.json(article) for article in Article.query.all()]
    
    def get_article(_id):
        return Article.json(Article.query.filter_by(id=_id).first())

    def update_article(_id, _title, _description, _author, _content, _thumbnail=None):
        article = Article.query.filter_by(id=_id).first()
        article.title = _title
        article.description = _description
        article.author = _author
        article.content = _content
        article.modified_at = datetime.datetime.utcnow()

        if _thumbnail:
            article.thumbnail = _thumbnail
            
        db.session.commit()
    
    def delete_article(_id):
        Article.query.filter_by(id=_id).delete()
        db.session.commit()


# Upload ----------------------------------------------------------------

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return 

def upload_image(img_file):
    img_name = secure_filename(img_file.filename)
    create_new_folder(app.config['UPLOAD_FOLDER'])
    saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    app.logger.info("saving {}".format(saved_path))
    img_file.save(saved_path)
    return img_name