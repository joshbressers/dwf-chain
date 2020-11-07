# This module is meant to be a driver that allows a blockchain to be saved
# to disk or some other data storage destination.
#
# The default storage format is shelve because it's easy
#

import shelve
from .block import *

class DB:

    def __init__(self, the_db):

        self.db_file = the_db

        self.db = shelve.open(self.db_file)

    def add_chain(self, the_chain):

        the_block = the_chain.get_genesis()

        while(True):

            self.db[the_block.id] = the_block.get_json()
            self.db[the_block.get_hash()] = the_block.get_id()

            the_block = the_block.get_next()
            if the_block is None:
                # We're at the end
                break

    def close(self):
        self.db.close()

    def load_by_id(self, block_id):

        the_block = load_json(self.db[block_id])
        return the_block

    def load_by_hash(self, block_hash):

        the_id = self.db[block_hash]
        return self.load_by_id(the_id)
