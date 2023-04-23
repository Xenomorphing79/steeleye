from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TradeDetails(BaseModel):
    buy_sell_indicator: Optional[str] = Field(
        alias="buySellIndicator",
        description="Whether the trade was a buy or a sell"
    )
    price: float = Field(
        description="The price of the trade"
    )
    quantity: int = Field(
        description="The quantity of the trade"
    )


class Trade(BaseModel):
    asset_class: Optional[str] = Field(
        alias="assetClass",
        default=None,
        description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc"
    )
    counterparty: Optional[str] = Field(
        default=None,
        description="The counterparty the trade was executed with. May not always be available"
    )
    instrument_id: Optional[str] = Field(
        alias="instrumentId",
        description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc"
    )
    instrument_name: Optional[str] = Field(
        alias="instrumentName",
        description="The name of the instrument traded."
    )
    trade_date_time: Optional[datetime] = Field(
        alias="tradeDateTime",
        description="The date-time the Trade was executed"
    )
    trade_details: Optional[TradeDetails] = Field(
        alias="tradeDetails",
        description="The details of the trade, i.e. price, quantity"
    )
    trade_id: Optional[str] = Field(
        alias="tradeId",
        default=None,
        description="The unique ID of the trade"
    )
    trader: Optional[str] = Field(
        description="The name of the Trader"
    )
