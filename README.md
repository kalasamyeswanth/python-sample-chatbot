TITLE: Sample Python Chatbot
 Task Documentation: Using Python.
INTERN INFORMATION: 
Name: Kalasam Yeshwanth
ID: ICOD6551
INTRODUCTION:

Chatbot responds to different greetings, inquiries about its well-being, expressions of gratitude, and farewells. For any other input, it provides a default response. You can expand its capabilities by adding more patterns and responses in the responses dictionary. Chatbots can provide real-time customer support and are therefore a valuable asset in many industries. When you understand the basics of the ChatterBot library, you can build and train a self-learning chatbot with just a few lines of Python code.
You’ll get the basic chatbot up and running right away in step one, but the most interesting part is the learning phase, when you get to train your chatbot. The quality and preparation of your training data will make a big difference in your chatbot’s performance. 
Implementation:
	Here we implement random module to Python Random module generates random statements in Python 
	This module can be used to perform random actions such as generating random statements, printing random a value for a list or string, etc. It is an in-built function in Python.
	Here we define Responses Dictionary which the  dictionary is used to store predefined responses for different user inputs
	This main() function serves as the entry point of the chatbot program. It starts by printing a greeting message and then enters a loop where it continuously prompts the user for input. The loop terminates when the user enters "exit".
	By encapsulating the response generation logic in the chatbot_response() function, it provides a clean and modular way to generate responses based on user input
	This function can easily be extended to handle more complex patterns and responses as needed. 
CODE EXPLAINATION:
Functions Signature:
This line defines a function named “chatbot_response” that takes one parameter user_input, which represents the input provided by the user.
Lowercasing User Input:
	This line converts the user_input to lowercase using the lower() method. This ensures that the chatbot can match user input regardless of the case (e.g., "hi", "Hi", "HI", etc.).
Iterating Over Response Keys:
This line iterates over each key in the responses dictionary. Each key represents a pattern that the chatbot can respond to match user input 
Default Response:
		If no match is found in the previous step, this line returns a random response from the "default" key in the responses dictionary. This ensures that the chatbot always has a response, even if it doesn't recognize the user's input.
Main function:
__main__ is the name of the environment where top-level co
de is run. “Top-level code” is the first user-specified Python module that starts running. It’s “top-level” because it imports all other modules that the program needs. Sometimes “top-level code” is called an entry point to the application.

USAGE:
Copy the entire code provided for the chatbot, including the ‘responses’ dictionary, the “chatbot_response()” function, and the “main()” function. Paste the code into a Python file (e.g., chatbot.py) using a text editor or an Integrated Development Environment (IDE) Save the file.
 Open a terminal or command prompt. Navigate to the directory where the Python file is saved using the cd command. Once you're in the correct directory, run the Python file by typing python chatbot.py and pressing Enter. The chatbot will start running and display the initial message: "Chatbot: Hi there! How can I help you today?"
You can then interact with the chatbot by typing messages and pressing Enter. It will respond based on the predefined patterns in the responses dictionary. To exit the chatbot, type "exit" and press Enter. The chatbot will respond with a farewell message and the program will terminate.

CONCLUSION:
In conclusion, the Python chatbot offers a practical solution for providing automated responses to user queries and can be further customized and extended to meet specific requirements. Its simplicity, flexibility, and effectiveness make it a valuable tool for a wide range of applications, from customer service to educational purposes
The Python chatbot we've created provides a simple yet effective way to engage in conversation with users. By leveraging predefined patterns and responses stored in a dictionary, the chatbot can understand various user inputs and provide relevant responses.
OUTPUT:

 


