import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("https://www.gdgkl.org") 

class Tfxkl17(webapp2.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('//' + self.request.host + '/tfxkl17/')

app = webapp2.WSGIApplication([
    ('/tfxkl17.*', Tfxkl17),
    ('/.*', MainPage),
], debug=True)