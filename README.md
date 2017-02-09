<html>
<head>
</head>
<body>
<h1><b>pyfi</b> - Python Fidelity v0.1: An advanced module for Python</h1>
<hr>
<h2>Current module tree:</h2>
<ul>
<li><b>AdvancedInput</b>.py
  <ul>
  <li><b>sinput</b>: Return type sensitive values based on input format</li>
  <li><b>InputFormat(inpFormat, separateWords, prompt)</b>: Repeats 'input(prompt)' until it matches the given format.
    <ul>
    <li><b>'inpFormat'</b><i>: Example layout: '['int', 'str', 'upper']'. The format to compare the entered input against.</i></li>
    <li><b>'separateWords'</b><i>: If true will compare the input word-by-word (separated by spaces), to the inpFormat. If false, it will compare letter-by-letter.</i></li>
    <li><b>'prompt'</b><i>: Default value '>>> '. The text displayed by the 'input(prompt)' statement.</i></li>
    </ul>
  </li>
  </ul>
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
