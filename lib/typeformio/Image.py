# -*- coding: utf-8 -*-

from BuildAPI import BuildAPI

class Image (object):
    def __init__ (self, buildapi, image_url):
        self.image_endpoint = '/images'
        self.json = { 'url': image_url }
        self.buildapi = buildapi

    def getImageId (self):
        return self.buildapi.POSTjson(self.image_endpoint, self.json)['id']

