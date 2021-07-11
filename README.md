# validatorfx

A simple Python json validator, can be used to validate incoming REST requests
Early stage developement, please feel free to raise any issue, enhancements, or suggessions

## Currently supported data types
    object/dict
    string
    integer
    float
    boolean
    email
    array/list
## Importing the package
`from validatorfx.index import validate `

## Example use cases
```
testSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "required":"true"},
        "class": {"type": "string"},
        "subjects": {
            "type": "object",
            "properties": {
                "subject1": {"type": "string"},
            },
            "required":"true"
        }
    },
    "required" : "true"
}

data = {
    "name": "Nandan Raj"
    "class": "5B",
    "subjects": {
        "subject1": "maths"
    }
}

validate(testSchema, data)
```

```
testSchema2 = {
    "type": "string"
}
data2 = "test"

validate(testSchema, data)
```

```
from validatorfx.index import validate

testSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "class": {"type": "string"},
        "email": {"type": "email", "required": "true"},
        "subjects": {"type": "array", "required": "true"},
        "xobj": {
            "type": "object",
            "properties": {
                "dsf": {
                    "type": "string"
                }
            }
        },
        "nraj":{
            "type" : "object",
            "properties":{},
            "required":"true"
        }
    }
}

data = {
    "name": "Nandan Raj",
    "class": "5b",
    "email": "hjhdsajh@gh.ds",
    "subjects": ["Maths", "Science"],
    "xobj": {
        "dsf": "sdfsd"
    },
    "nraj":{}
}

validate(testSchema, data)

```

