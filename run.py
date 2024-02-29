'''
    module that starts the gist application
'''
from flaskblog import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
