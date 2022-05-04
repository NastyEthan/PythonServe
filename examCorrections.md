# Exam Corrections

# Exam 1
## Question 23
### Which of the following has the greatest potential for compromising a user’s personal privacy?
* A group of cookies stored by the user’s Web browser
* The Internet Protocol (IP) address of the user’s computer
* The user’s e-mail address
* The user’s public key used for encryption

## Correction
I selected B because I initially thought the IP address is important to a computer, but the address itself does not have as much information as cookies stored by the web browser. The cookies have information that the websites can use to track the user's actions (which invades the privacy). This quesiton was less about getting hacked but more about losing privacy.

## Question 24
### Which of the following best explains how data is typically assembled in packets for transmission over the Internet?*
* Each packet contains data to be transmitted, along with metadata containing information used for routing the data.
* Each packet contains an encrypted version of the data to be transmitted, along with metadata containing the key needed to decrypt the data.
* Each packet contains only the metadata used to establish a direct connection so that the data can be transmitted.
* Each packet contains multiple data files bundled together, along with metadata describing how to categorize each data file.

## Correction
I selected D because I thought that the data would be sent with data describing that, but I was also thinking between A. D is not the correct answer because the data does not come in packets, and actually routes the data instead.

## Question 29
### Which of the following is true?
* The conclusion is correct; the program works as intended.
* The conclusion is incorrect; the program does not display the correct value for the test case [0, 1, 4, 5].
* The conclusion is incorrect; using the test case [0, 1, 4, 5] is not sufficient to conclude the program is correct.
* The conclusion is incorrect; using the test case [0, 1, 4, 5] only confirms that the program works for lists in increasing order.

## Correction
I initially picked A as the test case did in fact work, but didn't realize the first line of the code made the code faulty. As a result, I should've picked C, because the answer was actually wrong and the code would not work with a different input. I should've been more careful looking at the question but its unlikely I would catch a problem like this

## Question 42
###  If the ID number assigned to the last student who enrolled was the binary number 1001 0011, what binary number will be assigned to the next student who enrolls?
* 1001 0100
* 1001 0111
* 1101 0100
* 1101 0111

## Correction
I carelessly picked A in this case when I meant to pick C

## Question 50
### Which of the following describes a lossless transformation of the digital image?
* Compressing the image in a way that may lose information but will suffer only a small loss of image quality.
* Creating the gray scale of an image by averaging the amounts of red, green, and blue in each pixel and assigning this new value to the corresponding pixel in the new image. The new value of each pixel represents a shade of gray, ranging from white to black.
* Creating the negative of an image by creating a new RGB triplet for each pixel in which each value is calculated by subtracting the original value from 255. The negative of an image is reversed from the original; light areas appear dark, and colors are reversed.
* Modifying part of the image by taking the pixels in one part of the picture and copying them to the pixels in another part of the picture.

## Correction
I picked C but the correct answer was D. If the negative of the image is made, each RGB value will be preserved through the process of subtracting from 255, but if the pixels are copied the values will be lost forever.

# Exam 2

## Question 8
### Which of the following is NOT an advantage of using open-source software?
* Open-source software is generally free or lower in cost than commercially available software.
* The availability of source code makes it possible to customize open-source software to a user’s individual needs.
* The original developer of open-source software provides free or low-cost support for users installing and running the software.
* Unlike commercial software, which can become obsolete when the company that created it goes out of business, open-source software can be updated without the involvement of the original programmers.

## Correction
I was very confused with this question but after realizing that the answer was C the answer makes more sense to me. C is a better answer than B because C doesn't actually always happen, so with this question I should've been looking for something that wasn't actually true not given

## Question 14
### Which of the following best describes the average amount of data stored per user for the first eight years of the application’s existence?
* Across all eight years, the average amount of data stored per user was about 10 GB.
* Across all eight years, the average amount of data stored per user was about 100 GB.
* The average amount of data stored per user appears to increase by about 10 GB each year.
* The average amount of data stored per user appears to increase by about 100 GB each year.

## Correction
I knew how to do this problem, but I accidentally selected 100 instead of 10 - multiplication error that could be corrected by being a little more careful and checking answers

## Question 32
### Which of the following statements is true about how the eight directions must be stored in memory?
* Four bits are not enough to store the eight directions. Five bits are needed for the new version of the game.
* Four bits are not enough to store the eight directions. Eight bits are needed for the new version of the game.
* Four bits are not enough to store the eight directions. Sixteen bits are needed for the new version of the game.
* Four bits are enough to store the eight directions.

## Corrections
Another simple mistake, miscounting the bits. bits go from 2^x, should've been D did not neet another bit (for 8 total directions)

## Question 45
### Which of the following pairs of spreadsheets can be combined and analyzed to determine the desired information?
* Spreadsheets I and II
* Spreadsheets I and IV
* Spreadsheets II and III
* Spreadsheets III and IV

## Corrections
This was actually a very tricky problem I probably would've missed even if I was careful. Choice A is the best because we don't need GPA above 3.5 or not, but we need GPAs from each student and who are athletes. A fits this criteria the best.

