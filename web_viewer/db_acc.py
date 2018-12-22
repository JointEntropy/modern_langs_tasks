import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
try:
    cursor.execute("CREATE TABLE images (site_url CHAR, image_url CHAR);")
except sqlite3.OperationalError:
    pass



def add_site_data(url, images):
    purchases = [(url, img)  for img in images ]
    query = 'INSERT INTO images VALUES (?,?)'
    cursor.executemany(query, purchases)
    conn.commit()

def get_images(url=None):
    if url:
        query =  'SELECT site_url, image_url from images WHERE site_url="{}";'.format(url)
    else:
        query =  'SELECT site_url, image_url from images ORDER BY rowid DESC;'
    images_urls = cursor.execute(query).fetchall()
    return images_urls

def get_all_sites():
    return set(cursor.execute('SELECT distinct site_url from images').fetchall())

def remove_all():
    cursor.execute('DROP TABLE images')
    conn.commit()



if __name__ == '__main__':
    # cursor.executemany('INSERT INTO images VALUES ("kek.com", ?)', 
    #     [('javascript:alert("Hello"); alert("World");', )])
    remove_all()
    # cursor.commit()
    # add_site_data('https://auto.ferrari.com/en_EN/', 
    #     ['https://auto.ferrari.com/en_EN/wp-content/uploads/sites/5/2018/10/Ferrari_MonzaSP1-1260x570.jpg'])
    # print(get_images())

    # print(get_all_sites())
