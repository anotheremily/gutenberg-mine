#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'index',
	'/about', 'about',
	'/visualizer', 'visualizer',
	'/examples', 'examples'
)

app = web.application(urls, globals()).wsgifunc() 
render = web.template.render('templates/')

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

###
# Page definitions
###
class index:
	def GET(self):
		return render.desktop(render.index(), 'Welcome')

class about:
	def GET(self):
		return render.desktop(render.about(), 'About')

class visualizer:
	def GET(self):
		return render.desktop(render.visualizer(), 'Visualizer')

class examples:
	def GET(self):
		return render.desktop(render.examples(), 'Examples')

if __name__ == "__main__": 
	app.cgirun()
