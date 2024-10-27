# CrewAI Series Day 4

This is a "day 4" of a series of projects based on https://github.com/tylerprogramming/ai/tree/main/crewai_series and ["I Created a CUSTOM AI Tool with CrewAI"](https://www.youtube.com/watch?v=rcmMK-zkxrQ&list=PLwPL8GA9A_un2_WrDekhx0SFLO4TVYZd1&index=7). It deviates from the Youtube video in that instaed of using serper for search it uses Tavily.

This project creates a custom tool to search the web and return results to a second agent to generate a report. It uses [Tavily](https://tavily.com/) search service. You can create an account and get 1000 calls a month for free at Tavily.

The requirements.txt contains the tavily and other needed packages.

Once, I have had what seemed like CrewAI to get stuck in a loop calling the TavilyBasicSearch tool. I had to break the run and it had consumed about 100 API calls. I'm not sure if there is a mechanism on CrewAI to limit the number of calls to a tool or if that would have even worked in my case. I didn't have any breakpoints and wasn't running debug so I have no idea what it was doingm, but it stalled and after cancelling it my newly setup Tavily account had encountered an extra 100 API calls.
