#-*- coding: utf-8 -*-

class Form (object):
    def __init__ (self, title, webhook_submit_url, design_id=None):
        self.json = {'title': title, 'webhook_submit_url': webhook_submit_url,'fields': []}
        if design_id is not None:
            self.json['design_id'] = design_id


    def __addField (self, field_type, question, description, required):
        new_field = {'type': field_type, 'question': question}
        if required is not None:
            new_field['required'] = required

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
        new_field['choices'] = choices
        self.json['fields'].append(new_field)


    def addPictureChoiceField (self, question, description=None, required=False,
                               choices=[]):
        new_field = self.__addField('picture_choice', question, description, required)
        new_field['choices'] = choices
        self.json['fields'].append(new_field)


    def addDropdownField (self, question, description=None, required=False,
                          choices=[]):
        new_field = self.__addField('dropdown', question, description, required)
        new_field['choices'] = choices
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

