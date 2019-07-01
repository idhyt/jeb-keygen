#! /usr/bin/env python
# -*- coding: cp936 -*-

#
# Copyleft (c) 2014, 2025
# ------------------------------------------------------------------------
# Author      : CodeColorist
#             : https://gist.github.com/ChiChou/6a6427068965752c3c7b
# Original    : quard@pediy
#             : wangshy@pediy
#             : scz
#             : http://scz.617.cn/misc/201507251700.txt
#             : http://scz.617.cn/misc/201507271722.txt
#             : http://scz.617.cn/misc/201507281725.txt
#             :
# Create      : 2014-04-23 17:01
# Modify      : 2015-07-28 17:25
# ------------------------------------------------------------------------
# The only thing they can't take from us are our minds. !H
#

import struct, time, hashlib, platform, re, subprocess

def License_GetSerialNumber () :
    system  = platform.system()
    ctrl    =   \
    {
        'Windows'   :
        [
            'wmic bios get serialnumber',
            r'SerialNumber\s+(\S+)\s+'
        ],
        'Darwin'    :
        [
            'ioreg -l',
            r'"IOPlatformSerialNumber" = "(\S+)"'
        ],
        'Linux'     :
        [
            'cat /var/lib/dbus/machine-id',
            r'(\S+)'
        ]
    }
    if system in ctrl :
        command, regular    \
                    = ctrl[system]
        p           = subprocess.Popen  \
        (
            command.split( ' ' ),
            stdin   = subprocess.PIPE,
            stdout  = subprocess.PIPE,
            stderr  = subprocess.PIPE
        )
        out, err    = p.communicate()
        if not err :
            return( re.search( regular, out, re.S ).group( 1 ) )
        else:
            raise Exception( "Failed to retrieve serial number.\n%s" % err )
    else :
        raise Exception( "OS not supported." )
#
# end of License_GetSerialNumber
#


def License_sum ( val ) :
    i   = 0
    while val > 0 :
        i      += ( val & 0xF )
        val   >>= 4
    #
    # end of while
    #
    return( i % 10 )
#
# end of License_sum
#

def License_GetMachineId ( SerialNumber ) :
    md5     = hashlib.md5()
    md5.update( SerialNumber )
    digest  = md5.digest()
    return( struct.unpack( '<Q', digest[:8] )[0] )
#
# end of License_GetMachineId
#

def License_GetMachineId_2 ( MachineId ) :
    low     = MachineId & 0xFFFFFFFF
    high    = MachineId >> 32
    n       = low + 376273029 + 287454020 & 0xFFFFFFFF
    m       = high - 52416167 + 1432778632 & 0x7FFFFFFF
    buf     = struct.pack( '>LL', m, n )
    return( struct.unpack( '>Q', buf )[0] )
#
# end of License_GetMachineId_2
#

def License_GenerateKey ( MachineId, timestamp ) :
    l   = License_GetMachineId_2( MachineId )
    t   = timestamp & 0xFFFFFFFF ^ 0x56739ACD
    return( '%dZ%d%d' % ( l, t, License_sum( t ) ) )
#
# end of License_GenerateKey
#

def main () :
    SerialNumber    = License_GetSerialNumber()
    MachineId       = License_GetMachineId( SerialNumber )
    timestamp       = int( time.time() + 86400 * 365 * 100 )
    ret             =   \
    "SerialNumber    : %s\n"    \
    "MachineId       : %x\n"    \
    "MachineId_2     : %x\n"    \
    "License key     : %s"      \
    %   \
    (
    SerialNumber,
    MachineId,
    License_GetMachineId_2( MachineId ),
    License_GenerateKey( MachineId, timestamp )
    )
    print ret
#
# end of main
#

if __name__ == '__main__' :
    main()