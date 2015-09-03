# py-typeformio
Pythonic library for typeform.io API (WORK IN PROGRESS).

Example:
```python
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

buildapi = BuildAPI()

form = Form('Test form', buildapi, 'http://domain.tld/hook')
form.addStatementField('hola ke ase')
form.addLegal('pos te mola?')
form.addShortTextField('Dime como te llamas?')
form.addYesNoField('Se ha quedao buena tarde, no?')
form.addDropdownField('Que prefieres', choices=['manzana', 'platano', 'pomelo'])
form.addPictureChoiceField('con jake el perro y finn el humano', choices=[
            ('https://media.giphy.com/media/FMGubfDOHHnCo/giphy.gif', 'Why no both?'), 
            ('https://media.giphy.com/media/bE5qi2tiSfdZu/giphy.gif', 'Finn el humano'),
            ('https://media.giphy.com/media/j50v9vd9rbhjG/giphy.gif', 'Jake el perro') ]
)
json = form.generateForm()
```

More documentation:
http://docs.typeform.io/
