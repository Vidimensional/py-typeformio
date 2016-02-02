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

buildapi = BuildAPI(user_agent='My Awesome app')

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

###Your own user agent.
You can define your own user agent when initialize BuildAPI.
```python
(...)
buildapi = BuildAPI(user_agent='My Awesome app')
(...)
```

### Available fields
#### Short text
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `max_characters` | The maximum number of characters the respondent can type as an answer.                            | -       | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Long text
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Statement
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `choices`        | Array of choice objects with the choices that the respondent can select                           | `[]`    | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Multiple choice
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `choices`        | Array of choice objects with the choices that the respondent can select.                          | `[]`    | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Picture choice
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `choices`        | Array of choice objects with the choices that the respondent can select                           | `[]`    | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Dropdown
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `choices`        | Array of choice objects with the choices that the respondent can select.                          | `[]`    | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Yes/No
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Image
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Rating
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Opinion scale
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Email
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -       | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Website
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -      | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |

#### Legal
| Argument         | Description                                                                                       | Default | Required |
| :--------------: | ------------------------------------------------------------------------------------------------- | ------- | -------- |
| `question`       | The main question text for the field.                                                             | -      | Yes      |
| `description`    | The description (or sub-text) that appears below the main question text (in a smaller font size). | -       | No       |
| `required`       | Decides if the field is mandatory.                                                                | `False` | No       |
| `tags`           | An array of tags as strings.                                                                      | `[]`    |          |
| `ref`            | A unique reference for the field.                                                                 | -       | No       |


###More documentation:
http://docs.typeform.io/