# Exam 3
## Question 15
### Which of the following is a true statement about program documentation?
* Program documentation should not be changed after it is first written.
* Program documentation is only needed for programs in development; it is not needed after a program is completed.
* Program documentation is useful when programmers collaborate but not when a programmer works individually on a project.
* Program documentation is useful during initial program development and also when modifications are made to existing programs.

## Corrections
This question was tricky, but if I looked at all of the answer options more closely I would've found that D was a better choice than B, since documentation is needed after the program is finished

## Question 30
### Which of the following best explains the relationship between the Internet and the World Wide Web?

* Both the Internet and the World Wide Web refer to the same interconnected network of devices.
* The Internet is an interconnected network of data servers, and the World Wide Web is a network of user devices that communicates with the data servers.
* The Internet is a local network of interconnected devices, and the World Wide Web is a global network that connects the local networks with each other.
* The Internet is a network of interconnected networks, and the World Wide Web is a system of linked pages, programs, and files that is accessed via the Internet.

## Corrections
I was between the answers B and D and lost the coinflip when deciding this. Essentially my definition of the world wide web was incorrect.

## Question 34
### For which of the following situations would it be best to use a heuristic in order to find a solution that runs in a reasonable amount of time?

* Appending a value to a list of  n  elements, which requires no list elements be examined.
* Finding the fastest route that visits every location among n locations, which requires n! possible routes be examined.
* Performing a binary search for a score in a sorted list of n scores, which requires that fewer than n scores be examined.
* Performing a linear search for a name in an unsorted database of n people, which requires that up to n entries be examined.

## Corrections
I misread this question. I meant to select the answer that does not need a huerstic but the question asked for the program that won't finish in reasonable time.

## Question 41
### In public key cryptography, the sender uses the recipient’s public key to encrypt a message. Which of the following is needed to decrypt the message?
* The sender’s public key
* The sender’s private key
* The recipient’s public key
* The recipient’s private key

## Corrections
I didn't know the answer to this question straight up. The answer is D because logically speaking the recipient would need a private key or else the message would not be decrypted

## Question 46
### Which of the following is an example of symmetric encryption?
* Evy buys a locked box that operates using two different codes. When the first code is entered, a slot opens that allows a message to be put in the box. When the second code is entered, the door to the box opens. Evy gives the first code to her friends so they can leave messages for her and keeps the second code to herself so that she is the only one who can retrieve the messages.
* Finn and Gwen develop a system that maps each letter of the alphabet to a unique symbol using a secret key. Finn uses the key to write a message to Gwen where each letter is replaced with the corresponding symbol. Gwen uses the key to map each symbol back to the original letter.
* Hannah writes a message to send to Isabel and hides the message under a rock behind the soccer field. Hannah gives Isabel the exact location of the rock so that only Isabel can find the message.
* Juan writes a message to send to Kelly and slides the message through a slot in the front of Kelly’s locker. Juan knows that Kelly has not shared her locker combination with anyone, so no one other than Kelly will be able to read the message.

## Corrections
This question was difficult because I didn't know the symmetric encryption. I could've gotten this question right by reviewing terms such as symmetric encryption

# Exam 5
## Question 3
### For which of the following procedure calls does the procedure NOT return the intended value?
* The figure presents a line of code. The line of code contains a nested block of code. Line 1: [begin block] Multiply [begin block] 2, 5 [end block] [end block]
* The figure presents a line of code. The line of code contains a nested block of code. Line 1: [begin block] Multiply [begin block] 2, −5 [end block] [end block]
* The figure presents a line of code. The line of code contains a nested block of code. Line 1: [begin block] Multiply [begin block] −2, 5 [end block] [end block]
* The figure presents a line of code. The line of code contains a nested block of code. Line 1: [begin block] Multiply [begin block] −2, −5 [end block] [end block]

## Corrections
I picked B and C but I mistakened the code segment. As a result, B and D was the correct answer because y doesn't meet the condition and the code never executes

## Question 17
### Which of the following best compares the execution times of the two versions of the program?
* Version I requires approximately 1 more minute to execute than version II.
* Version I requires approximately 5 more minutes to execute than version II.
* Version II requires approximately 1 more minute to execute than version I.
* Version II requires approximately 5 more minutes to execute than version I.

## Corrections
I picked C, but I had a feeling that the answer was D. Each time the loop runs the procedure is called twice, not once and ends up being 9 vs 4

## Question 41
### Which of the following could be used to replace steps 3 and 4 so that the algorithm works as intended?
* Step 3
Increase the value of position by 1.
Step 4
Repeat steps 2 and 3 until the value of count is greater than 100.
* Step 3
Increase the value of position by 1.
Step 4
Repeat steps 2 and 3 until the value of position is greater than n.
* Step 3
Repeat step 2 until the value of count is greater than 100.
Step 4
Increase the value of position by 1.
* Step 3
Repeat step 2 until the value of position is greater than n.
Step 4
Increase the value of count by 1.

## Corrections

## Question
###

## Corrections
