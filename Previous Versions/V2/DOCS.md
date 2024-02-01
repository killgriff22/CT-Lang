----NEED TO KNOW
any instruction (other that PEND) that DOESNT take an argument MUST have "-" as an argument<br>
in order for it to be correctly executed<br>
--<br>
For JUMP, the "address" it jumps to is notaed by the line, or index in the "addresses" list<br>
----Special instructions<br>
PEND -- Program End<br>
PY -- Run python code that can extend the language.<br>
PRINTA -- prints the value in the A_Register. Syntax (-)<br>
PRINTB -- prints the value in the B_Register. Syntax (-)<br>
AINT -- casts the value in the A_Register to int. Syntax (-)<br>
ASTR -- casts the value in the B_Register to str. Syntax (-)<br>
BINT -- casts the value in the B_Register to int. Syntax (-)<br>
BSTR -- casts the value in the B_Register to str. Syntax (-)<br>
FUNC -- Creates a new instruction. Syntax (Name, Pointer)<br>
Make sure that you call JUMPA at the end of the instruction so that you can return to normal<br>
operation<br>
CALL -- Calls a created instruction. Syntax (Name, Argument)<br>
IMPORT -- Runs another file on disk and returns to the original file at PEND<br>
EXTERNAL FUNCTIONS SHOULD BE ENDED WITH PEND, NOT JUMPA <br>
----Standard instructions<br>
NOOP -- NOOP - NO OPERATION. Syntax (-)<br>
LOADA -- Load Address into A. Syntax (Instrcution, Address)<br>
INAI -- Load Int into A. Syntax (Instrcution, Int)<br>
INAS -- Load String into A. Syntax (Instrcution, String) DOES NOT USE QUOTATION MARKS<br>
LOADB -- Load Address into B. Syntax (Instrcution, Address)<br>
INBI -- Load Int into B. Syntax (Instrcution, Int)<br>
INBS -- Load String into B. Syntax (Instrcution, String) DOES NOT USE QUOTATION MARKS<br>
B+A -- Add A to B. Syntax (-)<br>
A+B -- Add B to A. Syntax (-)<br>
B-A -- Sub A from B. Syntax (-)<br>
A-B -- Sub B from A. Syntax (-)<br>
JUMP -- Set program counter to new value and stop processing current instruction. Syntax (Address)<br>
JUMPA -- Set program counter to Value in A register and stop processing. Syntax (-)<br>
JUMPB -- Set program counter to Value in B register and stop processing. Syntax (-)<br>
CJUMP -- Conditional jump, compares A and B Registers. Syntax ([<,>,=,!=,<=,>=,!>,!<,!<=,!>=], Address)<br>
It always compares A register first (Ex. A_Register > B_Register)<br>
----Comments<br>
Comments are plain text and should not be run, is they are, you likely have put CTFF of an<br>
instruction into your comment.<br>
----Python<br>
Python code can be run, allowing for extension of the language<br>
There is an existing function (func()) inside the interpreter that you can target using the<br>
PY instruction and every time the cycle the function will be executed.<br>
You can also use the Python interpreter to import custom libraries, and you can<br>
use the code inside them by overwriting func() function
