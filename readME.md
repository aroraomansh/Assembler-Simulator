# Project Title

Short description or overview of the project.

## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Question Description](#question description)
  - [Deadlines](#deadlines)
  - [Instructions](#instructions)
  - [Screenshots](#screenshots)
  - [Contribution](#contribution)

## Introduction

Assignment

###CSE 112 Computer Organization
####Introduction and Instructions

● This will be a group assignment, each student in the group will be marked separately.
Therefore try to make sure that work is roughly divided equally among all the members
of the group.
● In this assignment, you will have to design and implement a custom assembler and a
custom simulator for a given ISA.
● You are not restricted to any programming language. However, your program must read
from stdin and write to stdout.
● You must use GitHub to collaborate. You must track your progress via git.
● The automated testing infrastructure assumes that you have a working Linux-based
shell. For those who are using Windows, you can either use a VM or WSL.
● TAs will conduct a separate session to explain the whole assignment. They will
also show you the sample solution code and will explain to you how to run the
automated testing scripts.
● Start the assignment early and ask the queries well in advance. Do not expect any reply
on weekends and 7 PM - 7 AM on working days. Do not escalate your query to
instructors directly. Write any queries you have in the comments section. Wait at
least 24 hours before any reply to your comment. If there is no reply then you can mail it
to the respective TAs if still there is no response, then mail the TFs, and if still there is no
response, then mail the instructors.
● No last-minute deadline extensions will be considered whatsoever. This includes
but is not limited to connectivity issues, one group member not working or not
cooperating, a group member is/are getting sick etc. The duration of the deadline is
sufficient enough to complete the assignment.
● Commit your code to the repository periodically to prevent any loss of your code due to
system failures or any other issues. In case of system failures of all the members of the
group, your last committed code on github before the deadline will be considered for
evaluation.

## Question Description
There are a total of four questions in this assignment:
1. Designing and Implementing the assembler.
2. Designing and Implementing the simulator.
3. Extending the functionality of the assembler-simulator set-up to handle simple
floating-point computations.
4. A bonus question based on the assembler and simulator.
The bonus will be worth 10%.

Questions:
Q1: Assembler:
Program an assembler for the aforementioned ISA and assembly. The input to the
assembler is a text file containing the assembly instructions. Each line of the text file may be of
one of 3 types:
● Empty line: Ignore these lines
● A label
● An instruction
● A variable definition
Each of these entities have the following grammar:
● The syntax of all the supported instructions is given above. The fields of an instruction
are whitespace separated. The instruction itself might also have whitespace before it. An
instruction can be one of the following:
○ The opcode must be one of the supported mnemonic.
○ A register can be one of R0, R1, … R6, and FLAGS.
○ A mem_addr in jump instructions must be a label.
○ A Imm must be a whole number <= 127 and >= 0.
○ A mem_addr in load and store must be a variable.
● A label marks a location in the code and must be followed by a colon (:). No spaces are
allowed between label name and colon(:)
● A variable definition is of the following format:
var xyz
which declares a 16 bit variable called xyz. This variable name can be used in
place of mem_addr fields in load and store instructions.
All variables must be defined at the very beginning of the assembly program.
The assembler should be capable of:
1) Handling all supported instructions
2) Handling labels
3) Handling variables
4) Making sure that any illegal instruction (any instruction (or instruction usage) which is not
supported) results in a syntax error. In particular you must handle:
a) Typos in instruction name or register name
b) Use of undefined variables
c) Use of undefined labels
d) Illegal use of FLAGS register
e) Illegal Immediate values (more than 7 bits)
f) Misuse of labels as variables or vice-versa
g) Variables not declared at the beginning
h) Missing hlt instruction
i) hlt not being used as the last instruction
You need to generate distinct readable errors for all these conditions. If you find any
other illegal usage, you are required to generate a “General Syntax Error”.
The assembler must print out all these errors.
5) If the code is error free, then the corresponding binary is generated. The binary file is a
text file in which each line is a 16bit binary number written using 0s and 1s in ASCII. The
assembler can write less than or equal to 128 lines.
Input/Output format:
● The assembler must read the assembly program as an input text file (stdin).
● The assembler must generate the binary (if there are no errors) as an output text file
(stdout).
● The assembler must generate the error notifications along with line number on which the
error was encountered (if there are errors) as an output text file (stdout). In case of
multiple errors, the assembler may print any one of the errors.
Example of an assembly program:
var X
mov R1 $10
mov R2 $100
mul R3 R2 R1
st R3 X
hlt
The above program will be converted into the following machine code
0001000100001010
0001001001100100
0011000011010001
0010101100000101
1101000000000000
Q2: Simulator:
You need to write a simulator for the given ISA. The input to the simulator is a binary
file (the format is the same as the format of the binary file generated by the assembler in Q1.
The simulator should load the binary in the system memory at the beginning, and then start
executing the code at address 0. The code is executed until hlt is reached. After execution of
each instruction, the simulator should output one line containing an 7 bit number denoting the
program counter. This should be followed by 8 space separated 16 bit binary numbers
denoting the values of the registers (R0, R1, … R6 and FLAGS).
<PC (7 bits)><space><R0 (16 bits)><space>...<R6 (16 bits)><space><FLAGS (16 bits)>.
The output must be written to stdout. Similarly, the input must be read from stdin. After
the program is halted, print the memory dump of the whole memory. This should be 128 lines,
each having a 16 bit value.
<16 bit data>
<16 bit data>
…..
<16 bit data>
Your simulator must have the following distinct components:
1. Memory (MEM): MEM takes in an 7 bit address and returns a 16 bit value as the data.
The MEM stores 256 bytes, initialized to 0s.
2. Program Counter (PC): The PC is an 7 bit register which points to the current instruction.
3. Register File (RF): The RF takes in the register name (R0, R1, … R6 or FLAGS) and
returns the value stored at that register.
4. Execution Engine (EE): The EE takes the address of the instruction from the PC, uses it
to get the stored instruction from MEM, and executes the instruction by updating the RF
and PC.
The simulator should follow roughly the following pseudocode:
initialize(MEM); // Load memory from stdin
PC = 0; // Start from the first instruction
halted = false;
while(not halted)
{
Instruction = MEM.fetchData(PC); // Get current instruction
halted, new_PC = EE.execute(Instruction); // Update RF compute new_PC
PC.dump(); // Print PC
RF.dump(); // Print RF state
PC.update(new_PC); // Update PC
}
MEM.dump() // Print the complete memory

## Deadlines
You will have two deadlines for this assignment:
1. The mid-evaluation:
a. By this deadline, you must have the assembler ready.
b. You will be tested mostly on the test cases already provided to you with the
assignment.
c. However, we might add some other test cases as well.
d. You will only be evaluated on the assembler. (20%)
2. The final evaluation:
a) By this deadline, you must have both the assembler and the simulator
ready(70%).
b) You should also have completed Q3(10%).
c) You will be evaluated on a much larger set of test cases this time.
d) You will also be evaluated on the bonus question at this stage.
❖ The mid evaluation will be worth 20% of your final assignment grade. The final
evaluation will be worth the rest 80% of your final assignment grade. The bonus
will be worth 10% making the total 110%.

