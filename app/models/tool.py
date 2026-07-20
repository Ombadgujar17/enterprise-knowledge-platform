from pydantic import BaseModel


class ToolRequest(BaseModel):
    query: str


class ToolResponse(BaseModel):
    result: str