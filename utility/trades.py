from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from schema import Trade, TradeDetails
from sqlalchemy.orm import Session

# Sample data
trades = [
    Trade(
        asset_class='Equity',
        counterparty='ABC Corp',
        instrument_id='AAPL',
        instrument_name='Apple Inc.',
        trade_date_time=datetime(2022, 4, 20, 10, 30),
        trade_details=TradeDetails(
            buy_sell_indicator='BUY', price=150.0, quantity=100),
        trade_id='1',
        trader='John Doe'
    ),
    Trade(
        asset_class='Bond',
        counterparty='XYZ Bank',
        instrument_id='GOOGL',
        instrument_name='Alphabet Inc.',
        trade_date_time=datetime(2022, 4, 20, 11, 30),
        trade_details=TradeDetails(
            buy_sell_indicator='SELL', price=200.0, quantity=50),
        trade_id='2',
        trader='Jane Doe'
    )
]

class TradeFilter:
    def __init__(
        self,
        asset_class: str = None,
        end_date: datetime = None,
        max_price: float = None,
        min_price: float = None,
        start_date: datetime = None,
        trade_type: str = None,
    ):
        self.asset_class = asset_class
        self.end_date = end_date
        self.max_price = max_price
        self.min_price = min_price
        self.start_date = start_date
        self.trade_type = trade_type

async def get_all_trades() -> List[Trade]:
    return trades


async def get_trade_by_id(trade_id: str) -> Trade:
    for trade in trades:
        if trade.trade_id == trade_id:
            return trade
    return None


async def search_trades(query: str) -> List[Trade]:
    query = query.lower()
    search_fields = ["counterparty",
                     "instrument_id", "instrument_name", "trader"]
    matching_trades = []
    for trade in trades:
        for field in search_fields:
            if query in str(getattr(trade, field)).lower():
                matching_trades.append(trade)
                break
    return matching_trades


async def filter_trades(assetClass: str = None, start: str = None, end: str = None,
                        tradeType: str = None, minPrice: float = None, maxPrice: float = None) -> List[Trade]:
    filters = TradeFilter(assetClass=assetClass, start=start, end=end,
                          tradeType=tradeType, minPrice=minPrice, maxPrice=maxPrice)
    filtered_trades = []
    for trade in trades:
        if filters.match(trade):
            filtered_trades.append(trade)
    return filtered_trades