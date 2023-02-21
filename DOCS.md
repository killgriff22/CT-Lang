----NEED TO KNOW
any instruction (other that PEND) that DOESNT take an argument MUST have "-" as an argument
in order for it to be correctly executed
--
For JUMP, the "address" it jumps to is notaed by the line, or index in the "addresses" list
----Special instructions
PEND -- Program End
PY -- Run python code that can extend the language.
PRINTA -- prints the value in the A_Register. Syntax (-)
PRINTB -- prints the value in the B_Register. Syntax (-)
AINT -- casts the value in the A_Register to int. Syntax (-)
ASTR -- casts the value in the B_Register to str. Syntax (-)
BINT -- casts the value in the B_Register to int. Syntax (-)
BSTR -- casts the value in the B_Register to str. Syntax (-)
FUNC -- Creates a new instruction. Syntax (Name, Pointer)
Make sure that you call JUMPA at the end of the instruction so that you can return to normal
operation
CALL -- Calls a created instruction. Syntax (Name, Argument)
IMPORT -- Runs another file on disk and returns to the original file at PEND
EXTERNAL FUNCTIONS SHOULD BE ENDED WITH PEND, NOT JUMPA 
----Standard instructions
NOOP -- NOOP - NO OPERATION. Syntax (-)
LOADA -- Load Address into A. Syntax (Instrcution, Address)
INAI -- Load Int into A. Syntax (Instrcution, Int)
INAS -- Load String into A. Syntax (Instrcution, String) DOES NOT USE QUOTATION MARKS
LOADB -- Load Address into B. Syntax (Instrcution, Address)
INBI -- Load Int into B. Syntax (Instrcution, Int)
INBS -- Load String into B. Syntax (Instrcution, String) DOES NOT USE QUOTATION MARKS
B+A -- Add A to B. Syntax (-)
A+B -- Add B to A. Syntax (-)
B-A -- Sub A from B. Syntax (-)
A-B -- Sub B from A. Syntax (-)
JUMP -- Set program counter to new value and stop processing current instruction. Syntax (Address)
JUMPA -- Set program counter to Value in A register and stop processing. Syntax (-)
JUMPB -- Set program counter to Value in B register and stop processing. Syntax (-)
----Comments
Comments are plain text and should not be run, is they are, you likely have put CTFF of an
instruction into your comment.
----Python
Python code can be run, allowing for extension of the language
There is an existing function (func()) inside the interpreter that you can target using the
PY instruction and every time the cycle the function will be executed.
You can also use the Python interpreter to import custom libraries, and you can
use the code inside them by overwriting func() function