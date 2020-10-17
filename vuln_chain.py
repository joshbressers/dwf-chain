# Initial library to build a blockchain and use it
#

import hashlib

class Block:

    def __init__(self, id, date, previous, hash = None):
        self.id = id
        self.date = date
        self.previous_hash = previous
        self.hash = hash
        self.calculated_hash = None

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

    def gen_hash(self):
        sha = hashlib.sha512()

        # The variables we need to calculate are
        # id
        # date
        # prev

        sha.update(bytearray(self.id, 'utf8'))
        # Let's just convert the date to a string
        sha.update(bytearray(str(self.date), 'utf8'))
        sha.update(bytearray(self.previous_hash, 'utf8'))

        return sha.hexdigest()


    def verify(self):
        calculated_hash = self.gen_hash()

        if calculated_hash == self.hash:
            return True
        else:
            return False

    def next(self):
        return self.next

    def prev(self):
        return self.prev

    def root(self):
        pass

    def last(self):
        pass
