# py-typeformio
Pythonic library for typeform.io API (WORK IN PROGRESS).

Example:
```python
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
