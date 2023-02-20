----NEED TO KNOW
any instruction (other that CTFF) that DOESNT take an argument MUST have "-" as an argument
in order for it to be correctly executed
--
For CTJJ, the "address" it jumps to is notaed by the line, or index in the "addresses" list
----Special instructions
CTFF -- Program End
CTPP -- Run python code that can extend the language
CTPA -- prints the value in the A_Register
CTPB -- prints the value in the B_Register
CTAI -- casts the value in the A_Register to int
CTAS -- casts the value in the B_Register to str
CTBI -- casts the value in the B_Register to int
CTBS -- casts the value in the B_Register to str
----Standard instructions
CT00 -- NOOP - NO OPERATION
CTA1 -- Load Address into A {instrcution, address}
CTA2 -- Load Int into A {instrcution, Int}
CTA3 -- Load String into A {instrcution, String} DOES NOT USE QUOTATION MARKS
CTB- -- Same as A, but for B
CTC1 -- Add A to B
CTC2 -- Add B to A
CTC3 -- Sub A from B
CTC4 -- Sub B from A
CTJJ -- Set program counter to new value and stop processing current instruction
CTJA -- Set program counter to Value in A register and stop processing
CTJB -- Set program counter to Value in B register and stop processing
----Comments
Comments are plain text and should not be run, is they are, you likely have put CTFF of an
instruction into your comment.
----Python
Python code can be run, allowing for extension of the language
There is an existing function (func()) inside the interpreter that you can target using the
CTPP instruction and every time the cycle the function will be executed.
You can also use the Python interpreter to import custom libraries, and you can
use the code inside them by overwriting func() function