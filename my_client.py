import asyncio   
from fastmcp import Client

client = Client("my_server.py")  #name of server file       

async def call_tool(name : str):
    async with client:
        result = await client.call_tool("greet", {"name": name}) 
        #tools = await client.list_tools()
        print(result.data)

if __name__ == "__main__":
    asyncio.run(call_tool("Ford"))
 



