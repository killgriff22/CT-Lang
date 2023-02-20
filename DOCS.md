----NEED TO KNOW
any instruction (other that PEND) that DOESNT take an argument MUST have "-" as an argument
in order for it to be correctly executed
--
For JUMP, the "address" it jumps to is notaed by the line, or index in the "addresses" list
----Special instructions
PEND -- Program End
PY -- Run python code that can extend the language
PRINTA -- prints the value in the A_Register
PRINTB -- prints the value in the B_Register
AINT -- casts the value in the A_Register to int
ASTR -- casts the value in the B_Register to str
BINT -- casts the value in the B_Register to int
BSTR -- casts the value in the B_Register to str
----Standard instructions
NOOP -- NOOP - NO OPERATION
LOADA -- Load Address into A {instrcution, address}
INAI -- Load Int into A {instrcution, Int}
INAS -- Load String into A {instrcution, String} DOES NOT USE QUOTATION MARKS
LOADB -- Load Address into B {instrcution, address}
INBI -- Load Int into B {instrcution, Int}
INBS -- Load String into B {instrcution, String} DOES NOT USE QUOTATION MARKS
B+A -- Add A to B
A+B -- Add B to A
B-A -- Sub A from B
A-B -- Sub B from A
JMP -- Set program counter to new value and stop processing current instruction
JMPA -- Set program counter to Value in A register and stop processing
JMPB -- Set program counter to Value in B register and stop processing
----Comments
Comments are plain text and should not be run, is they are, you likely have put CTFF of an
instruction into your comment.
----Python
Python code can be run, allowing for extension of the language
There is an existing function (func()) inside the interpreter that you can target using the
PY instruction and every time the cycle the function will be executed.
You can also use the Python interpreter to import custom libraries, and you can
use the code inside them by overwriting func() function