import pandas as pd


def _sma(data, period=50):
    """
    Parameters
    ----------
    data: pandas dataframe
        Dataframe populated with prices.
    period: int
        Lookback period to compute the SMA.
    """
    SMA = data.rolling(window=period).mean()

    return SMA


def _std(data, period=50):
    """
    Parameters
    ----------
    data: pandas dataframe
        Dataframe populated with prices.
    period: int
        Lookback period to compute the SMA.
    """
    std = data.rolling(window=period)

    return std


def _PM(prices_df, sma_df):
    """
    Parameters
    ----------
    prices_df: pandas dataframe
        Dataframe containing prices.
    sma_df: pandas dataframe
     Dataframe containing sma data.
    """
    PM = (prices_df - sma_df) / sma_df

    return PM
