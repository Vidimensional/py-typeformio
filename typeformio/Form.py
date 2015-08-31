#-*- coding: utf-8 -*-

class Form (object):
    def __init__ (self, title, webhook_submit_url, design_id=None):
        self.json = {'title': title, 'webhook_submit_url': webhook_submit_url,'fields': []}
        if design_id is not None:
            self.json['design_id'] = design_id


    def __addField (self, field_type, question, description, required):
        new_field = {'type': field_type, 'question': question}
        if required:
            new_field['required'] = 'true'
        else:
            new_field['required'] = 'false'
                     
        if description is not None:
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
        
                           
