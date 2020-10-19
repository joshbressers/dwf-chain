# Initial library to build a blockchain and use it
#

import hashlib

class Block:

    def __init__(self, id, date, previous, hash = None, data = ''):
        self.id = id
        self.date = date
        self.data = data
        self.previous_hash = previous
        self.hash = hash
        self.calculated_hash = None
        self.children = []

        self.prev = None
        self.next = None

    def get_date(self):
        return self.date

    def get_id(self):
        return self.id

    def get_prev_hash(self):
        return self.previous_hash

    def get_hash(self):
        return self.hash

    def gen_hash(self, update = False):
        sha = hashlib.sha512()

        # The variables we need to calculate are
        # id
        # date
        # prev

        sha.update(bytearray(self.id, 'utf8'))
        # Let's just convert the date to a string
        sha.update(bytearray(str(self.date), 'utf8'))
        sha.update(bytearray(str(self.data), 'utf8'))
        sha.update(bytearray(self.previous_hash, 'utf8'))

        if update is True:
            self.hash = sha.hexdigest()

        return sha.hexdigest()


    def verify(self, all=False):

        verified_return = False

        if all is True:
            # We have to verify all the blocks going bakcwards

            current_block = self

            # We can't use recursion here because if we have to traverse
            # thousands of blocks, we will end up with a stack overflow
            # error
            while(True):
                if current_block.verify() is False:
                    break;

                current_block = current_block.get_prev()

                # If we hit the None block, we made it to the beginning
                if current_block is None:
                    verified_return = True
                    break

        else:
            calculated_hash = self.gen_hash()

            if calculated_hash == self.hash:
                verified_return = True

        return verified_return

    def add_next(self, id, date, data = ''):
        next_block = Block(id, date, self.get_hash())
        next_block.gen_hash(update = True)

        self.next = next_block
        next_block.prev = self

        return next_block

    def add_child(self, id, date, data = ''):
        child = Block(id, date, self.get_hash())
        child.gen_hash(update = True)

        self.children.append(child)
        child.prev = self

        return child

    def get_children(self):
        return self.children

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
