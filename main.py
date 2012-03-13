#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template
from google.appengine.runtime import apiproxy_errors
from google.appengine.api import mail
import os
import logging

path = os.path.join(os.path.dirname(__file__), 'templates')

class MainHandler(webapp.RequestHandler):
    def get(self):
        if "iPhone" in self.request.headers["User-Agent"]:
            self.redirect("http://iphone.bphamworld.appspot.com")
        else:
            self.response.out.write(template.render(path + '/index.html', {'home_active': 'active', 'resume_active': ''}))

class Contact(webapp.RequestHandler):
    def get(self):	
        self.response.out.write(template.render(path + '/contact.html', {}))

class Contact2(webapp.RequestHandler):
    def post(self):
        try:
            sender = self.request.get("email", default_value=str)
            subject = self.request.get("subject")
            body = self.request.get("message", default_value=str)
            message = mail.EmailMessage(sender="Website Viewer <gbaopham@gmail.com>", subject=subject)
            message.to = "BP <gbao.pham@gmail.com>"
            message.body = "From: " + sender + "\nMessage:\n" + body
            message.send()
            self.response.out.write(template.render(path + '/contact2.html', {}))
        except apiproxy_errors.OverQuotaError, m:
            logging.error(m)
            self.response.out.write('The email could not be sent. Please try again later.')

class Resume(webapp.RequestHandler):
    def get(self):	
        if "iPhone" in self.request.headers["User-Agent"]:
            self.redirect("http://iphone.bphamworld.appspot.com/resume")
        else:
            self.response.out.write(template.render(path + '/resume.html', 
                                                    {'home_active': '', 
                                                     'resume_active': 'active',
                                                     'onload_js': ''}))

class PDF(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = "application/txt"
        self.response.headers['Content-Disposition'] = "attachment; filename=resume.pdf"
        f = open(os.path.dirname(__file__) + '/files/Resume.pdf', 'r')
        self.response.out.write(f.read())

class Javascript_category(webapp.RequestHandler):
    def get(self):
        if "iPhone" in self.request.headers["User-Agent"]:
            self.redirect("http://iphone.bphamworld.appspot.com/javascript")
        else:
            self.response.out.write(template.render(path + '/javascript.html', 
                                                    {'matrix_href': '#matrix',
                                                     'life_href': '#life',
                                                     'js_active': 'active',
                                                     'onload_js': 'detectHash()'}))

class HTML5_category(webapp.RequestHandler):
    def get(self):
        if "iPhone" in self.request.headers["User-Agent"]:
            self.redirect("http://iphone.bphamworld.appspot.com/html5")
        else:
            self.response.out.write(template.render(path + '/html5.html', 
                                                    {'chess_href': '#chess',
                                                     'life_href': '#life',
                                                     'html5_active': 'active',
                                                     'onload_js': 'detectHash()'}))

class Bookmarks_category(webapp.RequestHandler):
    def get(self):
        if "iPhone" in self.request.headers["User-Agent"]:
            self.redirect("http://iphone.bphamworld.appspot.com/bookmarks")
        else:
            self.response.out.write(template.render(path + '/bookmarks.html', 
                                                    {'content_class': 'bookmarks',
                                                     'bookmarks_active': 'active',
                                                     'onload_js': 'detectHash()'}))

class Sitemap(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render(path + '/sitemap.xml', {}))

class ErrorHandler(webapp.RequestHandler):
    def get(self):
        self.error(404)
        #self.response.out.write(template.render(path + '/404.html', {}))        
        self.response.out.write('''
                                <html>
                                <head>
                                <title>Page not found</title>
                                </head>
                                <body>
                                <h1>Page not found</h1>
                                <hr>
                                <p>Sorry, but the requested page could not be found</p>

                                </body>
                                </html>
                                ''')

def main():
    application = webapp.WSGIApplication([('/', MainHandler), 
                                          ('/resume', Resume), 
                                          ('/download_resume', PDF),
                                          ('/javascript', Javascript_category),
                                          ('/html5', HTML5_category),
                                          ('/bookmarks', Bookmarks_category),
                                          ('/sitemap', Sitemap),
                                          ('/.*', ErrorHandler)],
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()

