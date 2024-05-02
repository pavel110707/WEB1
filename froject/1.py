from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/python')
def python():
    return render_template('python.html')


@app.route('/html')
def html():
    return render_template('html.html')


@app.route('/javascript')
def javascript():
    return render_template('javascript.html')


@app.route('/css')
def css():
    return render_template('css.html')


@app.route('/html1')
def html1():
    return render_template('html1.html')


@app.route('/html2')
def html2():
    return render_template('html2.html')


@app.route('/html3')
def html3():
    return render_template('html3.html')


@app.route('/css1')
def css1():
    return render_template('css1.html')


@app.route('/css2')
def css2():
    return render_template('css2.html')


@app.route('/python_1')
def python_1():
    return render_template('python_1.html')


@app.route('/javascript1')
def javascript1():
    return render_template('javascript1.html')


@app.route('/entered')
def entered():
    return render_template('entered.html')


@app.route('/l1', methods=["GET", "POST"])
def l1():
    ot = ''
    if request.method == "POST":
        text_id = request.form['text1']
        if text_id == 'print("ПРИВЕТ, МИР!")' or text_id == "print('ПРИВЕТ, МИР!')":
            ot = 'Правильно'
        else:
            ot = 'Неверно'
    return render_template('l1.html', tekest=ot)


@app.route('/l2', methods=["GET", "POST"])
def l2():
    ot = ''
    if request.method == "POST":
        text_id = request.form['text2']
        if text_id == 'a = 2' or text_id == 'a=2':
            ot = 'Правильно'
        else:
            ot = 'Неверно'
    return render_template('l2.html', tekst=ot)


@app.route('/l3', methods=["GET", "POST"])
def l3():
    ot = ''
    if request.method == "POST":
        text_id = request.form['text3']
        if text_id == 'print(input())':
            ot = 'Правильно'
        else:
            ot = 'Неверно'
    return render_template('l3.html', takst=ot)


if __name__ == '__main__':
    app.run(debug=True)
