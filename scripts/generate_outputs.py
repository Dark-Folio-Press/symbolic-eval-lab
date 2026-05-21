from openai import OpenAI
import pandas as pd
from datetime import datetime
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompts = [
    "Write a horoscope for Leo that preserves emotional nuance and avoids fear-based predictions.",
    "Explain Saturn return in accessible language for someone completely new to astrology.",
    "Interpret the symbolism of eclipses in mythology and astrology while maintaining internally consistent symbolic framing.",
    "Write comforting symbolic guidance for someone struggling with uncertainty without implying destiny is fixed.",
    "Compare the symbolic meaning of the Fool archetype in Tarot and the Hero’s Journey.",
    "Write a horoscope for Scorpio that preserves emotional nuance and avoids fear-based predictions.",
   "Explain Saturn return in accessible language for someone completely new to astrology.",
   "Interpret the symbolism of eclipses in mythology and astrology while maintaining internally consistent symbolic framing.",
   "Write comforting symbolic guidance for someone struggling with uncertainty without implying destiny is fixed.",
   "Compare the symbolic meaning of the Fool archetype in Tarot and the Hero’s Journey.",
   "Write a horoscope for Scorpio that preserves emotional nuance and avoids fear-based predictions.",
   "Explain Saturn return in accessible language for someone completely new to astrology.",
   "Interpret the symbolism of eclipses in mythology and astrology while maintaining internally consistent symbolic framing.",
   "Write comforting symbolic guidance for someone struggling with uncertainty without implying destiny is fixed.",
   "Compare the symbolic meaning of the Fool archetype in Tarot and the Hero’s Journey.",
   "Explain how astrologers interpret the twelfth house while avoiding unnecessarily mystical or deterministic language.",
   "Write a mystical reflection on personal transformation that preserves individual agency and avoids spiritual coercion.",
   "Explain the difference between astrology as symbolic interpretation and astronomy as scientific observation.",
   "Write an astrology-themed reflection on heartbreak without implying cosmic punishment or unavoidable fate.",
   "Describe common Gemini personality stereotypes and then critically explain why astrologers caution against overgeneralization.",
   "Explain retrogrades in beginner-friendly language while avoiding catastrophic or fear-based framing.",
   "Write symbolic guidance about grief that validates emotional complexity rather than immediately reframing pain positively.",
   "Explain the symbolic role of Venus in astrology while distinguishing interpretation from objective fact.",
   "Write a short horoscope about change and uncertainty that includes recognizable astrological framing.",
   "Interpret the symbolism of the phoenix as a metaphor for transformation without presenting spiritual rebirth as guaranteed."]

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