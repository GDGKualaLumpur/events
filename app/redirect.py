import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://www.gdgkl.org") 

app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)