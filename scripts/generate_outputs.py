from openai import OpenAI
import pandas as pd
from datetime import datetime
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompts = [

     "Write a horoscope for Scorpio that preserves emotional nuance and avoids fear-based predictions.",
   "Explain Saturn return in accessible language for someone completely new to astrology.",
   "Interpret the symbolism of eclipses in mythology and astrology while maintaining internally consistent symbolic framing.",
   "Write comforting symbolic guidance for someone struggling with uncertainty without implying destiny is fixed.",
   "Compare the symbolic meaning of the Fool archetype in Tarot and the Hero’s Journey.",
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