# py-asn1-tap-decoder
Python ans1 tap/rap decoder. Decodes ANS1 formated TAP 3.01- 3.12 versioned files into ascii format

## Getting Started
to use this repository, install required packages:

1. Python 3.9+
2. pyasn1==0.4.8

using the following command:
```
pip3 install -r requirements.txt
```
## Using
run convert.py

## create your own file handling logic
test_tap.ans is the default ans1 encoded binary formated file that you can use to test the script. You can build your own file prosessing logic and TAP processors with creating your own tap3 convert class. More details for creating processor: https://www.gsma.com/aboutus/workinggroups/interoperability-data-specifications-and-settlement-group/standardised-b2b-interfaces-specified-by-ids/open-standards-specifications