## Instructions
1. Use a Bash emulator: Install a Bash emulator such as Git Bash. Following are
the links to the installation and the procedure to follow, respectively.
https://gitforwindows.org/
https://stackoverflow.com/questions/36401147/running-sh-scripts-in-git-bash
(your run files usually have .sh extension in Linux. They can execute even
without the extension specified, like in the case of the run file provided to you)
2. Use Windows Subsystem for Linux (WSL) on VSCode: you can enable the
Windows Subsystem for Linux, which allows you to run a Linux distribution such
as Ubuntu directly on Windows. Once you have WSL installed, you can execute
the run file from within the Linux environment by moving your testing directory to
the Linux file system in WSL. It's recommended you do this on VSCode for a
better experience. Refer to the following link:
https://code.visualstudio.com/docs/remote/wsl-tutorial
3. Use a virtual machine: Install a virtual machine software like VirtualBox
(https://www.virtualbox.org/) or VMware (https://www.vmware.com/) and set up a
Linux distribution inside the virtual machine. This will provide you with a full Linux
environment where you can execute the run file. Obviously, you'll have to move
the entire testing directory to the OS run by your VM.
● Then go to the automatedTesting directory in your terminal and execute ./run
command.

## Screenshots
![image](https://github.com/aroraomansh/CSE112-B31-project/assets/119057485/7d6214d6-79b9-40b9-b723-21e66cd2ed31)
![image](https://github.com/aroraomansh/CSE112-B31-project/assets/119057485/c5b353dc-0315-4964-afc8-6b6a4d6bd4bb)
![image](https://github.com/aroraomansh/CSE112-B31-project/assets/119057485/74455c7b-6d3d-49a6-bd22-3b4d059c5817)
![image](https://github.com/aroraomansh/CSE112-B31-project/assets/119057485/cbea9f9d-6256-412a-bd82-29136b08338d)
![image](https://github.com/aroraomansh/CSE112-B31-project/assets/119057485/a340c604-b182-4df5-be95-6477ff0de172)
![image](https://github.com/aroraomansh/CSE112-B31-project/assets/119057485/56305825-38a4-4211-b62e-eabf3e3c5573)

## Contribution
Efforts by group B31:
Pranav Bharadwaj 2022363,
Omansh Arora     2022342,
Naman Singh      2022312,
Nishant Kumar    2022326.
