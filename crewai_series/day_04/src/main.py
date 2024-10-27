#!/usr/bin/env python
import sys
from crew import Day04Crew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """

    inputs = {
        'topic': 'news on CrewAI',
        'limit': 5,
    }

    Day04Crew().crew().kickoff(inputs=inputs)

run()