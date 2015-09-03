# py-typeformio
Pythonic library for typeform.io API (WORK IN PROGRESS).

Example:
```python
import pprint
import json

from typeformio.Design import Design
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

buildapi = BuildAPI()

design = Design(buildapi)
design.colors['background'] = '#121212'
design_json = design.generateDesign()
design_id = design_json['id']

form = Form(buildapi, 'Probando', 'http://vidimensional.es/hooker',design_id=design_id)
form.addStatementField('hola ke ase')
form.addLegal('pos te mola?')
form.addShortTextField('Dime como te llamas?')
form.addYesNoField('Se ha quedao buena tarde, no?')
form.addDropdownField('Que prefieres', choices=['manzana', 'platano', 'pomelo'])
form.addPictureChoiceField('con jake el perro y finn el humano', 
        choices=[
            ('https://media.giphy.com/media/FMGubfDOHHnCo/giphy.gif', 'Why no both?'), 
            ('https://media.giphy.com/media/bE5qi2tiSfdZu/giphy.gif', 'Finn el humano'),
            ('https://media.giphy.com/media/j50v9vd9rbhjG/giphy.gif', 'Jake el perro') ])

print "SHOW REQUEST"
print json.dumps(form.json, indent=4, separators=(',', ': '))

json_response = form.generateForm()
print "SHOW RESPONSE"
print json.dumps(json_response, indent=4, separators=(',', ': '))
```

More documentation:
http://docs.typeform.io/
