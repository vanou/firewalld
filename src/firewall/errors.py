#
# Copyright (C) 2010 Red Hat, Inc.
#
# Authors:
# Thomas Woerner <twoerner@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

ALREADY_ENABLED     =   11
NOT_ENABLED         =   12
COMMAND_FAILED      =   13
NO_IPV6_NAT         =   14
PANIC_MODE          =   15
ZONE_ALREADY_SET    =   16
UNKNOWN_INTERFACE   =   17
ZONE_CONFLICT       =   18
IMMUTABLE           =   19
BUILTIN_CHAIN       =   20
EBTABLES_NO_REJECT  =   21
NOT_OVERLOADABLE    =   22
NO_DEFAULTS         =   23
BUILTIN_ZONE        =   24
BUILTIN_SERVICE     =   25
BUILTIN_ICMPTYPE    =   26
NAME_CONFLICT       =   27
NAME_MISMATCH       =   28
PARSE_ERROR         =   29

INVALID_ACTION      =  100
INVALID_SERVICE     =  101
INVALID_PORT        =  102
INVALID_PROTOCOL    =  103
INVALID_INTERFACE   =  104
INVALID_ADDR        =  105
INVALID_FORWARD     =  106
INVALID_ICMPTYPE    =  107
INVALID_TABLE       =  108
INVALID_CHAIN       =  109
INVALID_TARGET      =  110
INVALID_IPV         =  111
INVALID_ZONE        =  112
INVALID_PROPERTY    =  113
INVALID_VALUE       =  114
INVALID_OBJECT      =  115
INVALID_NAME        =  116
INVALID_FILENAME    =  117
INVALID_DIRECTORY   =  118
INVALID_TYPE        =  119
INVALID_SETTING     =  120
INVALID_DESTINATION =  121

MISSING_TABLE       =  200
MISSING_CHAIN       =  201
MISSING_PORT        =  202
MISSING_PROTOCOL    =  203
MISSING_ADDR        =  204
MISSING_NAME        =  205
MISSING_SETTING     =  206

NOT_RUNNING         =  252
NOT_AUTHORIZED      =  253
UNKNOWN_ERROR       =  254

import sys

class FirewallError(Exception):
    mod = sys.modules[__module__]
    errors = dict([(getattr(mod,varname),varname)
                   for varname in dir(mod)
                   if not varname.startswith("_")])
    codes = dict([(errors[code],code) for code in errors])

    def __init__(self, code, msg=None):
        self.code = code
        self.msg = msg

    def __str__(self):
        if self.msg:
            return "%s: %s" % (self.errors[self.code], self.msg)
        return self.errors[self.code]

    def get_code(msg):
        if ":" in msg:
            idx = msg.index(":")
            ecode = msg[:idx]
        else:
            ecode = msg
        return FirewallError.codes[ecode]
    get_code = staticmethod(get_code)
