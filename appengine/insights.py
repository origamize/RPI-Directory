import webapp2
from google.appengine.api import users
import os
import jinja2
import logging
from models import Person
from models import StatsObject
import hashlib
import urllib

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class Stats(webapp2.RequestHandler):
  def get(self):
    num_people = Person.query().count(limit=15000)
    num_stats = StatsObject.query().count()
    
    majors = StatsObject.get_by_id('global:major').json
    first_name = StatsObject.get_by_id('global:first_name').json
    last_name = StatsObject.get_by_id('global:last_name').json
    year = StatsObject.get_by_id('global:year').json
    dept = StatsObject.get_by_id('global:department').json
    title = StatsObject.get_by_id('global:title').json
    type_person = StatsObject.get_by_id('global:type').json
    
    stats = [{'title': 'Breakdown by Major', 'data': majors},
             {'title': 'Breakdown by Year', 'data': year},
             {'title': 'Breakdown by First Name', 'data': first_name},
             {'title': 'Breakdown by Last Name', 'data': last_name},
             {'title': 'Breakdown by Title', 'data': title},
             {'title': 'Breakdown by Department', 'data': dept},
             {'title': 'Breakdown by Position', 'data': type_person}]
    
    logging.info(majors)
    
    template_values = {'active': 'stats',
                       'num_people': num_people,
                       'num_stats': num_stats,
                       'stats': stats}
    template = jinja_environment.get_template('html/insights.html')
    self.response.out.write(template.render(template_values))
    

app = webapp2.WSGIApplication([('/insights.*', Stats)])