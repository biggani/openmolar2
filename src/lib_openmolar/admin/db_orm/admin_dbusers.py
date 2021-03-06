#! /usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
##                                                                           ##
##  Copyright 2010-2012, Neil Wallace <neil@openmolar.com>                   ##
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

'''
This module provides the Demo User Queries
'''

from lib_openmolar.common.db_orm import InsertableRecord

TABLENAME = "dbusers"

class DemoGenerator(object):
    def __init__(self, database=None):
        self.database = database
        self.length = 1
        self.record = InsertableRecord(database, TABLENAME)

    def demo_queries(self):
        '''
        return a list of queries to populate a demo database
        '''

        self.record.setValue('username', 'admin')
        self.record.setValue('password', 'password')
        self.record.setValue('comments',
'''This user has full read/write create rights to all tables.
It should not be used by anyone who is not aware of the havoc they could
cause by disturbing the database. Whenever you connect with this user,
make sure you have a full backup.
Even qualified DBAs make unrecoverable mistakes occasionally.
Also - Do not remove this user!''')

        yield self.record.insert_query

if __name__ == "__main__":
    from lib_openmolar.admin.connect import DemoAdminConnection
    sc = DemoAdminConnection()
    sc.connect()

    builder = DemoGenerator(sc)
    print builder.demo_queries()
