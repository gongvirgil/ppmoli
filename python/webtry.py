#!/usr/bin/env python
# -* - coding: UTF-8 -* -
import web

render = web.template.render('templates')
urls = (
    '/', 'index')


class index:
    def GET(self):
        name = "virgil"
        print render.index(name)

web.webapi.internalerror = web.debugerror
if __name__ == "__main__":
    web.run(urls, globals(), web.reloader)
