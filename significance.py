import webapp2
import math


def calculate_significance(s1, s2, r1, r2):
    ''' run chi-squared test on variables input '''
    if s1 == "":
        return ""
    try:
		comparative_error = 1.96 * math.sqrt( (float(r1)*(100-float(r1)))/float(s1) + (float(r2) * (100-float(r2)))/float(s2))
		response_difference = float(r1) - float(r2)
		if response_difference > comparative_error:
			significance = "yes"
			return str(significance)
		else:
			significance = "no"
			return str(significance)
    except ValueError:  # user entered non-numeric temperature
        return "invalid input"


class MainPage(webapp2.RequestHandler):
    def get(self):
        s1 = self.request.get("s1")
        s2 = self.request.get("s2")
        r1 = self.request.get("r1")
        r2 = self.request.get("r2")
        significance = calculate_significance(s1, s2, r1, r2)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head>
            <title>Statistical Significance Calculator</title>
            <!-- Latest compiled and minified Boostrap CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
            </head>
            <body>
              <form action="/" method="get">
                Sample sizes and responses: <input type="text"
                                        name="s1" placeholder="sample 1 size" value={} >
										<input type="text"
                                        name="r1" placeholder="response %" value={} >
										<input type="text"
                                        name="s2" placeholder="samle 2 size" value={} >
										<input type="text"
                                        name="r2" placeholder="response %" value={} >
                <input type="submit" value="Calculate"><br>
                Significance: {}
              </form>
            </body>
          </html>""".format(s1, r1, s2, r2, significance))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)