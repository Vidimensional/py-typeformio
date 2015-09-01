# py-typeformio
Pythonic library for typeform.io API (WORK IN PROGRESS).

Example:
```python
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

form = Form('Probando', 'http://vidimensional.es/hooker')
form.addStatementField('hola ke ase')
buildapi = BuildAPI("API_TOKEN")
json = buildapi.buildForm(form)
# Now, do whatever you want this json.
```

More documentation:
http://docs.typeform.io/
