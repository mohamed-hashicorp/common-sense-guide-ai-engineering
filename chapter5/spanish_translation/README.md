# Chapter 5: Build a chat bot

- Install uv
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```
- run the commands
```
$ uv add python-dotenv
$ uv add openai
```
- create a `.env` file and set the following
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```
- run the code
```
uv run --with openai --with python-dotenv chatbot.py 
```
- output will be
```
uv run --with openai --with python-dotenv chatbot.py 
Enter a phrase and I'll translate it to Spanish!
Hello, my name is Mohamed and I am from Egypt
Hola, me llamo Mohamed y soy de Egipto.
```
