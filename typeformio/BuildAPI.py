# -*- coding: utf-8 -*-

import os
import requests

class ApiTokenNotDefinedException (Exception):
    pass

class BuildAPI (object):
    def __init__ (self, api_token=None):
        self.api_token = None
        if api_token:
            self.api_token = api_token
        else:
            try:
                self.api_token = os.environ['TYPEFORMIO_API_TOKEN']
            except KeyError:
                raise ApiTokenNotDefinedException
    
    def buildForm (self, form):
        coding

