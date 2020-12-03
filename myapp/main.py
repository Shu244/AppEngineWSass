from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware


app = Flask(__name__)
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    __name__ : ('static/sass', 'static/css', '/static/css')
})


@app.route('/')
def hello_world():
    return render_template('index.html', msg='HELLO Ryan, Laura, or PengXi!')


def main():
    app.run()


if __name__ == '__main__':
    main()
