#!/usr/bin/env python
import sys
from crew import Day03Crew
from date import datetime

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    inputs = {
        'topic': 'openai',
        'date': datetime.now().strftime('%Y-%m-%d'),
    }

Day03Crew().crew().kickoff(inputs=inputs)

run()