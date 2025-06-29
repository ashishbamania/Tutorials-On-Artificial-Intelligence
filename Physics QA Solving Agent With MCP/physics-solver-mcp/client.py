from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os

# Create a StdioServerParameters object for the physics server
server_params=StdioServerParameters(
    command="python3", 
    args=["physics_server.py"],
    env={**os.environ},
)

# Use the StdioServerParameters object to create a MCPServerAdapter
with MCPServerAdapter(server_params) as tools:
    print(f"Available physics tools: {[tool.name for tool in tools]}")

    agent = Agent(
        role="Physics Expert",
        goal="Solve physics problems using fundamental energy calculations.",
        backstory="An experienced physicist with deep knowledge of classical mechanics and energy principles. Can apply kinetic and potential energy concepts to solve practical problems.",
        tools=tools,
        verbose=True,
    )
    
    task = Task(
        description="Solve this physics problem: {physics_problem}",
        expected_output="A detailed step-by-step solution showing all calculations, intermediate values, and final answers with proper units. Use the available physics tools to perform kinetic energy and potential energy calculations.",
        agent=agent,
    )
    
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    # Physics problem
    crew_inputs = {
        "physics_problem" : """
        A roller coaster car with a mass of 800 kg starts from rest at the top of a hill that is 50 meters high.
        The car then descends the hill and reaches a velocity of 25 m/s at the bottom.
        
        Given:
        - Mass of the car: 800 kg
        - Initial height: 50 m
        - Final velocity: 25 m/s
        - Gravitational acceleration: 9.81 m/s²
        
        Questions:
        1. Calculate the initial gravitational potential energy of the car at the top of the hill.
        2. Calculate the final kinetic energy of the car at the bottom of the hill.
        3. Compare the initial potential energy with the final kinetic energy and explain any differences.
        4. If the car were to climb another hill, what maximum height could it reach if all its kinetic energy were converted back to potential energy?
        """
    }

    result = crew.kickoff(inputs=crew_inputs)
   
    print(result)