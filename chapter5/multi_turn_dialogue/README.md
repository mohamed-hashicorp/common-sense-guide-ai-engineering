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
Assistant: How can I help you today?

User: What is the weather today in Amsterdam
Assistant: I don't have real-time access to current weather data. To find out the weather in Amsterdam today, you can check a reliable weather website or app such as:

- [Weather.com](https://weather.com)
- [AccuWeather](https://www.accuweather.com)
- [BBC Weather](https://www.bbc.com/weather)

Or simply search "Amsterdam weather today" on a search engine for the latest updates.

User: What is the longest building in the world
Assistant: The longest building in the world is the **Great Wall of China** if considering it as a continuous structure, but if you are asking about a single building or structure designed for occupancy or use, the title often goes to:

- **The Great Wall of China**: It stretches over approximately 21,196 kilometers (13,171 miles), but it is a fortification, not a building in the traditional sense.

For the longest building designed for occupancy:

- **The New Century Global Center** in Chengdu, China, is one of the largest buildings by floor area but not necessarily the longest.

- **The Aalsmeer Flower Auction** building in the Netherlands is often cited as one of the longest buildings, stretching about 740 meters (2,428 feet).

- **The Boeing Everett Factory** in Washington, USA, is the largest building by volume but not the longest.

If you want the longest continuous building by length, the **Aalsmeer Flower Auction** is a good example.

Could you specify if you mean the longest building by length, floor area, or volume?

User: exit
```
