#!/bin/env python

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

import vuln_chain
import time
import tempfile


class TestShelve(unittest.TestCase):

    def setUp(self):

        self.hash = "ec81332e528ff522bfb05e93cd826c075ec26c5b9cc5bfcf7087d6f28da90e1d4f44df2a9af32573df5ab535d4b985731001c71d9f7629170518bba95280ef3d"

        the_time = time.time()

        self.the_block = vuln_chain.Block('id', 0, None, self.hash)
        self.second_block = self.the_block.add_next('id2', the_time, data = "Secret data2")
        self.third_block = self.second_block.add_next('id3', the_time, data = "Secret data3")

        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self):

        self.tempdir.cleanup()

    def test_lookup_id(self):

        tempdb = os.path.join(self.tempdir.name, 'test_db')

        # Open DB
        the_db = vuln_chain.DB(tempdb)

        # Write blocks
        the_db.add_chain(self.the_block)

        # Close the DB
        the_db.close()

        # Open the DB
        the_db = vuln_chain.DB(tempdb)

        # Read in a block
        a_block = the_db.load_by_id(self.the_block.get_id())

        self.assertEqual(a_block, self.the_block)

    def test_lookup_hash(self):

        tempdb = os.path.join(self.tempdir.name, 'test_db')

        # Open DB
        the_db = vuln_chain.DB(tempdb)

        # Write blocks
        the_db.add_chain(self.the_block)

        # Close the DB
        the_db.close()

        # Open the DB
        the_db = vuln_chain.DB(tempdb)

        # Read in a block
        a_block = the_db.load_by_hash(self.the_block.get_hash())

        self.assertEqual(a_block, self.the_block)


#    def test_chain(self):
#
#        # Write the chain
#        # Read the chain
#        # Verify the chain
#        # Check everything
#        self.assertTrue(False)
#
#    def test_child(self):
#
#        # write a chain with chidren
#        # Read it back in
#        # Verify
#        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()

