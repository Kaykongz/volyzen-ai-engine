from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    backtest,
    connections,
    consents,
    legal,
    live,
    markets,
    paper,
    reports,
    risk,
    strategies,
    websocket,
)

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(connections.router, prefix="/connections", tags=["Connections"])
api_router.include_router(markets.router, prefix="/markets", tags=["Markets"])
api_router.include_router(strategies.router, prefix="/strategies", tags=["Strategies"])
api_router.include_router(backtest.router, prefix="/backtest", tags=["Trading"])
api_router.include_router(paper.router, prefix="/paper", tags=["Trading"])
api_router.include_router(live.router, prefix="/live", tags=["Trading"])
api_router.include_router(risk.router, prefix="/risk", tags=["Risk"])
api_router.include_router(consents.router, prefix="/consents", tags=["Compliance"])
api_router.include_router(legal.router, prefix="/legal", tags=["Compliance"])
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"])
api_router.include_router(websocket.router, prefix="/ws", tags=["Websocket"])
