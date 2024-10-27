from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv


load_dotenv()


@CrewBase
class Day03Crew():
	"""Day03 crew"""

	# self.agents_config and self.tasks_config are automatically created by the @CrewBase decorator and don't need to be defined here
	# but could be if the paths were not the default 
	# agents_config = 'config/agents.yaml'
	# tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True,
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def repporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reportings_task'],
			output_file='report.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day01 crew"""
		return Crew(
			agents=self.agents,  # Automatically created by the @agent decorator
			tasks=self.tasks,  # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)