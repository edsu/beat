#!/usr/bin/env python

"""
give this script a batch of LC MARC data and it will return 
some "triples" about the relationship between the MARC record
and other web resources.
"""

import sys
import re
import pymarc

def lccn_uri(lccn):
    lccn = lccn.replace(' ', '')
    if '/' in lccn:
        lccn = lccn[0:lccn.find('/')]
    if '-' in lccn:
        pre, post = lccn.split('-')
        try:
            lccn = "%s%0i" % (pre, int(post))
        except:
            return None
    return "http://lccn.loc.gov/%s" % lccn 


for record in pymarc.MARCReader(file(sys.argv[1])):
    lccn = lccn_uri(record['001'].data)
    for field in record.get_fields('856'):
        if field['3']:
            print "%s\t%s\t%s" % (lccn, field['3'], field['u'])

