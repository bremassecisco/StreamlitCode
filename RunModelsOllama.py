from token_count import TokenCount
from multiprocessing import Pool
import pandas as pd
import ollama
import time
from openai import AsyncOpenAI
from openai import OpenAI

def run_prompt(integer, prompt, model = "phi3:latest"):
    print(integer)
    if integer % 3 == 0:
        print("phi3")
        model = "phi3:latest"
    elif integer % 3 == 1:
        print("llama3")
        model = "llama3:latest"
    else:
        print("mistral")
        model = "mistral:latest"
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ignore-me")
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt},],
        stream=True
    )
    streamed_text = ""
    for chunk in stream:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            streamed_text = streamed_text + chunk_content
            #print(streamed_text)  # Print the generated text to the terminal
            
    return streamed_text