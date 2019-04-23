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
        """
    s = Search(*args, **kwargs)
    return await s.aquery()


def fetch(field: str, term: Union[str, int]) -> pd.DataFrame:
    """
    Launch a synchronous fetch from HGNC.

    :param str field: HGNC field to query

    :param Union[str,int] term: query term

    :return: pd.DataFrame
    """
    f = Fetch(field, term)
    return f.query()


async def afetch(field: str, term: Union[str, int]) -> pd.DataFrame:
    """
    Launch an asynchronous fetch from HGNC.

    :param str field: HGNC field to query

    :param Union[str,int] term: query term

    :return: pd.DataFrame
    """
    f = Fetch(field, term)
    return await f.aquery()
