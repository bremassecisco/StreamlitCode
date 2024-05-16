import time
from openai import AsyncOpenAI
from openai import OpenAI
from token_count import TokenCount
from multiprocessing import Pool
import pandas as pd
import ollama

def run_prompt(prompt, model = "phi3:latest"):
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ignore-me")
    tc = TokenCount(model_name="gpt-3.5-turbo")
    start = time.time()
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
            end = time.time()
            time_taken = end-start
            tokens = tc.num_tokens_from_string(streamed_text)
            print(f"""**Duration: [{time_taken:.2f} secs]**
            **Eval count: [{tokens} tokens]**
            **Eval rate: [{tokens / time_taken:.2f} tokens/s]**
            """)  # Print the evaluation metrics to the terminal
    return streamed_text, (tokens / time_taken)


if __name__ == "__main__":
    #prompt = """Rewrite the following three sentence structure as one fluid sentence: The cat that is fat. The cat that is lazy. The cat that is sleeping."""
    filename = "ThatClauseOutput.csv"
    df = pd.read_csv(filename)
    prompts = []
    for q in df['Example']:
        prompts.append("Use as much of the original text as possible and provide me with a sentence that flows better. Only include the revise sentence - nothing more. Please respond with one sentence. " + q)
    LLMOutputs = []
    time_taken_list = []
    with Pool(processes=len(prompts)) as pool:
        LLMOutputs = pool.map(run_prompt, prompts)
    
    for q in range(0, len(LLMOutputs), 1):
        print("Input: " + prompts[q])
        print("Output: " + LLMOutputs[q][0])
        time_taken_list.append(LLMOutputs[q][1])
        print(" ")

    print("Average time taken is: " + str(sum(time_taken_list) / len(time_taken_list)) + " seconds.")