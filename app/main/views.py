from . import main

@main.route('/')
def index():
  return '<h1>Welcome Flasker<h1>'
