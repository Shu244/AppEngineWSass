from setuptools import setup, find_packages

setup(
    name='AppEngineWSass-shu244',
    version='0.1.0',
    author="Shuhao Lai",
    author_email="Shuhaolai18@gmail.com",
    description="A small web app with SASS deployed to App Engine package.",
    packages=find_packages(include=['myapp', 'myapp.*']),
    install_requires=['flask'],
    scripts=['myapp/main.py'],  # Allows us to call "main.py" to launch app
    entry_points={'console_scripts': ['run-app=myapp.main:main']},  # Allows us to call run-app to run the web app
    setup_requires=['libsass >= 0.6.0'],
    sass_manifests={
        'myapp': ('static/sass', 'static/css', '/static/css')
    }
)