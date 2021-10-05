<div align=center>
	<h1><b>5 x 7 ASCII Sign Generator</b></h1>
	<p>Convert ASCII values 32-126 into 5x7 blocks of text</p>
</div>

# **Quick start:**
This project is powered by the Message class which can be found in the [message.py] file. There are several prebuild ways to access this class including [main.py] and [sign.ipynb]. [main.py] supports both command line arguments and user input.
# **Using [sign.ipynb]**
Currently, [sign.ipynb] only accepts inputs in a simular manner to [main.py]
# **Using [main.py]**
## **User input:**
```
python3 main.py
```
User input is triggered whenever 4 total command line arguments are not used. When in this mode, [main.py] prompts the user for three inputs which are explained in the [usage](#usage)

> NOTE: The message class does support multi-line messages, but only through files which are passed in the command line

*This command creates the following prompt and output:*
```
> Enter your message: Hello
> Enter your line type: W
> Enter your character style: 0
0   0            00      00
0   0             0       0
0   0    000      0       0      000
00000   0   0     0       0     0   0
0   0   00000     0       0     0   0
0   0   0         0       0     0   0
0   0    000     000     000     000
```
## **Command line:**
```
python3 main.py sample1.txt W 0
```
Here we see that [main.py] can also take 3 arguments which are explained in the [usage](#usage):
- arv[1] = file containing message: [sample1.txt]
- arv[2] = Line writing type: W
- arv[3] = Letter Style: 0

*The output of this command is as follows:*
```
0                00      00
0                 0       0
0 00     000      0       0      000
00  0   0   0     0       0     0   0
0   0   00000     0       0     0   0
0   0   0         0       0     0   0
0   0    000     000     000     000
```
## Usage
There are three inputs to be considered in the Message class:
- message: the text to be converted and written
- Line Type: Three different line orientations
	- C: One character per line
	- W: Non-blank lines are printed
	- L: all lines are printed
- Letter Style: which character will be used to fill in the message

These inputs can be sent to the contructor as possitional arguments, or using the keywords "message", "lineType", and "style" respectively

[message.py]: https://github.com/aldenmoreton/ASCIISign/blob/master/message.py
[main.py]: https://github.com/aldenmoreton/ASCIISign/blob/master/main.py
[sign.ipynb]: https://github.com/aldenmoreton/ASCIISign/blob/master/sign.ipynb
[sample1.txt]: https://github.com/aldenmoreton/ASCIISign/blob/master/sample1.txt
