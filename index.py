##
# @author: Nandan Raj
##
import re

def validate(schema, data, key="input"):
    if(not "type" in schema):
        raise ValueError(f'{key}: Schema type not defined', schema, 'schemaError')

    if(schema["type"] == "object"):
        isObject(data, key)
    elif(schema["type"] == "string"):
        isString(data, key)
    elif(schema["type"] == "integer"):
        isString(data, key)
    elif(schema["type"] == "float"):
        isString(data, key)
    elif(schema["type"] == "boolean"):
        isString(data, key)
    elif(schema["type"] == "email"):
        isEmail(data, key)
    else:
        raise LookupError(
            f'{schema["type"]}: type is not known', schema, 'schemaError')

    if(schema["type"] == "object"):
        # Checks if "properties" is not present in schema: it defines all property data can have
        if(not "properties" in schema):
            raise ValueError(
                f'{key}: Schema properties not defined', schema, 'schemaError')

        # Checks if any Foreign key is present in data: A key that is not defined in properties of schema
        for dataKey in data.keys():
            if(not dataKey in schema["properties"]):
                raise KeyError(
                    f'{dataKey}: Foreign key present', data, "keyError")

        # Iterates over all property in schema and checks it in data
        for key in schema["properties"]:

            schemaValue = schema["properties"][key]
            # Checks if a required property is present or not in data
            if("required" in schemaValue and schemaValue["required"] == "true" and not key in data):
                raise KeyError(
                    f'{key}: Required key not present', data, "keyError")

            if(key in data):
                validate(schema["properties"][key], data[key], key)


def isObject(data, key):
    if(type(data) == dict):
        return True
    else:
        raise TypeError(f'Not a valid Object', data, 'typeError')


def isString(data, key):
    if(type(data) == str):
        return True
    else:
        raise TypeError(f'{key}: Not a valid String', data, 'typeError')


def isInteger(data, key):
    if(type(data) == int):
        return True
    else:
        raise TypeError(f'{key}: Not a valid Integer', data, 'typeError')


def isFloat(data, key):
    if(type(data) == float):
        return True
    else:
        raise TypeError(f'{key}: Not a valid Float', data, 'typeError')


def isBoolean(data, key):
    if(type(data) == bool):
        return True
    else:
        raise TypeError(f'{key}: Not a valid Boolean', data, 'typeError')


def isEmail(data):

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if(type(data) == str and re.search(regex, data)):
        return True
    else:
        raise ValueError('Not a valid Email', data, 'emailInvalid')
