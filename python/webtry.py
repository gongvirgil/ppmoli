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
    '/count', 'count',
    '/reset', 'reset',
    '/login', 'login',
    '/', 'index'
)
app = web.application(urls, globals())
session = web.session.Session(
    app,
    web.session.DiskStore('sessions'),
    initializer={'count': 0}
)
data = {}


class count:
    def GET(self):
        session.count += 1
        return session.count


class reset:
    def GET(self):
        session.kill()
        return ""


class login:
    def GET(self):
        return render.login()

    def POST(self):
        post_data = web.input()
        username = post_data['username']
        password = post_data['password']
        print session.count
        print username
        print password
        return render.login()


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
