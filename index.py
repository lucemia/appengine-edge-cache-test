import webapp2
from datetime import timedelta, datetime

class NoCache(webapp2.RequestHandler):
    def get(self):
        return

HTTP_DATE_FMT_GMT = "%a, %d %b %Y %H:%M:%S GMT"
class Cache(webapp2.RequestHandler):
    def get(self):
        expires = datetime(2016, 1, 1)
        response_headers = self.response.headers
        response_headers['Expires'] = expires.strftime(HTTP_DATE_FMT_GMT)

        response_headers['Cache-Control'] = 'public, max-age=%d' % 120
        response_headers['Pragma'] = 'Public'

        self.response.out.write('asdfasdfasfasdfasdfasdfasdfasfasdf')
        return

app = webapp2.WSGIApplication([
    (r'/test/cache', Cache),
    (r'/test/nocache', NoCache)
], debug=False)

