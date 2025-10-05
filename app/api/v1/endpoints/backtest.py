from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any

from app import schemas, crud
from app.api import deps
from app.services.trading_service import TradingService

router = APIRouter()

@router.post("/", response_model=schemas.BacktestResult)
def run_backtest(
    *,
    db: Session = Depends(deps.get_db),
    backtest_in: schemas.BacktestCreate,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Run a new backtest for a given strategy.
    """
    strategy = crud.strategy.get(db, id=backtest_in.strategy_id)
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    trading_service = TradingService(db=db, user_id=1) # Replace with actual user_id
    
    try:
        result = trading_service.run_backtest(
            strategy_name=strategy.name,
            symbol=backtest_in.symbol,
            timeframe=backtest_in.timeframe,
            start_date=backtest_in.start_date,
            end_date=backtest_in.end_date,
            initial_capital=backtest_in.initial_capital,
            risk_percentage=backtest_in.risk_percentage,
        )
        # Here you would typically save the result to the DB via crud operations
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
