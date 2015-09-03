# -*- coding: utf-8 -*-
from BuildAPI import BuildAPI

class Design (object):
    def __init__ (self, buildapi):
        self.design_endpoint = '/designs'
        self.colors = { "question": "#3D3D3D", 
			"button": "#4FB0AE", 
			"answer": "#4FB0AE", 
			"background": "#FFFFFF" }
        self.font = "Source Sans Pro"
	self.buildapi = buildapi


    def generateDesign (self):
        json = { 'colors': self.colors,
                 'font': self.font }
        return self.buildapi.POSTjson(self.design_endpoint, json)
