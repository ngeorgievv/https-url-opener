from flask import request, Flask, redirect, url_for, render_template
import webbrowser


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urls = request.form.get('urls')
        url_list = urls.split('\n')
        for url in url_list:
            webbrowser.open(f'https://{url.strip()}')
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

