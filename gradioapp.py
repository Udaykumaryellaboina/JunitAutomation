# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:41:06 2024

@author: LENOVO
"""

import google.generativeai as gen 
model = gen.GenerativeModel('gemini-pro')
import gradio as gr
import google.generativeai as genai
import os

my_api_key_gemini = ""
genai.configure(api_key=my_api_key_gemini)
model = genai.GenerativeModel('gemini-pro')
"""
def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        if response.text:
            return response.text
        else:
            return "Sorry, but I think Gemini didn't want to answer that!"
    except Exception:
        return "Sorry, but Gemini didn't want to answer that!"

# Define the Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs=gr.Textbox(label="Response"),
    title="Gemini AI Chat",
    description="Ask a question, and Gemini will respond."
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        if response.text:
            return response.text
        else:
            return "Sorry, but I think Gemini didn't want to answer that!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define the Gradio interface
with gr.Blocks() as interface:
    gr.Markdown("## Gemini AI Chatbot")
    gr.Markdown("### Ask a question, and Gemini will respond. You can adjust the prompt settings as well.")
    
    with gr.Row():
        prompt = gr.Textbox(lines=2, placeholder="Enter your prompt here...", label="Your Question")
    
    with gr.Accordion("Advanced Settings"):
        temperature = gr.Slider(0.0, 1.0, value=0.5, step=0.01, label="Creativity (Temperature)")
        max_tokens = gr.Slider(1, 512, value=128, step=1, label="Max Tokens")
    
    with gr.Row():
        clear_button = gr.Button("Clear")
        submit_button = gr.Button("Submit")

    output = gr.Textbox(label="Gemini's Response", lines=10)

    def process_input(prompt, temperature, max_tokens):
        try:
            response = model.generate_content(prompt, temperature=temperature, max_tokens=max_tokens)
            return response.text if response.text else "Sorry, but I think Gemini didn't want to answer that!"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    submit_button.click(fn=process_input, inputs=[prompt, temperature, max_tokens], outputs=output)
    clear_button.click(fn=lambda: "", inputs=None, outputs=prompt)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()
"""

def generate_response(prompt, temperature, max_tokens):
    try:
        response = model.generate_content(prompt, temperature=temperature, max_tokens=max_tokens)
        return response.text if response.text else "Sorry, but I think Gemini didn't want to answer that!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def generate_bdd_test_cases(file, temperature, max_tokens):
    try:
        if file is None:
            return "No file uploaded."
        
        # Read the content of the file
        user_story = file.decode('utf-8')
        prompt = f"Generate BDD test cases for the following user story:\n\n{user_story}"
        
        response = model.generate_content(prompt, temperature=temperature, max_tokens=max_tokens)
        return response.text if response.text else "Sorry, but I think Gemini didn't want to generate BDD test cases for that!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define the Gradio interface
with gr.Blocks() as interface:
    gr.Markdown("## Gemini AI Chatbot and BDD Test Case Generator")
    gr.Markdown("### Ask a question, or upload a user story to generate BDD test cases.")
    
    with gr.Row():
        prompt = gr.Textbox(lines=2, placeholder="Enter your prompt here...", label="Your Question")
    
    with gr.Accordion("Advanced Settings"):
        temperature = gr.Slider(0.0, 1.0, value=0.5, step=0.01, label="Creativity (Temperature)")
        max_tokens = gr.Slider(1, 512, value=128, step=1, label="Max Tokens")
    
    with gr.Row():
        clear_button = gr.Button("Clear")
        submit_button = gr.Button("Submit")
    
    with gr.Row():
        file_upload = gr.File(label="Upload User Story (.txt)")
        bdd_button = gr.Button("Generate BDD Test Cases")
    
    output = gr.Textbox(label="Gemini's Response", lines=10)

    submit_button.click(fn=generate_response, inputs=[prompt, temperature, max_tokens], outputs=output)
    clear_button.click(fn=lambda: "", inputs=None, outputs=prompt)
    bdd_button.click(fn=generate_bdd_test_cases, inputs=[file_upload, temperature, max_tokens], outputs=output)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()
