from multiprocessing import Pool
import pandas as pd
import Generate_m7b
filename = "ThatClauseOutput.csv"
df = pd.read_csv(filename)
prompts = []
for q in df['Example']:
    prompts.append("Use as much of the original text as possible and provide me with a sentence that flows better. " + q)
LLMOutputs = []
with Pool(processes=len(prompts)) as pool:
    LLMOutputs = pool.map(Generate_m7b.generate_m7b_output, prompts)