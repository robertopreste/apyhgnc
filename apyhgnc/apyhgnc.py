#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import asyncio
import pandas as pd
from typing import Union
from .classes import Info, Search, Fetch


def info() -> Info:
    """
    Retrieve basic information from HGNC.

    :return: Info

    Example::

    >>> i = apyhgnc.info()
    >>> i.searchableFields  # list of searchable fields
    >>> i.storedFields      # list of stored fields
    >>> i.lastModified      # date of last HGNC database modification
    >>> i.numDoc            # number of entries in HGNC database
    """
    i = Info()
    return i


def search(*args, **kwargs) -> pd.DataFrame:
    """
    Launch a synchronous search on HGNC.

    :param args: either a single term to search all available fields,
        or a specific field and term to restrich the search

    :param kwargs: one or more keywork arguments with a field and a
        string or list of strings representing the search term(s)

    :return: pd.DataFrame

    Example::

    >>> apyhgnc.search("BRAF")              # search all searchable fields
    >>> apyhgnc.search("symbol", "BRAF")    # restrict search to symbol field
    >>> apyhgnc.search(symbol="BRAF")       # search with a keyword argument
    >>> apyhgnc.search(symbol=["BRAF", "ZNF"])  # search with OR
    >>> apyhgnc.search(symbol="BRAF", status="Approved")  # search multiple keywords
    """
    s = Search(*args, **kwargs)
    return s.query()


async def asearch(*args, **kwargs) -> pd.DataFrame:
    """
    Launch an asynchronous search on HGNC.

    :param args: either a single term to search all available fields,
        or a specific field and term to restrich the search

    :param kwargs: one or more keywork arguments with a field and a
        string or list of strings representing the search term(s)

    :return: pd.DataFrame

    Example::

    >>> import asyncio
    >>> loop = asyncio.get_event_loop()
    >>> loop.run_until_complete(apyhgnc.asearch("symbol", "BRAF"))
    """
    s = Search(*args, **kwargs)
    return await s.aquery()


def fetch(field: str, term: Union[str, int]) -> pd.DataFrame:
    """
    Launch a synchronous fetch from HGNC.

    :param str field: HGNC field to query

    :param Union[str,int] term: query term

    :return: pd.DataFrame

    Example::

    >>> apyhgnc.fetch("symbol", "ZNF3")
    """
    f = Fetch(field, term)
    return f.query()


async def afetch(field: str, term: Union[str, int]) -> pd.DataFrame:
    """
    Launch an asynchronous fetch from HGNC.

    :param str field: HGNC field to query

    :param Union[str,int] term: query term

    :return: pd.DataFrame

    Example::

    >>> import asyncio
    >>> loop = asyncio.get_event_loop()
    >>> loop.run_until_complete(apyhgnc.afetch("symbol", "ZNF3"))
    """
    f = Fetch(field, term)
    return await f.aquery()
