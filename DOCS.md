----NEED TO KNOW
any instruction (other that PEND) that DOESNT take an argument MUST have "-" as an argument<br>
in order for it to be correctly executed<br>
The code has been optimized for dynamic variables, having said that, JUMPA is still used for returning from functions.<br>
--<br>
For JUMP, the "address" it jumps to is notaed by the line, or index in the "addresses" list<br>
----Special instructions<br>
PEND -- Program End<br>
PY -- Run python code that can extend the language.<br>
PRINT -- prints the value in the variable specified or prints the data specified. Syntax (VariableName/Data)<br>
INT -- casts the value in the specified variable to int. Syntax (-)<br>
STR -- casts the value in the specified variable to str. Syntax (-)<br>
FUNC -- Creates a new instruction. Syntax (Name, Pointer)<br>
Make sure that you call JUMPA at the end of the function so that you can return to normal execution<br>
CALL -- Calls a created instruction. Syntax (Name, Argument)<br>
IMPORT -- Runs another file on disk and returns to the original file at PEND<br>
EXTERNAL FUNCTIONS SHOULD BE ENDED WITH PEND, NOT JUMPA <br>
----Standard instructions<br>
NOOP -- NOOP - NO OPERATION. Syntax (-)<br>
LOAD -- Load Address into given variable. Syntax (VariableName, Address: VariableName/Int)<br>
IN -- Take user input into a given variable. Syntax (VariableName, Type (int/str/bool), Prompt: VariableName/Str)
INAS -- Load String into A. Syntax (Instrcution, String) DOES NOT USE QUOTATION MARKS<br>
ADD -- Add A to B. Syntax (A: VariableName/Int,B: VariableName/Int)<br>
SUB -- Subtract B from A. Syntax (A: VariableName/Int,B: VariableName/Int)<br>
JUMP -- Set program counter to new value and stop processing current instruction. Syntax (Address: VariableName/Int)<br>
JUMPA -- Set program counter to Value in A register and stop processing. Syntax (-)<br>
CJUMP -- Conditional jump, compares A and B Syntax (A: VariableName/Int/Str, [<,>,=,!=,<=,>=,!>,!<,!<=,!>=], B: VariableName/Int/Str, Address)<br>
It always compares A first (Ex. A > B)<br>
----Comments<br>
Comments are plain text and should not be run<br>
----Python<br>
Python code can be run, allowing for extension of the language<br>
There is an existing function (func()) inside the interpreter that you can target using the<br>
PY instruction and every instruction cycle the function will be executed.<br>
You can also use the Python interpreter to import custom libraries, and you can<br>
use the code inside them by overwriting func() function
