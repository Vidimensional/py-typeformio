# py-typeformio
Pythonic library for typeform.io API (WORK IN PROGRESS).

Example:
```python
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

buildapi = BuildAPI()

form = Form('Test form', 'http://domain.tld/hook', buildapi)
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
print "sending juanson"
print json.dumps(form.json, indent=4, separators=(',', ': '))
pprint.pprint(form.json)

json = form.generateForm()
```
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

form = Form('Testing', 'http://yourdomain.tld/webhook')
form.addStatementField("This a programatically generated form")
form.addYesNoField("Isn't this awesome?")
form.addWebsiteField("Do you know any cool website?")
buildapi = BuildAPI("API_TOKEN")
json = buildapi.buildForm(form)
# Now, do whatever you want this json.
```

More documentation:
http://docs.typeform.io/
