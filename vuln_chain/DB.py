# This module is meant to be a driver that allows a blockchain to be saved
# to disk or some other data storage destination.
#
# The default storage format is dbm because it's easy
#

import os
import dbm
import json
from .block import *

class DB:

    def __init__(self, the_db):

        self.db_file = the_db

        if os.path.exists(self.db_file):
            self.db = dbm.open(self.db_file)
        else:
            self.db = dbm.open(self.db_file, 'c')

    def add_chain(self, the_chain):

        if not the_chain.verify():
            raise Exception("The chain failed to verify")

        the_block = the_chain.get_genesis()

        while(True):

            self.add_block(the_block)

            the_block = the_block.get_next()
            if the_block is None:
                # We're at the end
                break

    def add_block(self, the_block):

        if not the_block.verify():
            raise Exception("The block failed to verify")

        # We add these identifiers to avoid any possible collisions
        # where id is the same as a valid hash
        store_id = "id:%s" % the_block.get_id()
        store_hash = "hash:%s" % the_block.get_hash()
        parent_hash = "parent:%s" % the_block.get_parent()

        self.db[store_id] = the_block.get_json()

        # We also need to store a mapping from the hash to the ID
        self.db[store_hash] = the_block.get_id()

        if parent_hash in self.db:
            the_ids = json.loads(self.db[parent_hash])
            the_ids.append(the_block.get_hash())
            self.db[parent_hash] = json.dumps(the_ids)
        else:
            the_ids = [the_block.get_hash()]
            self.db[parent_hash] = json.dumps(the_ids)

    def close(self):
        self.db.close()

    def load_by_id(self, block_id):

        # Sometimes we get bytes back
        if type(block_id) is bytes:
            block_id = block_id.decode()

        store_id = "id:%s" % block_id

        the_block = load_json(self.db[store_id])
        return the_block

    def load_by_hash(self, block_hash):

        store_hash = "hash:%s" % block_hash
        the_id = self.db[store_hash]

        return self.load_by_id(the_id)

    def load_by_parent(self, parent_hash):

        found_blocks = []

        parent_hash = "parent:%s" % parent_hash
        if parent_hash in self.db:
            the_ids = json.loads(self.db[parent_hash])

            for i in the_ids:
                found_blocks.append(self.load_by_hash(i))

        return found_blocks
