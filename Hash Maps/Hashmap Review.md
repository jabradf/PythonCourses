##Review
We’ve learned together what a hash map is and how to create one. Let’s go over the concepts presented in this lesson.

A hash map is:

* Built on top of an array using a special indexing system.
* A key-value storage with fast assignments and lookup.
* A table that represents a map from a set of keys to a set of values.

Hash maps accomplish all this by using a hash function, which turns a key into an index into the underlying array.

A hash collision is when a hash function returns the same index for two different keys.

There are different hash collision strategies. Two important ones are separate chaining, where each array index points to a different data structure, and open addressing, where a collision triggers a probing sequence to find where to store the value for a given key.