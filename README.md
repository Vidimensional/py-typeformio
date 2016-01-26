# py-typeformio
Pythonic library for [typeform.io](http://typeform.io/) API (WORK IN PROGRESS).

##Usage
###Authentication
First you'll need an API Key, [you can get yours here](http://docs.typeform.io/v0.4/page/signup).

Then you just have to define put it on a env variable called ``TYPEFORMIO_API_TOKEN`` and py-typeformio will use it.

Also, you can define it on your code when initialize the BuildAPI:
```python
(...)
buildapi = BuildAPI(api_token='XXX')
(...)
```

### Basic example

Example:
```python
from typeformio.Design import Design
from typeformio.Form import Form
from typeformio.BuildAPI import BuildAPI

buildapi = BuildAPI()

design = Design(buildapi)
design.colors['question'] = '#FFFFFF'
design.colors['button'] = '#069ACB'
design.colors['answer'] = '#CEDBF0'
design.colors['background'] = '#292929'

design_json = design.generateDesign()
design_id = design_json['id']

form = Form(buildapi, 'Probando', 'http://vidimensional.es/hook',
            design_id=design_id)

form.addShortTextField("What's your name?")
form.addYesNoField("Do you like Boardgames?")
form.addDropdownField('Which is you favourite boardgame?',
                      choices=['King Of Tokyo',
                               'Tigris and Eufrates',
                               'Carcassonne'])
form.addPictureChoiceField('Who is you favourite author?',
        choices=[
            ('https://cf.geekdo-images.com/images/pic511133_t.jpg', 'Richard Garfield'),
            ('https://cf.geekdo-images.com/images/pic472979_t.jpg', 'Reiner Knizia'),
            ('https://cf.geekdo-images.com/images/pic820214_t.jpg', 'Klaus-Jürgen Wrede') ])

json_response = form.generateForm()
```

This will generate a form [like this](https://forms.typeform.io/to/45dVbNDTrB).

### Available fields
#### Short text
#### Long text
#### Statement
#### Multiple choice
#### Picture choice
#### Dropdown
#### Yes/No
#### Image
#### Rating
#### Opinion scale
#### Email
#### Website
#### Legal


###More documentation:
http://docs.typeform.io/
