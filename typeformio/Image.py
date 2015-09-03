# -*- coding: utf-8 -*-

from BuildAPI import BuildAPI

class Image (object):
    def __init__ (self, buildapi, image_url):
        image_endpoint = '/images'
        json = { 'url': image_url }
        self.response_json = buildapi.POSTjson(image_endpoint, json)

    def getImageId (self):
        return self.response_json['id']

