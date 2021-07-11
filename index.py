##
# @author: Nandan Raj
##
import re

def validate(schema, data, key="inputSchema"):
    if(not "type" in schema):
        raise ValueError(f'{key}: Schema type not defined',
                         schema, 'schemaError')

    if(schema["type"] == "string"):
        isString(data, key)

    elif(schema["type"] == "integer"):
        isInteger(data, key)

    elif(schema["type"] == "float"):
        isFloat(data, key)

    elif(schema["type"] == "boolean"):
        isBoolean(data, key)

    elif(schema["type"] == "email"):
        isEmail(data, key)

    elif(schema["type"] == "array"):
        isArray(data, key)

    elif(schema["type"] == "object"):
        isObject(data, key)

    else:
        raise LookupError(
            f'{schema["type"]}: type is not known', schema, 'schemaError')

    if(schema["type"] == "object"):
        # Checks if "properties" is not present in schema: it defines all property data can have
        if(not "properties" in schema):
            raise ValueError(
                f'{key}: Schema properties not defined', schema, 'schemaError')

        #Checks if schema properties is object or not: Should always be an object 
        isObject(schema["properties"],f"{key}.properties")

        # Checks if any Foreign key is present in data: A key that is not defined in properties of schema
        for dataKey in data:
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

            #Checks if Schema value is object type or not
            if(type(schemaValue) != dict):
                raise ValueError(
                    f'{key}: Schema/Subschema is not of type object/dict', schema, 'schemaError')

            # Checks for each key of schema properies only if they are also in data
            if(key in data):
                validate(schemaValue, data[key], key)


def isArray(data, key):
    if(isinstance(data, list)):
        return True
    else:
        raise TypeError(f'{key}: Not a valid Array/list', data, 'typeError')


def isObject(data, key):
    if(type(data) == dict):
        return True
    else:
        raise TypeError(f'{key}: Not a valid Object/dict', data, 'typeError')


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


def isEmail(data, key):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if(type(data) == str and re.search(regex, data)):
        return True
    else:
        raise ValueError(f'{key}: Not a valid Email', data, 'emailInvalid')
