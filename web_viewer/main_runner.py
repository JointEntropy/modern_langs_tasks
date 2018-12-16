from flask import Flask
from parse_methods import page_images
from flask import request, render_template
import db_acc

app = Flask(__name__)
app.config['DEBUG'] = False

def  validate_url(url):
    if url:
        return True

    return True

@app.route('/', methods=['GET' ,'POST'])
def main_viewer():
    url = request.args.get('url')
    if validate_url(url):
        if url and url not in db_acc.get_all_sites():
        images = [(img_url if img_url.startswith('http') else (url+'/'+img_url) ) for img_url in page_images(url)]
        images = [img for img in images if validate_url(img)]
        db_acc.add_site_data(url, images)
    else:
        url = None
    images = db_acc.get_images(url)  # если url пустой, то выведёт все что в базе, иначе выведет ток по сайту
    result = render_template('index.html', images=images)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')
