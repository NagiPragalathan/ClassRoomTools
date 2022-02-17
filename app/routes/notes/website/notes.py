from flask import Blueprint, render_template
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

from . import notes
from .DocToHtml import convert

UPLOAD_FOLDER : str = "E:/_Projects/ClassRoomTools/app/temp"
DocxTohtlm = "E:/_Projects/ClassRoomTools/app/templates/public/"

ALLOWED_EXTENSIONS  = {'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#blueprints
notes = Blueprint("notes", __name__)
@notes.route('/')
def index():
    return render_template("notes/WebMenu.html.j2",Title = "example")


@notes.route('/check', methods=['GET', 'POST'])
def upload_file():
    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    if (request.method == 'POST'):
        if ('file' not in request.files):
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        path_ = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            file.save(path_)
            output = DocxTohtlm+filename.rsplit('.', 1)[0].lower() +".html"
            Doctohtml = convert(path_,output)
            os.remove(path_)
            return render_template(f"public/{filename.rsplit('.', 1)[0].lower() +'.html'}")
        
    return render_template("notes/UplodeDocx.html")