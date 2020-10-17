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

Every block can have multiple children. We can have a system where every
vuln type has a "root" block that's tied to the primary chain. Then every
vuln database is part of its own chain. Every block can multiple children

For example

CVE-1 -> child metadata -> more metadata
 |   \
 |    \ --- child metadata
 v
CVE-2

Everything can be easily traced back to the root block for verification

Maybe do something clever with signatures to specify which bits of metadata
are associated wtih a specific group or person

Store the public keys in a different tree
