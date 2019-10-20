#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import platform

if platform.sys.platform.__contains__("win"):
    from Token import Token
else:
    from src.Token import Token

class AnaliseLexica(object):
    __hashTokens = {
        "int": Token("int", "int"),
        "float": Token("float", "float"),
        "bool": Token("bool", "bool"),
        "double": Token("double", "double"),
        "true": Token("double", "double"),
        "false": Token(),
        "if": Token(),
        "while": Token(),
        "break": Token(),
        "{": Token(),
        "}": Token(),
        "(": Token(),
        ")": Token(),
        "[": Token(),
        "]": Token(),
        ";": Token(),
        "=": Token(),
        "+": Token(),
        "<": Token(),
        ">": Token(),
        ">=": Token(),
        "<=": Token(),
        "!=": Token(),
        "==": Token()
    }
    __regex = re.compile('[{]|([a-z{A-Z]+[\s]+(([a-zA-Z]+[\s]*[\;])|(([a-zA-Z]+[\s]+)*[\=]+[\s]+(([0-9]+([\.][0-9]+)*['
                         '\;])|([a-zA-Z]+[\s]*[\;])|(([a-zA-Z]+|[0-9]+([\.][0-9]+)*)[\s]*([\+]|[\-]|[\*]|[\/])[\s]*(['
                         'a-zA-Z]+|[0-9]+([\.][0-9]+)*)[\;])))))|([a-zA-Z]+[\s]+[\(]+[\s](([a-zA-Z]+[\s][\)])|([a-zA-Z]+['
                         '\s]([<]|[>]|[>=]|[<=]|[!=]|[==])[\s]([a-zA-Z]+|[0-9]+)[\s][\)]))[\s]([\{]|[a-zA-Z]+[\;]))|(['
                         'a-zA-Z]+[\;])|[\}]')

