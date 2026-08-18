from fastmcp import FastMCP

sharad = FastMCP("My MCP Server")  #name of server 


#tool
@sharad.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@sharad.tool
def add(a:int, b:int) -> int:
    return a + b

if __name__ == "__main__":
    #sharad.run()    # this is streamable ,streamable transport is default 
    sharad.run(transport = "stdio")   

