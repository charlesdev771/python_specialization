from flask import Flask, redirect, url_for, request, abort, make_response, session
import os
from werkzeug.utils import secure_filename
from flask import render_template
from json import dumps

#static_folder='public'
app = Flask(__name__, template_folder='templates')

app.secret_key = '777'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/indexMain', methods=['GET', 'POST'])
def indexMain():
    username = None
    if 'username' in session:
        username = session['username']
    return render_template('loginNovo.html', username=username)

@app.route('/loginNovo', methods=['GET', 'POST'])
def loginNovo():
    if request.method == 'POST' and request.form['username' != '']:
        session[username] = request.form['username']
        return redirect(url_for('indexMain'))
    return render_template('')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/notas')
def notas():
    return render_template('notas.html')

@app.route('/calculo', methods=['GET', 'POST'])
def calculo():
    total = request.form.to_dict().values()
    return str(total)


def teste():
    return '<h1>Ola</h1>'
app.add_url_rule('/teste', 'teste', teste)




@app.route('/games')
@app.route('/games/<nome>')
def games(nome = ''):
    return '<h1>Xvideos para {}</h1>'.format(nome)

@app.route('/blog/<int:post>')
def blog(post):
    if post > 0:

        return 'tal post {}'.format(post)
    else:
        return 'Blog'


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == 'POST':
        return '<h1>Success {} {} </h1>'.format(request.form['teste'], request.form['teste2'])
        #return dumps(request.form)
        '''
        t1 = request.args.to_dict()
        t2 = dict(request.args)
        return json.dumps([t1['teste'],t2['teste2']])
        '''
    else:
        return 'JOOJ'


@app.route('/blogNovo/<name>', methods=["POST", "GET"])
def blogNovo(name):
    if name == 'admin':
        return '<h1> Ola admin {} Como vai?'.format(name)
    else:
        return redirect(url_for('games', name = name))

@app.route('/google', methods=['GET', 'POST'])
def google():
    return redirect('https://google.com')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['teste'] == 'admin' and request.form['teste2'] == '12345':
            return redirect(url_for('google'), code=302)
        else:
            abort(401)
    else:
        abort(403)

@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    return  render_template('cookie.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        data = request.form['c']
        print(data)

    resp = make_response(render_template('setcookie.html'))
    resp.set_cookie('testecookie', data)
    return resp

@app.route('/getcookie', methods=['GET', 'POST'])
def getcookie():
    cookieName = request.cookie.get('testecookie')
    return '<h1> cookie {} </h1>'.format(cookieName)


@app.route('/uploadSite', methods=['GET', 'POST'])
def uploadSite():
    return render_template('upload.html')
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return 'Upload feito :)'






UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')








if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='777')
