#!/bin/env python

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

import vuln_chain
import time
import tempfile


class TestDB(unittest.TestCase):

    def setUp(self):

        the_time = time.time()

        self.the_block = vuln_chain.Block('id', 0, None)
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

        a_block = the_db.load_by_id(self.second_block.get_id())
        self.assertEqual(a_block, self.second_block)

        a_block = the_db.load_by_id(self.third_block.get_id())
        self.assertEqual(a_block, self.third_block)

    def test_write_block(self):

        tempdb = os.path.join(self.tempdir.name, 'test_db')

        # Open DB
        the_db = vuln_chain.DB(tempdb)

        # Write blocks
        the_db.add_block(self.the_block)

        # Close the DB
        the_db.close()

        # Open the DB
        the_db = vuln_chain.DB(tempdb)

        # Read in a block
        a_block = the_db.load_by_id(self.the_block.get_id())
        self.assertEqual(a_block, self.the_block)

        with self.assertRaises(Exception) as context:
            a_block = the_db.load_by_id(self.second_block.get_id())


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


    def test_child(self):

        tempdb = os.path.join(self.tempdir.name, 'test_db')

        # Open DB
        the_db = vuln_chain.DB(tempdb)

        # Write chain
        the_db.add_chain(self.the_block)

        # add some children
        child1 = vuln_chain.Block('child1', 0, None, parent = self.the_block)
        child2 = vuln_chain.Block('child2', 0, None, parent = self.the_block)
        child3 = vuln_chain.Block('child3', 0, None, parent = self.the_block)

        the_db.add_block(child1)
        the_db.add_block(child2)
        the_db.add_block(child3)

        # Close the DB
        the_db.close()

        # Open the DB
        the_db = vuln_chain.DB(tempdb)

        # Read in a block
        child_blocks = the_db.load_by_parent(self.the_block.get_hash())

        print(child_blocks)

        self.assertTrue(child1 in child_blocks)
        self.assertTrue(child2 in child_blocks)
        self.assertTrue(child3 in child_blocks)

if __name__ == '__main__':
    unittest.main()

