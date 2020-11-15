# vuln-chain
A chain of vulnerability info

Someday this will have more things, but CVE info is an easy place ot start as it's very public and very JSON

The idea is there will be no "official" chain. Every user adds a link to
chains of their choosing. There will also be no p2p network. All imported
chains are read only. Chain locations will be URLs. Any block can refer to
any other block and be viewed as a way to enrich their data.

For example we could have a CVE chain and an NVD chain. The NVD chain can
include new details for different CVD IDs. How we incorporate the new and
old data may be a challenge. An example below

CVE-1900-0001v1 -----> CVE-1900-0001v2
       ^
       |
    NVD-1900-0001

We will rever to the blocks in a singular chain as next and previous. The
genesis block of every chain has no previous.

The blocks that rever to other blocks not in their chain (like the NVD
block above) will be child blocks. So a block can have zeor or one parent.
A block can also have zero or many children.

How should the data look after we apply the v2 update and the new NVD data?

# The chain

There is no primary chain, this shold be viewed as a collection of
arbitrary chains. A block can be pointed to by any other block. Every chain
has a specific sequence of blocks, but those blocks may refer to other
blocks on any chain. Everything will be json data.

Every block will contain

id
date
previous
hash
data

Everything can be easily traced back to the root block for verification
