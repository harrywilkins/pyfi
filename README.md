<html>

<body>
<h1><b>pyfi</b> - Python Fidelity v0.1: An advanced module for Python</h1>

<h3><b>AdvancedInput</b>.py - Advanced methods for getting user inputs</h3>
  <ul>
  <li><b>sinput (prompt): </b>Returns type sensitive values based on input format</li>
    <ul>
    <li><b>prompt - </b>The prompt displayed to the user at the input statement. Default value ">>> "</li>
    </ul>

  <p></p>
  <li><b>InputFormat (inpFormat, separateWords, prompt): </b>Returns user input if it matches a given format</li>
    <ul>
    <li><b>inpFormat - </b>The format to compare the input to in the form of a list</li>
    <li><i>Useable data types: ["int", "float", "alpha", "lower", "upper", "str", "space"]</i></li>
    <li><b>separateWords - </b>If true, the method will compare the user input word-by-word. If false, character-by-character</li>
    <li><b>prompt - </b>The prompt displayed to the user at the input statement. Default value ">>> "</li>
    </ul>
  </ul>

<h3><br><b>AutoComplete</b>.py - Method that auto-completes unfinished words</h3>
  <ul>
  <li><b>AutoCompleteFast (word): </b>Returns the first exact match it finds. Faster than full check</li>
    <ul>
    <li><b>word - </b>The word to auto-complete. Format examples: "h*ll_" ["H",")","l","l","@"] - Both represent unfinished "hello"</li>
    </ul>

  <p></p>
  <li><b>AutoCompleteFull (word): </b>Returns a list of the best matching words. Takes slightly longer</li>
    <ul>
    <li><b>word - </b>The word to auto-complete. Format examples: "ap,l%" ["a","P",":","l","."] - Both represent unfinished "apple"</li>
    </ul>
  
  <p></p>
  <li><b>SpellCheck (word): </b>Takes a word, and returns the closest match of the same length in the English dictionary</li>
    <ul>
    <li><b>word - </b>Any alphabetic string. It can include numbers and spaces, but it will treat it as a single word</li>
    </ul>
  
  <p></p>
  <li><b>SCInput (prompt): </b>Type in a sentence and it will return an 'SpellCheck()' version of each word as a sentence</li>
    <ul>
    <li><b>prompt - </b>Default value ">>> " - The prompt displayed to the user by the input statement</li>
    </ul>
  </ul>
  
  
<h3><br><b>Debug</b>.py - A system for storing and printing logs</h3>
  <ul>
  <li><b>Log (logType, value): </b>Logs a value as a specific log type</li>
    <ul>
    <li><b>logType - </b></li>
    <li><b>value - </b></li>
    </ul>

  <p></p>
  <li><b>PrintLog (): </b>Prints the current log</li>
  </ul>


<h3><br><b>MathSeq</b>.py - A number of maths sequences</h3>
  <ul>
  <li><b>Fibonacci (iterations): </b>Displays the Fibonacci sequence</li>
    <ul>
    <li><b>iterations - </b>The number of iterations of the sequence to display</li>
    </ul>
  </ul>
  
  
<h3><br><b>Searching</b>.py - List searching methods</h3>
  <ul>
  <li><b>BinarySearch (numList, item): </b>Returns index of an item in an ordered number list</li>
    <ul>
    <li><b>numList - </b>An ordered number list (int or float)</li>
    <li><b>item - </b>The number (int or float) to look for in the specified list</li>
    </ul>
    
  <p></p>
  <li><b>LinearSearch (itemList, item): </b></li>
    <ul>
    <li><b>itemList - </b>A list of any values</li>
    <li><b>item - </b>The item to find the index of in the list</li>
    </ul>
  </ul>


<h3><br><b>Table</b>.py - Table creation and manipulation module</h3>
  <ul>
  <li><b>Table (x, y, cellValue): </b>Create a new Table class instance</li>
    <ul>
    <li><b>x - </b>The x location of the cell. This applies to the entire class</li>
    <li><b>y - </b>The y location of the cell. This applies to the entire class</li>
    </ul>

  <p></p>
  <li><b>DisplayBoard (spaces): </b>Display the current table/board</li>
    <ul>
    <li><b>spaces - </b>The number of spaces between each element. Default value is 0</li>
    </ul>
    
  <p></p>
  <li><b>GetCell (x, y): </b>Get the value of a cell at position (x, y)</li>

  <p></p>
  <li><b>ModifyCell (x, y, newValue): </b>Modify the value of a cell at position (x, y)</li>
    <ul>
    <li><b>newValue - </b>The new value you would like the cell to take</li>
    </ul>

  <p></p>
  <li><b>GetCellByNumber (cellNumber): </b>Get the value of a cell by cell number</li>
    <ul>
    <li><b>cellNumber - </b>The cell number, the top-left cell is 0, and from there it reads in the way a book does</li>
    </ul>

  <p></p>
  <li><b>ModifyCellByNumber (cellNumber, newValue): </b>Modify the value of a cell by cell number</li>
    <ul>
    <li><b>cellNumber - </b>The cell number, the top-left cell is 0, and from there it reads in the way a book does</li>
    <li><b>newValue - </b>The new value you would like the cell to take</li>
    </ul>
  </ul>

</body>

</html>
