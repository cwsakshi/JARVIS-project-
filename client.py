from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)
