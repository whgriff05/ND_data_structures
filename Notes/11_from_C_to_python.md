# From C to Python

## Review a Dynamic Array from C
```C
typedef struct {
    int *data;
    int capacity;
    int size;
} Array;

Array* array_create();
void array_delete(Array *array);
void array_append(Array *array, int val);
int array_at(Array *array, int index);
int array_index(Array *array, int val);
void array_insert(Array *array, int val, int index);
```
Separate functions from the `Array` struct, all need the array pointer passed to it\
C is __not__ an object-oriented language

## Dynamic Array in C++
```C++
class Array {
private:
    int *data;
    int capacity;
    int size;

public:
    Array();
    ~Array();

    void append(int val);
    int at(int index);
    int index_of(int val);
    void insert(int val, int index);
    int get_size();
}
```

Functions are within the `Array` class, no need to pass the array pointer to them\
C++ is an object-oriented language

```C++
Array arr;

arr.append(10);
arr.append(20);

int x = arr.at(1);

std::cout << "arr[1]: " << x << std::end;
```

## Attributes of Object-Oriented Languages
__abstraction__ - hiding private/implementation details, exposing public interface through methods

__inheritance__ - child class takes methods and attributes from a parent class

__polymorphism__ - type-specific methods with the same name

