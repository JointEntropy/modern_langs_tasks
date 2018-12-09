from flask import Flask
from parse_methods import page_images
from flask import request, render_template


app = Flask(__name__)
app.config['DEBUG'] = False




@app.route('/', methods=['GET' ,'POST'])
def main_viewer():
    url = request.args.get('url')
    images = [(img_url if img_url.startswith('http') else (url+'/'+img_url) ) for img_url in page_images(url)] if url else None
    with open('images.log','w') as f:
        f.write('\n'.join(images))
    result = render_template('index.html', original_url=url, images=images)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
