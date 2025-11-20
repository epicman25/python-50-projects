# Build a Simple Blockchain

**Difficulty Level:** Advanced (Est. 4-6 Hours)

## Project Description
A capstone project in pure Python and OOP. Create a `Block` class (attributes: index, timestamp, data, previous_hash, hash) and a `Blockchain` class (attributes: a list of Blocks). Implement a proof_of_work algorithm (e.g., finding a hash that starts with "0000") and a `hash_block` method. This demonstrates a deep understanding of OOP and cryptographic concepts.

## Possible Folder Structure
```
py_chain/
├── main.py         # (Runs simulation)
├── block.py        # (Block class)
├── blockchain.py   # (Blockchain class)
└── requirements.txt
```

## Inputs and Expected Outputs
- **Input:** (In main.py) `my_chain.add_block("Transaction 1")`, `my_chain.add_block("Transaction 2")`
- **Output:** The script prints the entire valid, hashed blockchain to the console, showing the linked "previous_hash" values

## Learning Objectives
- Blockchain fundamentals
- Cryptographic hashing
- Proof of work algorithms
- Advanced OOP design
- Distributed systems concepts
