# -*- coding: utf-8 -*-
from Image import Image

class Form (object):
    def __init__ (self, buildapi, title, webhook_submit_url, design_id=None):
        self.form_endpoint = '/forms'
        self.buildapi = buildapi
        self.json = {'title': title, 'webhook_submit_url': webhook_submit_url,'fields': []}
        if design_id is not None:
            self.json['design_id'] = design_id


    def __addField (self, field_type, question, description, required):
        new_field = {'type': field_type, 'question': question}
        #if required is not None:
        #    new_field['required'] = bool(required)

        if description:
            new_field['description'] = str(description)

        return new_field


    def addShortTextField (self, question, description=None, required=False,
                           max_characters=None):
        new_field = self.__addField('short_text', question, description, required)
        if max_characters is not None:
            new_field['max_characters'] = str(max_characters)
        self.json['fields'].append(new_field)


    def addLongTextField (self, question, description=None, required=False,
                          max_characters=None):
        new_field = self.__addField('long_text', question, description, required)
        if max_characters is not None:
            new_field['max_characters'] = str(max_characters)
        self.json['fields'].append(new_field)


    def addStatementField (self, question, description=None, required=False):
        new_field = self.__addField('statement', question, description, required)
        self.json['fields'].append(new_field)


    def addMultipleChoiceField (self, question, description=None, required=False,
                                choices=[]):
        new_field = self.__addField('multiple_choice', question, description, required)
        choices_object = [ { 'label': elem } for elem in choices ]
        new_field['choices'] = choices_object
        self.json['fields'].append(new_field)


    def addPictureChoiceField (self, question, description=None, required=False,
                               choices=[]):
        # Choices must be an array of tuples like '(image_url, image_label)'
        new_field = self.__addField('picture_choice', question, description, required)
        choices_object = []
        for elem in choices:
            image_id = Image(self.buildapi, elem[0]).getImageId()
            label = elem[1]
            choices_object.append({ 'image_id': image_id,
                                    'label': label })
        new_field['choices'] = choices_object
        self.json['fields'].append(new_field)


    def addDropdownField (self, question, description=None, required=False,
                          choices=[]):
        new_field = self.__addField('dropdown', question, description, required)
        choices_object = [ { 'label': elem } for elem in choices ]
        new_field['choices'] = choices_object
        self.json['fields'].append(new_field)


    def addYesNoField (self, question, description=None, required=False):
        new_field = self.__addField('yes_no', question, description, required)
        self.json['fields'].append(new_field)


    def addNumberField (self, question, description=None, required=False):
        new_field = self.__addField('number', question, description, required)
        self.json['fields'].append(new_field)


    def addRatingField (self, question, description=None, required=False):
        new_field = self.__addField('rating', question, description, required)
        self.json['fields'].append(new_field)


    def addOpinionScaleField (self, question, description=None, required=False):
        new_field = self.__addField('opinion_scale', question, description, required)
        self.json['fields'].append(new_field)


    def addEmailField (self, question, description=None, required=False):
        new_field = self.__addField('email', question, description, required)
        self.json['fields'].append(new_field)


    def addWebsiteField (self, question, description=None, required=False):
        new_field = self.__addField('website', question, description, required)
        self.json['fields'].append(new_field)


    def addLegal (self, question, description=None, required=False):
        new_field = self.__addField('legal', question, description, required)
        self.json['fields'].append(new_field)


    def generateForm (self):
        return self.buildapi.POSTjson(self.form_endpoint, self.json)
