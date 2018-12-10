#!/usr/bin/env python

import os
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from collections import defaultdict
from datetime import datetime
from urllib   import urlretrieve
from urlparse import urljoin
from zipfile  import ZipFile
import pytz

# Request counters for Prometheus exporter
homersimpson_request_count = 0
covilha_request_count = 0

class Handler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # Handles for GET request
    def do_GET(self):

        global homersimpson_request_count
        global covilha_request_count

        if self.path=="/":
            self._set_headers()
            self.wfile.write("<html><head></head><body>MessageBird Webserver Index</body></html>")
        elif self.path=="/homersimpson":
            self._set_headers()
            self.wfile.write("<html><head></head><body><div><table width=\"100%\" height=\"100%\" align=\"center\" valign=\"center\"><tr><td><div style=\"text-align: center; vertical-align: middle;\"><img src=\"https://kpbs.media.clients.ellingtoncms.com/assets/img/2014/05/08/simp2006_homerarmscrossed_f_wide-f5b7cb17067fc89225d72d768a00dc0a9cf2545c_t800.jpg\" alt=\"Homer Simpson\"></div></td></tr></table></div></body></html>")
            homersimpson_request_count += 1
        elif self.path=="/covilha":
            self._set_headers()
            self.wfile.write("<html><head></head><body>Current time in Covilha City: %s</body></html>" % request_time('Covilha'))
            covilha_request_count += 1
        elif self.path=="/metrics":
            # Endpoint for Prometheus metrics
            self._set_headers()

            # Provide simple metrics in text-based format
            self.wfile.write("# HELP http_requests_total The total number of HTTP requests for a respective endpoint.\n")
            self.wfile.write("# TYPE http_requests_total counter\n")
            self.wfile.write("http_request_total {endpoint=\"homersimpson\"} %i\n" % homersimpson_request_count)
            self.wfile.write("http_request_total {endpoint=\"covilha\"} %i\n" % covilha_request_count)
            self.wfile.write("\n")

def request_time(city):
    
    "Get time of a request for a certain city"

    geonames_url = 'http://download.geonames.org/export/dump/'
    basename = 'cities15000'
    filename = basename + '.zip'

    if not os.path.exists(filename):
        urlretrieve(urljoin(geonames_url, filename), filename)

    city2tz = defaultdict(set)
    with ZipFile(filename) as zf, zf.open(basename + '.txt') as file:
        for line in file:
            fields = line.split(b'\t')
            if fields:
                name, asciiname, alternatenames = fields[1:4]
                timezone = fields[-2].decode('utf-8').strip()
                if timezone:
                    for city in [name, asciiname] + alternatenames.split(b','):
                        city = city.decode('utf-8').strip()
                        if city:
                            city2tz[city].add(timezone)
    
    for tzname in city2tz[city]:
        return datetime.now(pytz.timezone(tzname)).strftime('%H:%M:%S')

if __name__ == "__main__":

    try:
        port = int(os.getenv('WEBSERVER_PORT', 80))
        address = os.getenv('WEBSERVER_ADDRESS', "127.0.0.1")
        httpd = HTTPServer((address, port), Handler)
        print("HTTP server is listening on address %s and %s port" % (address, port))
        httpd.serve_forever()
    
    except KeyboardInterrupt:
        print ("Shutting down the web server")
        httpd.socket.close()
