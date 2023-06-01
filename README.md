# State-Table-to-Boolean-Expression-Converter

This project aims to automate the process of converting a state diagram into a boolean expression, providing a precise
and faster response even with a higher number of states. It incorporates the Quine McCluskey method, which is widely
used in industry-level projects for handling large state tables.

<h2>Problem Statement</h2>
State diagrams are commonly used in digital logic design to represent the behavior of sequential circuits. Converting a
state diagram into a boolean expression manually can be a time-consuming and error-prone process, especially when
dealing with a large number of states. Techniques like Karnaugh maps become increasingly complex and challenging to
apply as the state table grows.

<h2>Solution</h2>
To address this challenge, we have developed a state diagram to boolean expression converter that utilizes the 
<b><u>"Quine McCluskey method"</u></b>. This method offers an iterative approach for minimizing boolean expressions, which significantly
simplifies the conversion process. The key features of our solution include:


<ul>
    <li>Automated Conversion: Our code automates the conversion process, reducing the need for manual intervention and
        minimizing the chances of human error.
    </li>
    <li>Efficient Handling of Large State Tables: By employing the Quine McCluskey method, our solution is well-equipped
        to handle state tables with a higher number of states efficiently. It reduces the complexity and time required
        compared to traditional methods such as Karnaugh maps.
    </li>
    <li>Precise and Optimal Output: The Quine McCluskey method ensures that the resulting boolean expression is
        simplified and optimized. It minimizes the number of terms and variables, resulting in a concise and precise
        representation of the original state diagram.
    </li>
    <li>User-Friendly Interface: Our code provides a user-friendly interface, guiding users to input the state
        transitions and output values, and displaying the resulting state diagram and boolean expression.</li>
</ul>

Please watch the YouTube video provided below, which offers a theoretical explanation of the concept.<br>
<a href="https://youtu.be/NbON135lf60" target="">Youtube video link from Neso Academy</a>

<h2>Usage:</h2>
In order to ensure smooth execution, please make sure to have the necessary dependencies installed on your local
computer. You may either copy the provided code or follow the instructions mentioned below.
<p></p>
<ol>
    <li>Clone the repository by running the following command in your terminal:<br>
        <code>git clone https://github.com/your-username/state-diagram-converter.git</code>
    </li>
    <li>
        Navigate to the project directory:<br>
        <code>cd state-diagram-converter</code>
    </li>
    <li>
        Run the code using the following command:<br>
        <code>python state_diagram_converter.py</code>
    </li>
    <li>
        Follow the prompts to provide the required inputs, including the number of states and the next state and output
        values for each state transition.
        Once all the necessary information is provided, the code will generate the state diagram and display it.
        Subsequently, the code will apply the Quine McCluskey method to convert the state diagram into a boolean
        expression and show the result in the console.
    </li>
</ol>


<h2>Dependencies</h2>
<p>The code is implemented in Python and relies on the following dependencies:</p>
<ol>
    <li>Python 3.x</li>
    <li>tabulate (for proper visualization of tabular data)</li>
    <li>tkinter (for creating a graphical user interface)</li>
</ol>

<h2>Installation</h2>
<p>To install the required dependencies, you can use the following pip install commands:</p>

<pre>
<code>pip install tabulate</code>
<code>pip install tkinter</code>
</pre>

<p>Make sure you have Python 3.x installed on your system before running these commands.</p>


<h2>Code execution snippets</h2>
<div style="display: flex;">
    <img src="https://github.com/PavanSETTEM-003/State-Table-to-Boolean-Expression-Converter/assets/88257205/b5903454-c06f-42e1-beed-cf4ed3165528" alt="Screenshot 1" style="width: 50%;">
    <img src="https://github.com/PavanSETTEM-003/State-Table-to-Boolean-Expression-Converter/assets/88257205/68f77378-0b98-4952-97f0-5a25697f0838" alt="Screenshot 2" style="width: 50%;">
</div>


https://github.com/PavanSETTEM-003/State-Table-to-Boolean-Expression-Converter/assets/88257205/bd619fd9-85c0-4d37-96ef-5c259f8870d4


<h2>Conclusion:</h2>
In summary, the State Table to Boolean Expression Converter is a valuable tool that simplifies the process of converting state tables into boolean expressions. It provides a user-friendly GUI interface and Python-based code for generating state diagrams, applying the Quine McCluskey method, and obtaining boolean expressions representing state transitions.

By using this converter, developers and designers can save time and effort when working with state-based systems. It streamlines the design and analysis process, improving efficiency and enhancing understanding of complex systems.


Try out our State Table to Boolean Expression Converter, provide feedback.
