# Import Streamlit framework for creating the web app
import streamlit as st
import time

# Define a dictionary with predefined questions and answers
predefined_answers = {
    "questions": [
        {
            # Bonus Question for Thoughtful AI
            "question": "What is Thoughtful AI?",
            "answer": "Thoughtful AI is a company that builds advanced AI solutions to automate and enhance business processes, including customer support and healthcare automation."
        },
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}

# Function to get a response based on user query
def get_response(query):
    """
    This function searches through the predefined answers and returns the answer
    if a match is found. If no match is found, it returns a default error message.
    """
    try:
        # Iterate through the list of predefined questions and answers
        for item in predefined_answers["questions"]:
            # If the user's query matches any of the predefined questions (case insensitive)
            if item["question"].lower() == query.lower():
                return item["answer"]
        
        # Return a default message if no match is found
        return "Sorry, I don't have an answer because that question is not predefined."
    
    except Exception as e:
        # Catch any unexpected errors and provide a user-friendly error message
        return f"An error occurred while processing your request: {str(e)}"

# Function to simulate typewriter effect
def typewriter_effect(text, speed=0.1):
    placeholder = st.empty()  # Create a placeholder to update the text
    typed_text = ""
    
    for char in text:
        typed_text += char  # Append the next character
        placeholder.write(typed_text)  # Update the placeholder with the current text
        time.sleep(speed)  # Wait a little before adding the next character

# Title for the Streamlit web page
st.title("Thoughtful AI - Customer Support Agent")

# Input field where the user can type a question
user_input = st.text_input("Ask me anything about Thoughtful AI:")

# Check if user has entered a question
if user_input:
    # Get the response based on the user's input
    answer = get_response(user_input)
    # Display the response in the app
    typewriter_effect(answer, speed = 0.03)
else:
    # Provide an initial message when no user input is provided
    st.write("Please enter a question to get an answer about Thoughtful AI.")
