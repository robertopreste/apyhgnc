#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import asyncio
import aiohttp
import requests
import urllib.parse
import pandas as pd
from typing import Dict, Any, Union, List


class _Server:
    """
    Basic server class used to call HGNC using sync or async calls.

    :param str host: url for the desired HGNC REST service
        (default: http://rest.genenames.org)
    """
    _BASE_URL = "http://rest.genenames.org/"

    def __init__(self,
                 host: str = _BASE_URL):
        self._url = host

    def _get_sync(self) -> Dict[str, Any]:
        """Synchronous call to HGNC.

        Make a sync call to HGNC's REST service and return a json
        dictionary.

        :return: Dict[str, Any]
        """
        resp = requests.get(self._url,
                            headers={"Accept": "application/json"})
        return resp.json()

    async def _get_async(self):
        """Asynchronous call to HGNC.

        :return:
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url,
                                   headers={"Accept": "application/json"}) as resp:
                return await resp.json()

    @property
    def url(self) -> str:
        """
        Return the URL used to retrieve results.

        :return: str
        """
        return self._url

    @staticmethod
    def _to_frame(response: Dict[str, Any]) -> pd.DataFrame:
        """
        Convert the given sync or async response to a DataFrame.

        :param Dict[str, Any] response: input response to convert

        :return: pd.DataFrame
        """
        return pd.DataFrame.from_records(response.get("docs"))

    def query(self) -> pd.DataFrame:
        """
        Perform a synchronous query on HGNC.

        :return: pd.DataFrame
        """
        resp = self._get_sync()
        response = resp.get("response", {"numFound": 0, "docs": []})

        return self._to_frame(response)

    async def aquery(self) -> pd.DataFrame:
        """
        Perform an asynchronous query on HGNC.

        :return: pd.DataFrame
        """
        resp = await self._get_async()
        response = resp.get("response", {"numFound": 0, "docs": []})

        return self._to_frame(response)


class Info:
    """
    Class used to retrieve information from HGNC.

    >>> i = Info()
    >>> i.searchableFields  # list of searchable fields
    >>> i.storedFields      # list of stored fields
    >>> i.lastModified      # date of last HGNC database modification
    >>> i.numDoc            # number of entries in HGNC database
    """

    def __init__(self) -> None:
        self._url = "http://rest.genenames.org/info"
        self._searchable = None
        self._stored = None
        self._modified = None
        self._numdoc = None
        self._response = self._get_sync()

    def _get_sync(self) -> Dict[str, Any]:
        """Synchronous call to HGNC.

        Make a sync call to HGNC's REST service and return a json
        dictionary.

        :return: Dict[str,Any]
        """
        resp = requests.get(self._url,
                            headers={"Accept": "application/json"})
        return resp.json()

    @property
    def url(self) -> str:
        """
        Return the URL used to retrieve results.

        :return: str
        """
        return self._url

    @property
    def response(self) -> Dict[str, Any]:
        """
        Return the raw response produced by the info call.

        :return: Dict[str,Any]
        """
        return self._response

    @property
    def searchableFields(self) -> List[str]:
        """
        Return the list of available searchable fields from HGNC.

        :return: List[str]
        """
        if self._searchable is None:
            self._searchable = self.response.get("searchableFields", "")
        return self._searchable

    @property
    def storedFields(self) -> List[str]:
        """
        Return the list of available stored fields from HGNC.

        :return: List[str]
        """
        if self._stored is None:
            self._stored = self.response.get("storedFields", "")
        return self._stored

    @property
    def lastModified(self) -> str:
        """
        Return the date and time when the HGNC server was last modified.

        :return: str
        """
        if self._modified is None:
            self._modified = self.response.get("lastModified", "")
        return self._modified

    @property
    def numDoc(self) -> int:
        """
        Return the number of entries currently present in the HGNC
        server.

        :return: int
        """
        if self._numdoc is None:
            self._numdoc = self.response.get("numDoc", 0)
        return self._numdoc

    def __repr__(self) -> str:
        return "HGNC Info results"


class Search(_Server):
    """
    Class used to look for entries of interest on HGNC.

    :param args: either a single term to search all available fields,
        or a specific field and term to restrich the search

    :param kwargs: one or more keywork arguments with a field and a
        string or list of strings representing the search term(s)

    Example::

    >>> Search("BRAF")              # search all searchable fields
    >>> Search("symbol", "BRAF")    # restrict search to symbol field
    >>> Search(symbol="BRAF")       # search with a keyword argument
    >>> Search(symbol=["BRAF", "ZNF"])              # search with OR
    >>> Search(symbol="BRAF", status="Approved")    # search multiple keywords
    """

    def __init__(self, *args, **kwargs):
        self._url = self._BASE_URL + "search/"
        if args:
            if len(args) == 1:
                term = urllib.parse.quote_plus(args[0])
                self._url += term
            elif len(args) == 2:
                field = urllib.parse.quote_plus(args[0])
                term = urllib.parse.quote_plus(args[1])
                self._url += "{}/{}".format(field, term)
        elif kwargs:
            q = []
            for key in kwargs:
                if isinstance(kwargs[key], list):
                    term = "+OR+".join(list(map(urllib.parse.quote_plus,
                                                kwargs[key])))
                else:
                    term = urllib.parse.quote_plus(kwargs[key])
                q.append("{}:{}".format(key, term))
            self._url += "+AND+".join(q)
        super().__init__(self._url)
        # self._response = self.get_sync()

    def __repr__(self):
        return "HGNC Search results"


class Fetch(_Server):
    """
    Class used to look for specific entries on HGNC.

    :param str field: HGNC field to query

    :param Union[str,int] term: query term

    Example::

    >>> Fetch("symbol", "ZNF3")
    """

    def __init__(self,
                 field: str,
                 term: Union[str, int]) -> None:
        self._url = self._BASE_URL + "fetch/"
        field = urllib.parse.quote_plus(field)
        term = urllib.parse.quote_plus(term)
        self._url += "{}/{}".format(field, term)
        super().__init__(self._url)

    def __repr__(self):
        return "HGNC Fetch results"
