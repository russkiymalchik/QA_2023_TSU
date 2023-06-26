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
