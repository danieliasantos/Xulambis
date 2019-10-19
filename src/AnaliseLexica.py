#!/usr/bin/python
#-*- coding: utf-8 -*-
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
       "false",
       "if",
       "while",
       "break",
       "{",
       "}",
       "(",
       ")",
       "[",
       "]",
       ";",
       "=",
       "+",
       "<",
      ">",
       ">=",
      "<=",
      "!=": Token(),
       "==": Token("==", "==")
   }
