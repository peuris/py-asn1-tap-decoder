#!/home/billing/venv/bin python
# -*- coding: UTF-8 -*-

from operator import imod
from pyasn1.codec.ber import decoder

def main(source=None, tapversion=None):
    if not source: return False

    if not tapversion: return False

    if tapversion == '0301':
        import tap0301_py_classes as tap
    elif tapversion == '0302':
        import tap0302_py_classes as tap
    elif tapversion == '0303':
        import tap0303_py_classes as tap
    elif tapversion == '0304':
        import tap0304_py_classes as tap
    elif tapversion == '0309':
        import tap0309_py_classes as tap
    elif tapversion == '0310':
        import tap0310_py_classes as tap
    elif tapversion == '0311':
        import tap0311_py_classes as tap
    elif tapversion == '0312':
        import tap0312_py_classes as tap
    
    data = open(source, 'rb').read()
    msg, res = decoder.decode(data, tap.DataInterChange())
    return msg.prettyPrint()