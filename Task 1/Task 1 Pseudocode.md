# Task 1 Pseudocode
## Task 1.1
```pseudocode
TYPE Books
    DECLARE id : INTEGER[100..999]
    # Store unique code for each book
    DECLARE title : STRING
    # Store title of the book
    DECLARE author : STRING
    # Store main author
    DECLARE year : INTEGER
    # Store year of publication
ENDTYPE
```

## Task 1.7
Write a pseudocode algorithm to perform the hash calculation.  
```pseudocode
FUNCTION hash_code(code:INTEGER) RETURNS INTEGER
    exp <- code * code * code
    hash_val <- MID(STRING(exp), 3, 5)
    RETURN hash_val 
```

## Task 1.8
Write a pseudocode algorithm to store a record in its hashed location in the random file.  
```pseudocode
OPENFILE "Task 1 random.bin" FOR RANDOM
address <- hash_code(newbook.get_id)
SEEK "Task 1 random.bin", address
PUTRECORD "Task 1 random.bin", newbook
CLOSEFILE "Task 1 random.bin"
```

## Task 1.9
Write a pseudocode algorithm to read a record from its hashed location in the random file.
```pseudocode
OPENFILE "Task 1 random.bin" FOR RANDOM
address <- hash_code(newbook.get_id)
SEEK "Task 1 random.bin", address
GETRECORD "Task 1 random.bin", newbook
CLOSEFILE "Task 1 random.bin"
```