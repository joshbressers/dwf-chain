#!/bin/env python

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

import vuln_chain
import time


class TestBlock(unittest.TestCase):

    def setUp(self):

        self.hash = "ec81332e528ff522bfb05e93cd826c075ec26c5b9cc5bfcf7087d6f28da90e1d4f44df2a9af32573df5ab535d4b985731001c71d9f7629170518bba95280ef3d"

        self.the_block = vuln_chain.Block('id', 0, 'prev_hash', self.hash)

    def test_create(self):
        the_block = vuln_chain.Block('id', 0, 'prev_hash', 'hash')

        self.assertEqual(the_block.get_date(), 0, "Should be 0")
        self.assertEqual(the_block.get_id(), 'id', "Should be 'id'")
        self.assertEqual(the_block.get_prev_hash(), 'prev_hash', "Should be 'prev_hash'")
        self.assertEqual(the_block.get_hash(), 'hash', "Should be 'hash'")

    def test_hash(self):

        output = self.the_block.gen_hash()

        self.assertEqual(output, self.hash, "Should be '%s'" % self.hash)

    def test_genesis(self):

        the_block = vuln_chain.Block('id', 0, None)
        the_block.gen_hash(update=True)

        self.assertEqual(the_block.get_prev(), None)

    def test_verify(self):

        self.assertTrue(self.the_block.verify())

        the_block = vuln_chain.Block('id', 0, 'prev_hash', 'bad_hash')
        self.assertFalse(the_block.verify())

    def test_next(self):

        the_block = self.the_block
        the_time = time.time()

        the_block.add_next('id2', the_time)

        next_block = the_block.get_next()

        self.assertTrue(next_block.verify())

    def test_prev(self):

        the_block = self.the_block
        the_time = time.time()

        the_block.add_next('id2', the_time)

        next_block = the_block.get_next()

        self.assertEqual(next_block.get_prev(), the_block)

    def test_data(self):

        the_block = self.the_block
        the_time = time.time()

        next_block = the_block.add_next('id2', the_time, data = "Secret data")

        self.assertTrue(next_block.verify())

    def test_verify_chain(self):

        the_block = self.the_block
        the_time = time.time()

        second_block = the_block.add_next('id2', the_time, data = "Secret data2")
        third_block = second_block.add_next('id3', the_time, data = "Secret data3")


        self.assertTrue(second_block.verify())
        self.assertTrue(third_block.verify())
        self.assertTrue(third_block.verify(all=True))

        second_block.id = "bad_id"
        self.assertFalse(second_block.verify())
        self.assertFalse(third_block.verify(all=True))

    def test_child(self):

        the_block = self.the_block
        the_time = time.time()

        second_block = the_block.add_next('id2', the_time, data = "Secret data2")
        third_block = second_block.add_next('id3', the_time, data = "Secret data3")

        second_child = second_block.add_child("id_child2", the_time, data = "child data")
        third_child = third_block.add_child("id_child3", the_time, data = "child data")


        self.assertTrue(second_block.verify())
        self.assertTrue(third_block.verify())
        self.assertTrue(third_block.verify(all=True))

        self.assertIn(second_child, second_block.get_children())
        self.assertIn(third_child, third_block.get_children())

    def test_get_first(self):

        the_block = self.the_block
        the_time = time.time()

        second_block = the_block.add_next('id2', the_time, data = "Secret data2")
        third_block = second_block.add_next('id3', the_time, data = "Secret data3")

        first_block = third_block.get_genesis()

        self.assertEqual(first_block, the_block)

if __name__ == '__main__':
    unittest.main()

