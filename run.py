from flaskblog import create_app
'''
    module that starts the gist application
'''

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
