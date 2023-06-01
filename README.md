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
To address this challenge, we have developed a state diagram to boolean expression converter that utilizes the Quine
McCluskey method. This method offers an iterative approach for minimizing boolean expressions, which significantly
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
The code is implemented in Python and relies on the following dependencies:
<ol>
    <li>Python 3.x</li>
    <li>tabulate (for proper visualization of tabular data)</li>
    <li>tkinter (for creating a graphical user interface)</li>
</ol>

