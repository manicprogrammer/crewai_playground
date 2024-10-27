# CrewAI Series Day 4

This is a "day 4" of a series of projects based on https://github.com/tylerprogramming/ai/tree/main/crewai_series and https://www.youtube.com/watch?v=rcmMK-zkxrQ&list=PLwPL8GA9A_un2_WrDekhx0SFLO4TVYZd1&index=7. It deviates from the Youtube video in that instaed of using serper for search it uses Tavily.

This project creates custom tools to search the web and generate a report. It uses Tavily search service (https://tavily.com/) which you can create an account and get 1000 calls a month for free.

The requirements.txt contains the tavily python package.

I have had one time what seemed like CrewAI to get stuck in a loop calling the TavilyBasicSearch. I think this because I had to break the run and it had consumed about 100 api calls
