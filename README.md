# QA_2023_TSU

Khairi Wiryawan</br>
Вирьяван Хайри</br>
972006</br>

## Unit Test
In this section, I am trying to test the input inside the constraint boundary. </br></br>Checks that are performed under ```test.py``` are :
- find the word that exist on the board
- find the word that not exist on the board
- find the word in the board that contains number/integer
- find the word in the board that contains special character (such as *&#@^*$$@)
- find the word in the board in which contains double character (such as AB)
- find the word in the board in which contains lowercase character
- find the word in the board with a word search using lowercase input
- find the word, but there is no board

![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/37d38010-5817-4cc2-bd43-246a683d1ee1)
![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/b808ad2c-1eb7-482d-83e5-b374abf8888e)

#### Conclusion
4 out of 8 test that are executed provide a result of ```True``` which are :
- find the word that exist on the board
- find the word in the board that contains number/integer
- find the word in the board that contains special character (such as *&#@^*$$@)
- find the word in the board in which contains lowercase character

this translates to the idea that the board accepts any kind of inputs from the user in any forms of character.

3 out of 8 test emit a result of ```False``` which are :
- find the word that not exist on the board
- find the word in the board in which contains double character (such as AB)
- find the word in the board with a word search using lowercase input

Obviously, the solution turn out false if there is no word found in the board based on our will. the other test which gave a false result bring us into a new idea and conclusion on how the solution works. </br></br>```test_board_contains_doubleInput``` turns out to be false gave us a signal that each element in the board only able to handle one character regardles of its type/form which means that elements such as "GH" inside the element of the board is unintelligible. </br></br> the other test of ```test_wordsearchInput_lowercase``` emitted false result is due to the letter case inconsistency throughout the process. for example, in the board we may see the word ```C A T```, but the we input the word search as ```C a T```, then the program is not finding any result because the code is created to be case-sensitive which mean that the code dont find ```C a T``` instead of ```C A T```.</br>

the last but not least, there is neither ```True``` nor ```false```. the test on an empty board(```test_empty_board```) give us an error. This is happened due to the absence of board inputs from its user. This directly translated to that the board inputs is necessary for the ongoing program.

## UI Test
In this section of the assignment, I demonstrate how to conduct an automated UI test using Selenium. By leveraging Selenium's powerful capabilities, I create a script that simulates user interactions with the web application's graphical user interface. This allows for the efficient testing of various UI elements, ensuring that the application is functioning properly and meeting the desired user experience requirements.

<img src="https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/11955af1-a6a1-4fee-ab25-7e38dc2bbc25" width="300" height="314" />
</br>

First start, configuring WebDriver properties in Selenium is an essential step in automating web browsers. It involves specifying the browser type, its location, and other settings to create a WebDriver instance that can interact with the browser. This enables users to perform automated testing tasks efficiently.
![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/7b9d47a3-7617-4a11-8ecd-78d54b7ed647)

This code snippet below retrieves the title of the current web page using the getTitle() method and stores it in a string variable called at2. It then prints the actual title using System.out.println(). The expected title, "Matrix Form", is stored in another string variable called et2, and this value is also printed. The code then compares the actual title with the expected title using the equalsIgnoreCase() method.
![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/1009d609-40f6-4de6-b2fe-03bf75bd851a)

Next, the code below enters values into a 3x4 matrix and a word field on a web page. The first four lines use the sendKeys() method to enter the values "A", "D", "A", and "H" into the first row of the matrix, with each value entered into a different column. The next four lines enter the values "E", "C", "A", and "A" into the second row of the matrix. The last four lines enter the values "B", "K", "Z", and "U" into the third row of the matrix. Finally, the code enters the value "CCG" into the "word" field using the sendKeys() method, followed by the Keys.ENTER command to simulate pressing the Enter key.

![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/e0677a53-703d-4abb-80c9-6cf28442f1e7)

Subsequently, the code verifies the contents of a 3x4 matrix on a web page. It first retrieves the matrix table using an XPath expression and counts the number of rows and columns in the table. It then iterates over each cell in the table using nested for loops, printing the value of each cell to the console.

After that, the code defines an expected matrix of values and retrieves the contents of the matrix table again. It then iterates over each cell in the table, comparing the actual value of each cell to the expected value. If the values match, the code prints a message indicating that the letter in the matrix is the same as the input. If they do not match, the code prints an error message indicating that the actual value does not match the expected value. This code can be used to verify that the values in a matrix on a web page match the expected values, which is useful for testing and quality assurance purposes.
![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/277d3422-6bd3-4f92-9b1f-145641aac07e)

Finally, the code verifies the title and the contents of a result page. It first retrieves the title of the result page and stores it in a string variable at. It then prints both the actual and expected titles to the console and compares them using the equalsIgnoreCase() method. If the titles match, the code prints a message indicating that the expected title matches the actual title. If they do not match, the code prints a message indicating that the expected title does not match the actual title.

The code then retrieves the text of an element with id "keyword" on the result page using the getText() method and stores it in a string variable at1. It then prints both the actual and expected texts to the console and compares them using the equalsIgnoreCase() method. If the texts match, the code prints a message indicating that the expected text matches the actual text. If they do not match, the code prints a message indicating that the expected text does not match the actual text.

Finally, the code closes the browser window using the close() method. This code can be used to automate the process of verifying the title and contents of a result page, which is useful for testing and other tasks.
![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/ed344d2f-96f1-48fc-b049-7844c2cb9ab1)

#### Conclusion
The UI testing was conducted smoothly by checking all the inputs, verifying the inputs, and confirming the results. All expected values were matched with actual values, and there were no errors or issues encountered during the testing process.
![image](https://github.com/russkiymalchik/QA_2023_TSU/assets/73766131/cd5e1888-0afb-4973-9ca1-ce2308b678c7)

