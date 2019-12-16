from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/main')
def main():
    return 'Main page'

@app.route('/search')
def search():
    return '''
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" type="text/css" href="choccy-styles.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Chocolatey Goodness</title>
    </head>
    <body>
    {% block content %}
    <h1>Search for chocolate!</h1>
    <p>Search our extensive database below</p>
    <form class="example" action="action_page.php">
     <input type="text" placeholder="Search.." name="search">
    <button type="submit"><i class="fa fa-search"></i></button>
    </form>
    {% endblock %}
    </body>
    </html>
    
    '''

@app.route('/about')
def about():
    return 'About us'

if __name__ == '__main__' :
    app.run()