from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv


load_dotenv()


@CrewBase
class Day02Crew():
	"""Day02 crew"""

	# ollama_31_8b is set up for LMStudio using a llama3.1:8b model and setting the provider as openai because it is compatible 
	# note the /v1 added to the base_url and had set the port in LMStudio to 11434
	# ollama_31_8b = LLM(model="openai/llama3.1:8b", base_url="http://localhost:11434/v1")
	# setting the provider as openai is per: https://docs.litellm.ai/docs/providers/openai_compatible
	
	ollama_32_3b = LLM(model="ollama/llama3.2:3b", base_url="http://localhost:11434")
	phi3 = LLM(model="ollama/phi3", base_url="http://localhost:11434")

	# self.agents_config and self.tasks_config are automatically created by the @CrewBase decorator and don't need to be defined here
	# but could be if the paths were not the default 
	# agents_config = 'config/agents.yaml'
	# tasks_config = 'config/tasks.yaml'

	@agent
	def chuck_norris_joke_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['chuck_norris_joke_generator'],
			verbose=True,
			llm=self.ollama_32_3b
		)

	@agent
	def chuck_norris_joke_picker(self) -> Agent:
		return Agent(
			config=self.agents_config['chuck_norris_joke_picker'],
			verbose=True,
			llm=self.phi3
		)

	@task
	def generate_jokes_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_jokes_task'],
		)

	@task
	def pick_joke_task(self) -> Task:
		return Task(
			config=self.tasks_config['pick_joke_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day02 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)