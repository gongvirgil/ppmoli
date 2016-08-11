#!/usr/bin/env python
# -* - coding: UTF-8 -* -
import web
web.config.debug = False
db = web.database(
    dbn='mysql',
    user='root',
    pw='',
    host='localhost',
    port=3306,
    db='mydoc',
    charset='utf8',
)
render = web.template.render('templates')
urls = (
    '/', 'index')
app = web.application(urls, globals())
data = {
    'name': '',
    'user': ''
}


class index:
    def GET(self):
        name = "virgil"
        users = db.select('mydoc_user')
        data['name'] = name
        data['user'] = users[0].username
        print type(data)
        return render.index(data)

    def POST(self):
        post_data = web.input()
        data['name'] = post_data['name']
        data['user'] = post_data['username']
        return render.index(data)

if __name__ == "__main__":
    app.run()
