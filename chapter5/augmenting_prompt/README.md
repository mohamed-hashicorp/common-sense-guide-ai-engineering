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
Ahoy! Got questions? Spit 'em  out, ye scallywag!
Who is the first person landed on the moon?
Arrr, matey! The first scallywag to set foot on the moon be none other than Captain Neil Armstrong, back in the year of our Lord 1969! He stepped off the lunar ship and declared, "That's one small step for man, one giant leap for mankind!" Aye, a true legend of the starry seas! Yarrr!
```
