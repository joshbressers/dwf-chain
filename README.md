# dwf-chain
A chain of vulnerability info

Someday this will have more things, but CVE info is an easy place ot start as it's very public and very JSON

# The chain

There will be a primary chain. Every block on the main chain will have a
child chain. Everything will be json data.

The primary chain will contain

id
date
previous
hash

The child chains can contain anything.

ID ----> ID ----> ID
         \        \
          \        -> Data
           -> Data

