# -*- coding: utf-8 -*-

import os
import requests

class ApiTokenNotDefinedException (Exception):
    pass

class BuildAPI (object):
    def __init__ (self, api_token=None, user_agent='pyformio'):
        self.api_token = None
        self.user_agent = user_agent
        if api_token:
            self.api_token = api_token
        else:
            try:
                self.api_token = os.environ['TYPEFORMIO_API_TOKEN']
            except KeyError:
                raise ApiTokenNotDefinedException

        self.headers = {'User-Agent':  self.user_agent,
                        'X-API-TOKEN': self.api_token}
        #self.headers = {'User-Agent':  self.user_agent,
        #                'X-API-TOKEN': self.api_token}

    def POSTjson (self, endpoint, json):
        url_endpoint = 'https://api.typeform.io/v0.4%s' % endpoint
	print "posting %s" % url_endpoint
        r = requests.post(url_endpoint, headers=self.headers, json=json)
	print "Response: %s" % r.status_code
	print r.raw.read()
	return r.json()


