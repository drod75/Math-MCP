from src.api.main import router_app
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()
app.include_router(router_app)

mcp = FastApiMCP(
    app,
    "Math MCP Server",
    "An MCP server that allows LLM's to use math formulas and operations!",
)

mcp.mount()
