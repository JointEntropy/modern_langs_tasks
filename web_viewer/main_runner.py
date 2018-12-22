from flask import Flask
from parse_methods import page_images
from flask import request, render_template
import db_acc
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
app.config['DEBUG'] = False

def  validate_url(url):
    # https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet
    # https://stackoverflow.com/questions/28767896/how-do-i-catch-javascript-code-injection-in-url-using-python
    # на самом деле все очень сложно
    if url:
        return True
    return True

def relative_path(url):
    #return not bool(urlparse(url).netloc)
    if url.startswith('/'):
        return True
    return False

@app.route('/', methods=['GET' ,'POST'])
def main_viewer():
    url = request.args.get('url')
    if validate_url(url):
        if url and url not in db_acc.get_all_sites():
            images = [urljoin(url, img_url) if relative_path(img_url) else img_url for img_url in page_images(url)]
            images = [img for img in images if validate_url(img)]
            db_acc.add_site_data(url, images)
    else:
        url = None
    images = db_acc.get_images(url)  # если url пустой, то выведёт все что в базе, иначе выведет ток по сайту
    result = render_template('index.html', images=images)
    return result


@app.route('/any/', methods=['GET'])
def injection_page():
    url = request.args.get('url')
    result = render_template('inject.html', url=url)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')
