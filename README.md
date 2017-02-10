<html>

<body>

<h2>Current module tree:</h2>

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
    <li><b>separateWords - </b>If true, the method will compare the user input word-by-word. If false, letter-by-letter</li>
    <li><b>prompt - </b>The prompt displayed to the user at the input statement. Default value ">>> "</li>
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
    <li><b>newValue - </b></li>
    </ul>

  <p></p>
  <li><b>GetCellByNumber (cellNumber): </b>Get the value of a cell by cell number</li>
    <ul>
    <li><b>cellNumber - </b></li>
    </ul>

  <p></p>
  <li><b>ModifyCellByNumber (cellNumber, newValue): </b>Modify the value of a cell by cell number</li>
    <ul>
    <li><b>cellNumber - </b></li>
    <li><b>newValue - </b></li>
    </ul>
  </ul>

</body>

</html>


<html>
<head>
</head>
<body>
<h1><b>pyfi</b> - Python Fidelity v0.1: An advanced module for Python</h1>
<hr>
<h2>Current module tree:</h2>
<ul>
<li><b>AdvancedInput</b>.py
<p></p>
  <ul>
  <li><b>sinput</b>: Return type sensitive values based on input format.</li>
  <p></p>
  <li><b>InputFormat(inpFormat, separateWords, prompt)</b>: Repeats 'input(prompt)' until it matches the given format.
  <p></p>
    <ul>
    <li><b>'inpFormat'</b><i>: Example layout: '['int', 'str', 'upper']'. The format to compare the entered input against.</i></li>
    <li><b>'separateWords'</b><i>: If true will compare the input word-by-word (separated by spaces), to the inpFormat. If false, it will compare letter-by-letter.</i></li>
    <li><b>'prompt'</b><i>: Default value '>>> '. The text displayed by the 'input(prompt)' statement.</i></li>
    </ul>
  </li>
  </ul>
<p></p>
<li><b>Debug</b>.py
  <p><i>Supression</i>: [log, warning, error], values set to 1 to enable supression.</p>
  <ul>
  <li><b>Log</b>: Pasing the log type and type insensitive value stores and, based on supression, prints log.</li>
  <li><b>PrintLog</b>: Will output the log for the session.</li>
  </ul>
</li>

<li><b>MathSeq</b>.py
  <ul>
  <li><b>fibonacci</b>: Output fibonacci sequence as array to an iterative degree.</li>
  </ul>
</li>

<li><b>Table</b>.py
  <p><i>Initiated by creating an instance of a table - Example: 'board = Table(xSize, ySize)'</i></p>
  <ul>
  <li><b>GetCell</b>: Get the cell at the referenced position [x,y].</li>
  <li><b>ModifyCell</b>: Will set the referenced position [x,y] to the specified value.</li>
  <li><b>GetCellByNumber</b>: Get the nth cell in the entire table. </li>
  <li><b>ModifyCellByNumber</b>: Will set the nth cell in the table to the specified value.</li>
  </ul>
</li>
</ul>
</body>
</html>
