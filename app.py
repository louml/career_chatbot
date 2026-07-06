from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
from system_prompt import assistant_prompt

load_dotenv(override=True)

client = OpenAI()

GREETING = "Hi, I'm Lourenço's career assistant. You can ask me about his experience, skills, projects, education, or professional background."

chatbot = gr.Chatbot(
    value=[{"role": "assistant", "content": GREETING}],
)

textbox=gr.Textbox(
     placeholder="Ask me anything about Lou Marques' career...", 
     container=False, 
     scale=7
)

def chat(message, history):
    response = client.responses.create(
        model="gpt-5.5",
        instructions=assistant_prompt,
        input=message,
    )

    return response.output_text


demo = gr.ChatInterface(
     fn=chat, 
     chatbot=chatbot, 
     textbox=textbox,
)

demo.launch(theme=gr.themes.Monochrome())
    
