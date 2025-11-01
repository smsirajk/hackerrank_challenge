"""
Title     : Re.split()
Subdomain : Regex and Parsing
Domain    : Python
Author    : smsirajk
Created   : 15 July 2016
Updated   : 3 April 2021
Problem   : https://www.hackerrank.com/challenges/re-split/problem
"""

import re

regex_pattern = r"[.,]+"

print("\n".join(re.split(regex_pattern, input())))
