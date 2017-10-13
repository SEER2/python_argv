#!/usr/bin/env python
# coding=utf-8
"""
Get Option from Command Example

bulid time: 20171014
author: seer
email: li1234567890li@yeah.et
website: http://molecule.site
license: BSD

Please feel free to use and modify this, but keep the above information. Thanks!
"""

import sys
import getopt

# define some global variables
command		= False
display_target	= False
target		= ""

# usage
def usage():
    """
    help
    """
    # program name and version
    print "NAME"
    print "\targv v0.0"
    # synopsis
    print
    print "SYNOPSIS"
    print "\targv.py [-hc] [-t target]"
    # description
    print
    print "DESCRIPTION"
    print "\targv.py gives an example of how to get option from command line"
    # option
    print
    print "OPTIONS"
    print "\t-h --help"
    print "\t\tDisplay this help."
    print "\t-c --command"
    print "\t\tUse command as a switch to display a message."
    print "\t-t --target"
    print "\t\tUse target to get value followed -t, then display it."
    # example
    print
    print "EXAMPLES"
    print "\targv.py -c"
    print "\targv.py --help"
    print "\targv.py -t haha"
    print "\targv.py -c -t 666"
    # author
    print
    print "AUTHOR"
    print "\tseer <li1234567890li@yeah.net>"

    sys.exit(0)

# main, read option and set global variables then choose func
def main():

    global command
    global display_target
    global target
    if not len(sys.argv[1:]):
        usage()

    # read the commandline options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hct:", \
	["help", "command", "target"])
    except getopt.GetoptError as err:
        print str(err)
	usage()

    for o, a in opts:
        print o, a
        if o in ("-h", "--help"):
	    usage()
	elif o in ("-c", "--command"):
	    command = True
	elif o in ("-t", "--target"):
	    target = a
	    display_target = True
	else:
	    assert False, "Unhandled Option"
	
    if command:
        func()

    if display_target:
        func_target()

def func():
    print "-c : Get command"

def func_target():
    global target
    print "-t: ", target

#
main()
