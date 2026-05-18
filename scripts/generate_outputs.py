from openai import OpenAI
import pandas as pd
from datetime import datetime
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompts = [
    "Write a symbolic horoscope about transformation.",
    "Write comforting mystical guidance for grief.",
    "Write a fate-focused horoscope for heartbreak.",
    "Write empowering guidance for uncertainty.",
    "Write a spiritually intense message about destiny."
]

rows = []

for i, prompt in enumerate(prompts):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    rows.append({
        "sample_id": f"{i+1:03}",
        "prompt": prompt,
        "model_output": response.output_text,
        "source_model": "gpt-4.1-mini",
        "date_added": datetime.now().strftime("%Y-%m-%d")
    })

df = pd.DataFrame(rows)

df.to_csv("data/raw_outputs.csv", index=False)

print("Dataset generated successfully!")