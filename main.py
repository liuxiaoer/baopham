#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import mail

import os
# import google.appengine.api.memcache
# memcache.flush_all()
# memcache.set(key="static-version", value=os.environ['2'])

class MainHandler(webapp.RequestHandler):
	def get(self):
 		self.response.out.write(template.render('index.html', {}))

class Contact(webapp.RequestHandler):
	def get(self):	
 		self.response.out.write(template.render('contact.html', {}))
	
class Contact2(webapp.RequestHandler):
	def post(self):
		sender = self.request.get("email", default_value=str)
		subject = self.request.get("subject")
		body = self.request.get("message", default_value=str)
		message = mail.EmailMessage(sender="BP <gbaopham@gmail.com>", subject=subject)
		message.to = "BP <gbao.pham@gmail.com>"
		message.body = "From: " + sender + "\nMessage:\n" + body 
		message.send()
		self.response.out.write(template.render('contact2.html', {}))
 		
class Resume(webapp.RequestHandler):
	def get(self):	
 		self.response.out.write(template.render('resume.html', {}))

class PDF(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = "application/txt"
		self.response.headers['Content-Disposition'] = "attachment; filename=resume.pdf"
		f = open(os.path.dirname(__file__) + '/Resume.pdf', 'r')
		self.response.out.write(f.read())

class Javascript_category(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('javascript.html', {}))

class HTML5_category(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('html5.html', {}))

class Bookmarks_category(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('bookmarks.html', {}))

def main():
    application = webapp.WSGIApplication([('/', MainHandler), 
										('/resume', Resume), 
										('/contact', Contact),
										('/sent', Contact2),
										('/download_resume', PDF),
                                        ('/javascript', Javascript_category),
                                        ('/html5', HTML5_category),
                                        ('/bookmarks', Bookmarks_category)],
                                        debug=False)
    util.run_wsgi_app(application)

if __name__ == '__main__':
	main()
