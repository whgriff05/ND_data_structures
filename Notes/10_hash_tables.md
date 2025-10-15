# Hash Tables

Let's say we want to have an employee record database. Each entry will have two pieces of data, a numeric id and a name\
The operations we want to use with this database are insert and look up by id


__Is there a way to insert and look up in O(1)?__\
__Yes__, use the id as the index

However, this takes a __lot__ of storage, so let's try and separate these ids into buckets\
This separation is called a __hash function__ and introduces the idea of a __hash table__

What if we wanted to use the name as the key?
- first letter (26 buckets)
- first two letters of last name (26^2 buckets)
- somehow convert the string to a really big integer
- sum of ascii characters (n * 26 buckets)

### Collisions
If two elements are in the same bucket, how do we know which one we want?

Have each bucket be the head of a __linked list__ and when a new element is added to an already-populated bucket, add the new element onto the end of its linked list\
This technique is called __chaining__

The hash function determines how many collisions will happen

### Load Factor and Resizing

__Load Factor__ - the ratio of number of entries/records to the capacity
- size over number of buckets
- __α__ is the __trigger load factor__ for resizing (typically 0.5)

Resizing doubles the number of buckets and rehashing the values with a larger hash function, reducing number of collisions and the load factor

## Hash Table Structure

### Pair
```C
typedef struct {
    char *key;
    int value;
    Pair *next;
} Pair;
```

### Table
```C
typedef struct {
    Pair **buckets;
    int capacity;
    int size;
} Table;
```

## Linear Probing

An alternative to __chaining__ that does not use linked lists in the hash table, instead uses a dynamic array

Each bucket is just a number, but if a collision occurs, the value to be inserted is just inserted at the next possible index

## Hash Functions

- Use some multiplication by a large/randomish number, take N number of middle bits
- Shift x to the left (multiples by 2 in binary)
- Hash a string with this recursive formula for each char: `hash = 33 * hash + char` (same as `(hash << 5 + 1) + char`)

## Numbers of Buckets

The number of buckets in a hash table can also lessen the number of collisions

zyBooks says always use a prime number of buckets\
Convention: use a power of 2 because it is easy to work with




