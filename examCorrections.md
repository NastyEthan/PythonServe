# Exam Corrections

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
