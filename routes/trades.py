from fastapi import APIRouter


from utility.trades import get_all_trades, get_trade_by_id, search_trades, filter_trades


router = APIRouter()
router = APIRouter(prefix='/trades', tags=['Trades'])


@router.get("")
async def get_trades():
    trades = await get_all_trades()
    return trades


@router.get("/{trade_id}")
async def get_trade(trade_id: str):
    trade = await get_trade_by_id(trade_id)
    return trade


@router.get("/search")
async def search_trade(query: str):
    trades = await search_trades(query)
    return trades


@router.get("/filter")
async def filter_trade(assetClass: str = None, start: str = None, end: str = None, 
                       tradeType: str = None, minPrice: float = None, maxPrice: float = None):
    trades = await filter_trades(assetClass=assetClass, start=start, end=end, 
                                 tradeType=tradeType, minPrice=minPrice, maxPrice=maxPrice)
    return trades
