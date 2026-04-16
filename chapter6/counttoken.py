import tiktoken

#Choose the encoding model
encoding_model = tiktoken.encoding_for_model("gpt-4")

#Your data
with open ("flamehamster.md", "r", encoding="utf-8") as file:
    text = file.read()

#Count the tokens
tokenized_text = encoding_model.encode(text)
num_tokens = len(tokenized_text)

print(f"Number of tokens in the text: {num_tokens}")