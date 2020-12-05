import io
import re
from pprint import pprint

# from marshmallow import fields, Schema, validate, ValidationError


# class IdSchema(Schema):
#     byr = fields.Integer(required=True)
#     iyr = fields.Integer(required=True)
#     eyr = fields.Integer(required=True)
#     hgt = fields.String(required=True, validate=validate.Regexp(regex=r'\d+cm'))
#     hcl = fields.String(required=True, validate=validate.Regexp(regex=r'#\d+'))
#     ecl = fields.String(required=True)
#     pid = fields.Integer(required=True)
#     cid = fields.Integer(required=False)


def fieldExtractor(data: str) -> dict:
    """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm
    """
    id_dict = {}
    for pair in data.split(' '):
        kv = pair.split(':')
        id_dict[kv[0]] = kv[1]
    
    return id_dict

def validatorV1(passport: dict) -> bool:
    v1_keys = ["ecl","pid","eyr","hcl","byr","iyr","hgt"]

    for key in v1_keys:
        if key not in passport.keys():
            return False
    return True

def validatorV2(passport: dict) -> bool:
    

def part1():
    file_name = "input.txt"
    lines = open(file_name, "r").read()

    #flatten IDs to one line each
    lines = re.sub(r'(\w)\n(\w)',r'\g<1> \g<2>',lines)
    
    #remove extra line breaks
    lines = re.sub(r'\n\n',r'\n',lines)
    ids = 0
    for line in lines.split('\n'):
        print(line)
        passport = fieldExtractor(line)
        if validatorV1(passport):
            ids += 1

    print(ids)

part1()