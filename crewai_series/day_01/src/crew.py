from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv


load_dotenv()


@CrewBase
class Day01Crew():
	"""Day01 crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def joke_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['joke_creator'],
			verbose=True
		)

	@agent
	def add_emojis(self) -> Agent:
		return Agent(
			config=self.agents_config['add_emojis'],
			verbose=True
		)

	@task
	def joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['joke_task'],
		)

	@task
	def add_emojis_task(self) -> Task:
		return Task(
			config=self.tasks_config['add_emojis_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day01 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)