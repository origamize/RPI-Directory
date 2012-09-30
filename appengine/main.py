import webapp2
from google.appengine.api import users
import os
import jinja2
import logging
from models import Person

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    template_values = {'user': user}
    template = jinja_environment.get_template('html/index_new.html')
    self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage)])