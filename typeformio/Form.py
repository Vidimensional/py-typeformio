# -*- coding: utf-8 -*-
from Image import Image

class Form (object):
    def __init__ (self, buildapi, title, webhook_submit_url, design_id=None):
        self.form_endpoint = '/forms'
        self.buildapi = buildapi
        self.json = {'title': title, 'webhook_submit_url': webhook_submit_url,'fields': []}
        if design_id is not None:
            self.json['design_id'] = design_id


    def formField (fieldMethod):

        def addField (self, question, description=None, required=None, **field_args):
            new_field = {'question': question}
            if description:
                new_field['description'] = str(description)
            if required is not None:
                new_field['required'] = bool(required)
            new_field.update( fieldMethod(self, question, description, required, **field_args) )
            self.json['fields'].append(new_field)

        return addField


    @formField
    def addShortTextField (self, question, description=None, required=False,
                           max_characters=None):
        new_field = {'type': 'short_text'}
        if max_characters is not None:
            new_field['max_characters'] = str(max_characters)
        return new_field


    @formField
    def addLongTextField (self, question, description=None, required=False,
                          max_characters=None):
        new_field = {'type': 'long_text'}
        if max_characters is not None:
            new_field['max_characters'] = str(max_characters)
        return new_field


    @formField
    def addStatementField (self, question, description=None, required=False):
        new_field = {'type': 'statement'}
        return new_field


    @formField
    def addMultipleChoiceField (self, question, description=None, required=False,
                                choices=[]):
        new_field = {'type': 'multiple_choice'}
        choices_object = [ { 'label': elem } for elem in choices ]
        new_field['choices'] = choices_object
        return new_field


    @formField
    def addPictureChoiceField (self, question, description=None, required=False,
                               choices=[]):
        # Choices must be an array of tuples like '(image_url, image_label)'
        new_field = {'type': 'picture_choice'}
        choices_object = []
        for elem in choices:
            image_id = Image(self.buildapi, elem[0]).getImageId()
            label = elem[1]
            choices_object.append({ 'image_id': image_id,
                                    'label': label })
        new_field['choices'] = choices_object
        return new_field


    @formField
    def addDropdownField (self, question, description=None, required=False,
                          choices=[]):
        new_field = {'type': 'dropdown'}
        choices_object = [ { 'label': elem } for elem in choices ]
        new_field['choices'] = choices_object
        return new_field


    @formField
    def addYesNoField (self, question, description=None, required=False):
        new_field = {'type': 'yes_no'}
        return new_field


    @formField
    def addNumberField (self, question, description=None, required=False):
        new_field = {'type': 'number'}
        return new_field


    @formField
    def addRatingField (self, question, description=None, required=False):
        new_field = {'type': 'rating'}
        return new_field


    @formField
    def addOpinionScaleField (self, question, description=None, required=False):
        new_field = {'type': 'opinion_scale'}
        return new_field


    @formField
    def addEmailField (self, question, description=None, required=False):
        new_field = {'type': 'email'}
        return new_field


    @formField
    def addWebsiteField (self, question, description=None, required=False):
        new_field = {'type': 'website'}
        return new_field


    @formField
    def addLegal (self, question, description=None, required=False):
        new_field = {'type': 'legal'}
        return new_field


    def generateForm (self):
        return self.buildapi.POSTjson(self.form_endpoint, self.json)
