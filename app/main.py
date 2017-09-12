import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("https://www.gdgkl.org") 

class Tfxkl17(webapp2.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('//' + self.request.host + '/tfxkl17/')

class TensorflowDevSummit(webapp2.RequestHandler):
  def get(self, *args, **kwargs):
    path = self.request.path_qs.split('/')
    if (path[1] != 'tensorflow-dev-summit'):
        self.redirect('https://www.gdgkl.org')
    else:
        self.redirect('//' + self.request.host + '/tfxkl17/' + '/'.join(path[2:]))

class Jomcodekl17(webapp2.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('//' + self.request.host + '/jomcodekl17/')

app = webapp2.WSGIApplication([
    ('/tfxkl17.*', Tfxkl17),
    ('/tensorflow-dev-summit.*', TensorflowDevSummit),
    ('/jomcodekl17.*', Jomcodekl17),
    ('/.*', MainPage),
], debug=True)