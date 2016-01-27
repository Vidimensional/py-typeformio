#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from pprint import pprint

from typeformio.Design import Design
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

buildapi = BuildAPI()

design = Design(buildapi)
design.colors['question'] = '#FFFFFF'
design.colors['button'] = '#069ACB'
design.colors['answer'] = '#CEDBF0'
design.colors['background'] = '#292929'

design_json = design.generateDesign()
design_id = design_json['id']

form = Form(buildapi, 'Probando', 'http://vidimensional.es/hook',
            design_id=design_id)

form.addShortTextField("What's your name?")
form.addYesNoField("Do you like Boardgames?")
form.addDropdownField('Which is you favourite boardgame?',
                      choices=['King Of Tokyo',
                               'Tigris and Eufrates',
                               'Carcassonne'])
form.addPictureChoiceField('Who is you favourite author?',
        choices=[
            ('https://cf.geekdo-images.com/images/pic511133_t.jpg', 'Richard Garfield'),
            ('https://cf.geekdo-images.com/images/pic472979_t.jpg', 'Reiner Knizia'),
            ('https://cf.geekdo-images.com/images/pic820214_t.jpg', 'Klaus-Jürgen Wrede') ])

json_response = form.generateForm()
print 1
print json_response
print 2
pprint(json_response)
