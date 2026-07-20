from fastapi import APIRouter

from app.models.tool import ToolRequest, ToolResponse
from app.services.tool_service import ToolService

router = APIRouter(
    prefix="/tools",
    tags=["Tools"],
)

tool_service = ToolService()


@router.post("/ticket", response_model=ToolResponse)
def create_ticket(request: ToolRequest) -> ToolResponse:
    return ToolResponse(
        result=tool_service.execute_tool(
            tool_name="ticket",
            query=request.query,
        ),
    )


@router.post("/leave", response_model=ToolResponse)
def request_leave(request: ToolRequest) -> ToolResponse:
    return ToolResponse(
        result=tool_service.execute_tool(
            tool_name="leave",
            query=request.query,
        ),
    )


@router.post("/email", response_model=ToolResponse)
def send_email(request: ToolRequest) -> ToolResponse:
    return ToolResponse(
        result=tool_service.execute_tool(
            tool_name="email",
            query=request.query,
        ),
    )