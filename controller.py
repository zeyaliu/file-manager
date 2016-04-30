from flask import Flask, session, redirect, url_for, request, render_template, send_file
from os import listdir
from os.path import isfile, join
import os
from werkzeug.utils import secure_filename
from flask.ext.bootstrap import Bootstrap
from pymediainfo import MediaInfo


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'mxcvjnjd';
bootstrap = Bootstrap(app)


def index():
    session['username']=''
    session['massege']=''
    return render_template('main.html')


def signup():
    if request.form['username'] == '' :
        return redirect(url_for('index'))
    elif request.form['username'] != 'kassey' or request.form['password'] != '111':
        session['message'] = 'The username or password may not correct, please login again..'
        return render_template('main.html', message=session['message'])
    else:
        session['username'] = request.form['username']
        return redirect(url_for('feedback'))


def feedback():
    filelist = [f for f in listdir('/Users/kassey/Downloads/file--manager/static/Uploads') if isfile(join('/Users/kassey/Downloads/file--manager/static/Uploads', f))]
    return render_template('uplfile.html', username=session['username'], list=filelist)


def uplfile():
    filelist = [f for f in listdir('/Users/kassey/Downloads/file--manager/static/Uploads') if isfile(join('/Users/kassey/Downloads/file--manager/static/Uploads', f))]
    if request.method == 'GET':
        return render_template('uplfile.html', list=filelist)
    elif request.method == 'POST':
        f = request.files['file']
        infom=request.files['file'].read()
        type=f.content_type
        name=secure_filename(f.filename)
        print type
        print len(infom)
        print name
        file_name = secure_filename(f.filename)

        f.save(os.path.join('/Users/kassey/Downloads/file--manager/static/Uploads', file_name))
        return redirect(url_for('uplfile'))


def file():
    return send_file(request.args['files'])


