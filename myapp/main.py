import argparse
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', msg='Hello, my name is Shuhao!')


def main():
    parser = argparse.ArgumentParser(description='Processing cmd args for web app')
    parser.add_argument('--dev', action='store_true', help='Developer mode.')
    args = parser.parse_args()

    if args.dev:
        from sassutils.wsgi import SassMiddleware

        app.wsgi_app = SassMiddleware(app.wsgi_app, {
            'myapp' : ('static/sass', 'static/css', '/static/css')
        })

    app.run()


if __name__ == '__main__':
    main()
