#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import mail

import os

path = os.path.join(os.path.dirname(__file__), 'templates')

class MainHandler(webapp.RequestHandler):
	def get(self):
 		self.response.out.write(template.render(path + '/index.html', {}))

class Contact(webapp.RequestHandler):
	def get(self):	
 		self.response.out.write(template.render(path + '/contact.html', {}))
	
class Contact2(webapp.RequestHandler):
	def post(self):
		sender = self.request.get("email", default_value=str)
		subject = self.request.get("subject")
		body = self.request.get("message", default_value=str)
		message = mail.EmailMessage(sender="BP <gbaopham@gmail.com>", subject=subject)
		message.to = "BP <gbao.pham@gmail.com>"
		message.body = "From: " + sender + "\nMessage:\n" + body 
		message.send()
		self.response.out.write(template.render(path + '/contact2.html', {}))
 		
class Resume(webapp.RequestHandler):
	def get(self):	
 		self.response.out.write(template.render(path + '/resume.html', {}))

class PDF(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = "application/txt"
		self.response.headers['Content-Disposition'] = "attachment; filename=resume.pdf"
		f = open(os.path.dirname(__file__) + '/files/Resume.pdf', 'r')
		self.response.out.write(f.read())

class Javascript_category(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render(path + '/javascript.html', {}))

class HTML5_category(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render(path + '/html5.html', {}))

class Bookmarks_category(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render(path + '/bookmarks.html', {}))

class sitemap(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render(path + '/sitemap.xml', {}))

def main():
    application = webapp.WSGIApplication([('/', MainHandler), 
										('/resume', Resume), 
										('/contact', Contact),
										('/sent', Contact2),
										('/download_resume', PDF),
                                        ('/javascript', Javascript_category),
                                        ('/html5', HTML5_category),
                                        ('/bookmarks', Bookmarks_category),
                                        ('/sitemap', sitemap)],
                                        debug=False)
    util.run_wsgi_app(application)

if __name__ == '__main__':
	main()
