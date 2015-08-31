# -*- coding: utf-8 -*-

import os
import requests

from Form import Form

class ApiTokenNotDefinedException (Exception):
    pass

class BuildAPI (object):
    def __init__ (self, api_token=None):
	self.forms_endpoint = 'https://api.typeform.io/v0.4/forms'
        self.api_token = None
        if api_token:
            self.api_token = api_token
        else:
            try:
                self.api_token = os.environ['TYPEFORMIO_API_TOKEN']
            except KeyError:
                raise ApiTokenNotDefinedException
    
    def buildForm (self, form):
        headers = {'X-API-TOKEN': self.api_token}
        r = requests.post(self.forms_endpoint, headers=headers, json=form.json)
        print r.status_code
	print r.json()
