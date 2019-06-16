from flask import Flask


def return_bars_page():
    with open('bars.html') as html_file:
        return html_file.read()


app = Flask(__name__)
app.add_url_rule('/', 'Nearest Bars to You', return_bars_page)
app.run('0.0.0.0')
