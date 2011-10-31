#! /usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
##                                                                           ##
##  Copyright 2011, Neil Wallace <rowinggolfer@googlemail.com>               ##
##                                                                           ##
##  This program is free software: you can redistribute it and/or modify     ##
##  it under the terms of the GNU General Public License as published by     ##
##  the Free Software Foundation, either version 3 of the License, or        ##
##  (at your option) any later version.                                      ##
##                                                                           ##
##  This program is distributed in the hope that it will be useful,          ##
##  but WITHOUT ANY WARRANTY; without even the implied warranty of           ##
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            ##
##  GNU General Public License for more details.                             ##
##                                                                           ##
##  You should have received a copy of the GNU General Public License        ##
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.    ##
##                                                                           ##
###############################################################################


from SimpleXMLRPCServer import SimpleXMLRPCServer

import commands
import datetime
import subprocess
import logging

HOST = commands.getoutput("hostname -I").split(" ")[0]

PORT = 42230

logger = logging.getLogger("openmolar_server")

class MyFuncs(object):
    '''
    A class whose functions will be inherited by the server
    '''
    def last_backup(self):
        '''
        returns a iso formatted datetime string showing when the
        last backup was made
        '''
        return datetime.datetime.now().isoformat()

    def init_db(self):
        '''
        initialises the database, creating a demo database, and default users
        '''
        logger.debug("init_db called")
        p = subprocess.Popen(["openmolar_initdb"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        p.wait()

        logger.debug(p.stdout.read())
        logger.error(p.stderr.read())

        return True

    def create_db(self, name):
        '''
        creates a database with the name given
        '''
        logger.info("TODO create_db function doesn't work!")

    def layout_schema(self, name):
        '''
        creates a blank openmolar table set in the database with the name given
        '''
        logger.info("TODO layout_schema function doesn't work!")


def main():

    server = SimpleXMLRPCServer((HOST, PORT))
    server.register_instance(MyFuncs())

    logger.debug("listening on %s:%d"% (HOST, PORT))
    server.serve_forever()

if __name__ == "__main__":

    main()