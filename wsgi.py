from app import app, socketio


# funicorn and wsgi (web server getway interface ) are both components used in deploying and serving python web applications ,particularly those built with web frameworks like flask and django

if __name__ =="__main__":
  socketio.run(app)

