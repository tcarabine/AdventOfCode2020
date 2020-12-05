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
    if (
        validatorV1(passport)
        and validate_byr(passport['byr'])
        and validate_ecl(passport['ecl'])
        and validate_eyr(passport['eyr'])
        and validate_hcl(passport['hcl'])
        and validate_hgt(passport['hgt'])
        and validate_iyr(passport['iyr'])
        and validate_pid(passport['pid'])
        ):
        return True
    else:
        return False

def validate_year(value: str, min_val: int, max_val: int) -> bool:
    try:
        value = int(value)
    except:
        print("Year Not String")
        return False
    if min_val <= value and value <= max_val:
        print("Year Valid")
        return True
    print("Year Not Valid")
    return False
    

def validate_byr(value: str) -> bool:
    return validate_year(value, 1920, 2002)

def validate_ecl(value: str) -> bool:
    valid = ["amb","blu","brn","gry","grn","hzl","oth"]
    if value in valid:
        print("Eye Colour Valid")
        return True
    else:
        print("Eye Colour Not Valid")
        return False

def validate_eyr(value: str) -> bool:
    return validate_year(value, 2020, 2030)

def validate_hcl(value: str) -> bool:
    pattern = r'#([0-9a-fA-F]){6}'
    if re.fullmatch(pattern, value):
        print("Hair Colour Valid")
        return True
    else:
        print("Hair Colour Not Valid")
        return False

def validate_hgt(value: str) -> bool:
    pattern = r'(\d+)(in|cm)'
    match = re.match(pattern, value)
    if match:
        if ((
                match.group(2) == 'in' 
                and int(match.group(1)) >= 59 
                and int(match.group(1)) <= 76
            ) or (
                match.group(2) == 'cm' 
                and int(match.group(1)) >= 150 
                and int(match.group(1)) <= 193
            )):
                print("Height Valid")
                return True
    print("Height Not Valid")
    return False

def validate_iyr(value: str) -> bool:
    return validate_year(value, 2010, 2020)

def validate_pid(value: str) -> bool:
    pattern = r'\d{9}'
    if re.fullmatch(pattern, value):
        print("PID Valid")
        return True
    else:
        print("PID Not Valid")
        return False

def load() -> list:
    file_name = "input.txt"
    lines = open(file_name, "r").read()

    #flatten IDs to one line each
    lines = re.sub(r'(\w)\n(\w)',r'\g<1> \g<2>',lines)
    
    #remove extra line breaks
    lines = re.sub(r'\n\n',r'\n',lines)
    return lines.split('\n')

def part1():
    lines = load()
    ids = 0
    for line in lines:
        print(line)
        passport = fieldExtractor(line)
        if validatorV1(passport):
            ids += 1

    print(ids)

def part2():
    lines = load()
    ids = 0
    for line in lines:
        print(line)
        passport = fieldExtractor(line)
        if validatorV2(passport):
            ids += 1

    print(ids)

part1()
part2()