# Arrays of Strings

`char *string = "hello"`
- We can use `printf("%d\n", string);` to print
- Or, `puts(string)`

### Read a String Line-by-line
- Use `fgets` to read a string into a buffer
```C
char buffer[BUFSIZ];
while (fgets(buffer, BUFSIZ, stdin)) {
    process(buffer);
}
```
- `fgets` captures __newlines__ `\n`, we need to chomp those into __null characters__ `\0`

### Storing Multiple Strings
Let's say we have an array of strings "cat", "bird", and "mouse"
- In C, this is an array of pointers to these strings
- A variable declaration would look like `char **str_array`

How do we allocate and free this?
- `str_array` -> `calloc()` -> __heap__
- individual strings -> `strdup()` -> __heap__
- To free, free every individual string, then free `str_array`