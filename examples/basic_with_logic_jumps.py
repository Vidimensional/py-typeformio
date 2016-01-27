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
form.addYesNoField("Do you like Boardgames?", ref="do_you_like_boardgames")

form.addDropdownField('Which is you favourite boardgame?',
                      choices=['King Of Tokyo',
                               'Tigris and Eufrates',
                               'Carcassonne'],
                      ref="favourite_boardgame")
form.addPictureChoiceField('Who is you favourite author?',
        choices=[
            ('https://cf.geekdo-images.com/images/pic511133_t.jpg', 'Richard Garfield'),
            ('https://cf.geekdo-images.com/images/pic472979_t.jpg', 'Reiner Knizia'),
            ('https://cf.geekdo-images.com/images/pic820214_t.jpg', 'Klaus-Jürgen Wrede')],
        ref='favourite_author')
form.addStatementField("Thank you for your time :)", ref='thanks')

form.addLogicJump('do_you_like_boardgames', False, 'thanks')

json_response = form.generateForm()

pprint(json_response)
