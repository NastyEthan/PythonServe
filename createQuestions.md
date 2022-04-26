# Create Task Responses

# [Link to Create Task](https://www.loom.com/share/966c23bb8c6143d1a98ce7cea384f01a)
## 3 a. Provide a written response that does all three of the following:
Approx. 150 words (for all subparts of 3a combined)

### Describes the overall purpose of the program
This program essentially does a couple quick math calculations. It serves as a calculator to calculate the area of a triangle, factorial, and fibonacci sequences quickly.

### Describes what functionality of the program is demonstrated in the video
Each function is shown in the video in which each textfield parameters needed from the user. The initial value in the text fields indicate which value the text field requires in order to create the calculation, or the parameters. For example, to find an area of a triangle we need the base and height, which are the values required in the text field to make the calculations.

### Describes the input and output of the program demonstrated in the video
In this case, the user must input a number into the text field of what number they want to take the factorial of. They can also input two values in the other text field to calculate the area (one for base and one for height). The last one generates the fibonacci sequence up to the input term.

## 3 b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.
Approx. 200 words (for all subparts of 3b combined, exclusive of
program code)
### The first program code segment must show how data have been stored in the list.

```
if request.form:
            a = request.form.get("f") #user input
            print("The number is " + a)
            x = 0
            y = 1
            z = 0
            b = int(a)
            fs = [1,] #creates list of fibonacci numbers that starts with 1
            if b == 1:
                z = 1
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", z=z) #accounts for if user input is one
            else:
                for i in range(b-1):
                    z = x + y
                    x = y
                    y = z
                    i += 1
                    fs.append(z)
```

### The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.

```
for i in range(b-1):
                    z = x + y
                    x = y
                    y = z
                    i += 1
                    fs.append(z)
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", fs=fs) # accounts for any other number input, appends new turns to list
```

### Then, provide a written response that does all three of the following:

### Identifies the name of the list being used in this response
The list is called "z" and when the program runs the program will create the number in the fibonacci sequence and append it to the list until it reaches the desired term.

### Describes what the data contained in the list represent in your program
Inside the list are the generated terms of the fibonacci sequence. They are created by the loop and are appended into the list.

### Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list
Since we wanted to generate the entire fibonacci sequence up to the inputed term, we needed to be able to display multiple items. Without a list, we could not append the fibonacci numbers to something and then display it to show to the user.

## 3 c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure.
Approx. 200 words (for all subparts of 3c combined, exclusive of
program code)

### The first program code segment must be a student-developed procedure that:
* Defines the procedure’s name and return type (if necessary)
* Contains and uses one or more parameters that have an effect
on the functionality of the procedure
* Implements an algorithm that includes sequencing, selection,
and iteration

```
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
Credit: This is my partner Anirudh Ramachandran's Code. We worked together on this project.

### The second program code segment must show where your student-developed procedure is being called in your program. Then, provide a written response that does both of the following:

```
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 style="color:white" id="response"></h1>
```
Credit: This is my partner Anirudh Ramachandran's Code. We worked together on this project.

### Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
The procedure in this case is in the javascript for the function finding the area of the triangle. The function takes two parameters from the user and multiplies them and halves the product in order to get the area of a triangle with those dimensions. Since it finds the area of a triangle, it serves as another math product to put for our math functions program.

### Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
First, it creates constants for the base and height values required by the user. Then, it checks for negative inputs to execute error handling with an if/else statement. Lastly, it executes the code to generate the area of the triangle with proper inputs. Once given, it will return the answer by pringing a statement without relaoding the page of the answer.
