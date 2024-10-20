import streamlit as st
import google.generativeai as genai
from decryption import replace_with_original_words, decryption_after_replacing_original_words
from JavaCodeEncryption import encrypt_java_code_elements

# Configure the API key
my_api_key_gemini = ""
genai.configure(api_key=my_api_key_gemini)
model = genai.GenerativeModel('gemini-pro')

# Generate a secret key (keep it safe!)
encrypted_words_dict = {}

# Function to generate a response from the AI model
def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        if response.text:
            return response.text
        else:
            return "Sorry, but Gemini didn't want to answer that!"
    except Exception:
        return "Sorry, but Gemini didn't want to answer that!"

# Streamlit application
st.set_page_config(page_title="Gemini AI Automation Assistant", page_icon=":robot:", layout="wide")
st.markdown("""
    <style>
        /* Overall body styling with gradient background */
        body {
            background: linear-gradient(to right, #2b2b2b, #4c4c4c); /* Darker gradient background */
            background-attachment: fixed;
            background-position: center;
            color: #ffffff; /* White text for better readability */
            transition: background-color 0.5s ease; /* Smooth background transition */
        }
        
        /* Styling for the title */
        .title {
            color: #00d4ff; /* Bright cyan for title */
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            margin-top: 30px;
            text-shadow: 2px 2px #000000; /* Adds shadow for depth */
            animation: title-animation 2s ease-in-out infinite; /* Title animation */
        }
        
        /* Title animation keyframes */
        @keyframes title-animation {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        /* Styling for headers */
        .header {
            color: #ffdd57; /* Golden color for subheaders */
            font-size: 1.75em;
            font-weight: bold;
            margin-top: 20px;
            text-shadow: 1px 1px #000000;
            animation: header-animation 1.5s ease-in-out infinite; /* Header animation */
        }
        
        /* Header animation keyframes */
        @keyframes header-animation {
            0% { transform: translateX(0); }
            50% { transform: translateX(10px); }
            100% { transform: translateX(0); }
        }

        /* Styling for text areas (e.g., generated outputs) */
        .text-area {
            border: 2px solid #3498db; /* Soft blue border */
            border-radius: 10px;
            padding: 15px;
            background-color: rgba(255, 255, 255, 0.1); /* Subtle transparent background */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow for 3D effect */
            color: #ffffff; /* White text */
            animation: text-area-animation 2.5s ease-in-out infinite; /* Text area animation */
        }
        
        /* Text area animation keyframes */
        @keyframes text-area-animation {        /* Text area animation keyframes */
        @keyframes text-area-animation {
            0% { box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); }
            50% { box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2); }
            100% { box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); }
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: rgba(20, 30, 48, 0.8); /* Darker background for sidebar */
            padding: 20px;
            border-radius: 10px;
            color: #ffffff;
            animation: sidebar-animation 2s ease-in-out infinite; /* Sidebar animation */
        }
        
        /* Sidebar animation keyframes */
        @keyframes sidebar-animation {
            0% { transform: translateX(0); }
            50% { transform: translateX(5px); }
            100% { transform: translateX(0); }
        }

        /* Sidebar file uploader text */
        .sidebar .sidebar-content h2 {
            color: #00d4ff;
            font-size: 1.5em;
            margin-bottom: 10px;
            text-align: center;
            animation: uploader-text-animation 1.5s ease-in-out infinite; /* Uploader text animation */
        }
        
        /* Uploader text animation keyframes */
        @keyframes uploader-text-animation {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Text inside the text area */
        textarea {
            font-family: "Courier New", monospace; /* Monospace font for code */
            color: #ffffff;
            background-color: rgba(20, 30, 48, 0.7); /* Background for textarea */
            border: 2px solid #3498db;
            border-radius: 10px;
            animation: textarea-content-animation 2s ease-in-out infinite; /*
            /* Textarea content animation keyframes */
        @keyframes textarea-content-animation {
            0% { background-color: rgba(20, 30, 48, 0.7); }
            50% { background-color: rgba(20, 30, 48, 0.9); }
            100% { background-color: rgba(20, 30, 48, 0.7); }
        }

        /* Custom scrollbar for sidebar */
        ::-webkit-scrollbar {
            width: 12px;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #3498db;
            border-radius: 10px;
        }

        /* Hover effect for buttons */
        button:hover {
            background-color: #3498db !important; /* Button color on hover */
            transition: background-color 0.3s ease;
            transform: scale(1.05); /* Button scale on hover */
        }

        /* Button animation */
        button {
            animation: button-animation 1.5s ease-in-out infinite;
        }

        /* Button animation keyframes */
        @keyframes button-animation {
            0% { transform: scale(1); }
            50% { transform: scale(1.01); }
            100% { transform: scale(1); }
        }

        /* Fade-in animation for all elements */
        * {
            animation: fade-in-animation 2s ease-in-out;
        }

        /* Fade-in animation keyframes */
        @keyframes fade-in-animation {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="title">Gemini AI Test Case Generator</div>', unsafe_allow_html=True)
# Sidebar for file upload and toggle buttons
st.sidebar.header("**Upload a Text File**")
uploaded_file = st.sidebar.file_uploader("Upload a text file containing user story or code", type=["txt"])

# Toggle buttons to show/hide uploaded text and encrypted code
show_uploaded_text = st.sidebar.checkbox("Show Uploaded Text")
show_encrypted_code = st.sidebar.checkbox("Show Encrypted Code")

# Radio buttons for test case generation options with animation
option = st.radio(
    "Select the type of test cases to generate:",
    ('BDD Test Cases', 'JUnit Code', 'AAT Test Cases'),
    key="radio",
)

if uploaded_file is not None:
    uploaded_text = uploaded_file.read().decode("utf-8")
    
    # Show uploaded text if toggle button is checked
    if show_uploaded_text:
        st.sidebar.subheader("**Uploaded Text**")
        st.sidebar.text_area("Uploaded Text", value=uploaded_text, height=300, key="uploaded_text", 
                             help="The content of the uploaded text file.")
    
    # Show encrypted code if toggle button is checked
    if option == 'JUnit Code' and show_encrypted_code:
        encrypted_code = encrypt_java_code_elements(uploaded_text)
        st.sidebar.subheader("**Encrypted Code**")
        st.sidebar.text_area("Encrypted Code", value=encrypted_code, height=300, key="encrypted_code", 
                             help="The encrypted Java code.")
    
    # Button to generate response
    generate_button = st.button("**Generate Test Cases**")

    if generate_button:
        if option == 'BDD Test Cases':
            prompt = f"Generate BDD Automation test cases and scenarios for the following user story:\n\n{uploaded_text}"
        elif option == 'JUnit Code':
            encrypted_code = encrypt_java_code_elements(uploaded_text)
            prompt = f"Generate JUnit test cases de for the following Java code:\n\n{encrypted_code} with valid method names"
        elif option == 'AAT Test Cases':
            prompt = f"Generate AAT test cases in BDD framework for the following user story:\n\n{uploaded_text} for the following user story in the code"

        generated_output = generate_response(prompt)
        if option == 'JUnit Code':
            decrypted_output = replace_with_original_words(generated_output, encrypted_words_dict)
            decrypted_output = decryption_after_replacing_original_words(generated_output, encrypted_words_dict)
        else:
            decrypted_output = generated_output

        st.subheader(f"**Generated {option}**")
        st.text_area(f"{option}", value=decrypted_output, height=300, key="generated_output", 
                     help=f"The {option.lower()} generated based on the uploaded file.")
else:
    st.sidebar.write("No file uploaded.")