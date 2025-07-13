import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio(  
    'mcp-atlassian',
    command="docker",
    args=[
        "run",
        "--rm",
        "-i",
        "--env-file",
        ".env",
        "ghcr.io/sooperset/mcp-atlassian:latest"
    ]
)
agent = Agent('openai:gpt-4o', mcp_servers=[server])


async def main():
    async with agent.run_mcp_servers():
        result = await agent.run('create a new ticket for learning mcp, assign it to john and move it to in progress')
    print(result.output)

if __name__ == "__main__":
    asyncio.run(main())