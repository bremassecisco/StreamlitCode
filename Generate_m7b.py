from llama_cpp import Llama
def generate_m7b_output(query, max_tokens = 1000):
    modelpath = "./models/mistral-7b-instruct-v0.2.Q5_K_M.gguf"
    LLM = Llama(modelpath)
    output = LLM(query, max_tokens=1000)
    return output["choices"][0]["text"]