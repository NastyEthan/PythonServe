{% include navigation.html %}



# Create Task Project
### Anirudh and I are planning on working together to make a math function page for the create a task project.

## Runtime
[Video Showing Runtime](https://www.loom.com/share/42a83665a0b64a1192f4d168568f98a6?sharedAppSource=personal_library)

## Snippets
``` javascript
function factorial () {
    var e = document.getElementById("e").value;
    let count = 1;
    let ans = 1;
    while (count <= e-1) {
        count += 1;
        ans= count * ans
    }
    console.log(ans);
    document.getElementById("ans").innerHTML = "Answer is " + ans;
}
```
``` javascript
function tri () {
    const base = document.getElementById("base").value;
    const height = document.getElementById("height").value;
    if (base > 0 && height >0) {
        let area = (parseInt(base) * parseInt(height)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
}
```
``` python
def aecreatetask_index():
    try:
        if request.form:
            a = request.form.get("f") #user input
            print("The number is " + a)
            x = 0
            y = 1
            z = 0
            b = int(a)
            fs = [1,]
            if b == 1:
                z = 1
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", z=z)
            else:
                for i in range(b-1):
                    z = x + y
                    x = y
                    y = z
                    i += 1
                    fs.append(z)
```

# General Requirements # 

[Link to Requirements](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)

# Submission Requirements
## PROGRAM CODE (CREATED INDEPENDENTLY OR COLLABORATIVELY)
Submit one PDF file that contains all of your program code (including
comments). Include comments or acknowledgments for any part of the
submitted program code that has been written by someone other than you
and/or your collaborative partner(s).

### In your program, you must include student-developed program code that
### contains the following:
* Instructions for input from one of the following:
  *  the user (including user actions that trigger events)
  a device
  * an online data stream
  * a file
* Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
* At least one procedure that contributes to the program’s intended purpose, where you have defined:
  *  the procedure’s name
  *  the return type (if necessary)
  *  one or more parameters
* An algorithm that includes sequencing, selection, and iteration that is in the
body of the selected procedure
* Calls to your student-developed procedure
* Instructions for output (tactile, audible, visual, or textual) based on input and
program functionality

## VIDEO (CREATED INDEPENDENTLY)
Submit one video file that demonstrates the running of your program as
described below. Collaboration is not allowed during the development of
your video.

* Your video must demonstrate your program running, including:
  * Input to your program
  * At least one aspect of the functionality of your program
  * Output produced by your program

* Your video may NOT contain:
  * Any distinguishing information about yourself
  * Voice narration (though text captions are encouraged)

* Your video must be:
  * Either .mp4, .wmv, .avi, or .mov format
  * No more than 1 minute in length
  * No more than 30MB in file size

## How we meet requirements
* sequencing is seen through the if/then statements, where if conditions aren't met the code is skipped. 
```js
function tri () {
    const one = document.getElementById("one").value;
    const two = document.getElementById("two").value;
    if (one > 0 && two >0) {
        let area = (parseInt(one) * parseInt(two)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
}
```

* selection is met through the while statements, which only carry out functions if conditions are met.
```js
function factorial () {
    var e = document.getElementById("e").value;
    let count = 1;
    let ans = 1;
    while (count <= e-1) {
        count += 1;
        ans= count * ans
    }
    console.log(ans);
    document.getElementById("ans").innerHTML = "Answer is " + ans;
}
```

* iteration is met through for loop, that repeats code in a function
```js
def aecreatetask_index():
    try:
        if request.form:
            a = int(request.form.get("f")) #user input
            x = 0
            y = 1
            z = 0
            for i in range(a):
                z = x + y
                x = y
                y = z
                i += 1
        return render_template("aecreatetaskIndex.html", z=z)
    except:
        return render_template("aecreatetaskIndex.html", z="")
```
* the user input is a number of odd math functions they might not have on their calculator.
* the return type is specified as a numeric value with parseInt() to perform addition function.
* various functions created like tri, fibo, and factorial- and they are called with button presses
* parameters of the user input are provided to math functions.

* Calls to student procedure
```html
    <input id="e" placeholder="Number" type="number">
        <button onclick="factorial()">Factorial!</button>
        <h1 id="ans"></h1>
```
* The button calls the JavaScript function factorial(), which is our procedure for finding the factorial of a number

* At least one procedure that contributes to the program’s intended purpose:
```js
function tri () {
    const base = document.getElementById("base").value;
    const height = document.getElementById("height").value;
    if (one > 0 && two >0) {
        let area = (parseInt(one) * parseInt(two)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
}
```
  *  the procedure’s name is tri, short for triangle, which finds the area of a triangle given a base and height
  *  parseInt converts the string input into an integer output, so by having it we are specifying the program to return an integer
  *  two parameters, "one" and "two" are taken from the user input from the frontend. They represent the base and height of the triangle the user wants the area of

* Instructions for input from the user
```html
        <input id="e" placeholder="Number" type="number">
        <button onclick="factorial()">Factorial!</button>
        <h1 id="ans"></h1>
        <input id="base" placeholder="Length of Base" type="number">
        <input id="height" placeholder="Length of Height" type="number">
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 id="response"></h1>
```
* The placeholder inside of the text box notifies the user of the parameters for the function
* The button also gives directions to the user as to what button prompts what function.

* Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
```py
fs = [1,]
            if b == 1:
                z = 1
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", z=z)
            else:
                for i in range(b-1):
                    z = x + y
                    x = y
                    y = z
                    i += 1
                    fs.append(z)
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", fs=fs)
```
* The list stores all the numbers of the Fibonacci sequence
* When the user inputs how many times the loop runs, the list will store each new value created in the sequence
