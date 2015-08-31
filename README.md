# py-typeformio
Pythonic library for typeform.io API (WORK IN PROGRESS).

Example:
```python
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

form = Form('Probando', 'http://vidimensional.es/hooker')
form.addStatementField('hola ke ase')
buildapi = BuildAPI("API_TOKEN")
buildapi.buildForm(form)
```
