#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import requests
import urllib.parse
import pandas as pd
from typing import Dict, Any, Union, List


class Server:
    """
    Basic server class used to call HGNC using sync or async calls.

    :param str host: url for the desired HGNC REST service
    (default: http://rest.genenames.org)
    """
    _BASE_URL = "http://rest.genenames.org/"

    def __init__(self,
                 host: str = _BASE_URL):
        self._url = host
        self._response = self.get_sync()

    def get_sync(self) -> Dict[str, Any]:
        """Synchronous call to HGNC.

        Make a sync call to HGNC's REST service and return a json
        dictionary.
        :return: Dict[str, Any]
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
    def header(self) -> Dict[str, Any]:
        """
        Return the response header produced by the call.
        :return: Dict[str, Any]
        """
        return self._response.get("responseHeader", {"status": 0})

    @property
    def response(self) -> Dict[str, Any]:
        """
        Return the response content produced by the call.
        :return: Dict[str, Any]
        """
        return self._response.get("response", {"numFound": 0, "docs": []})


class Info(Server):
    """
    Class used to retrieve information from HGNC.

    >>> i = Info()
    >>> i.searchableFields  # list of searchable fields
    >>> i.storedFields      # list of stored fields
    """

    def __init__(self) -> None:
        self._url = self._BASE_URL + "info"
        super().__init__(self._url)
        self._searchable = None
        self._stored = None
        self._modified = None
        self._numdoc = None

    @property
    def response(self) -> Dict[str, Any]:
        """
        Return the raw response produced by the info call
        (overrides Server.response).
        :return: Dict[str, Any]
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
    def lastModified(self):
        if self._modified is None:
            self._modified = self.response.get("lastModified", "")
        return self._modified

    @property
    def numDoc(self):
        if self._numdoc is None:
            self._numdoc = self.response.get("numDoc", 0)
        return self._numdoc

    def __repr__(self) -> str:
        return "HGNC Info results"


class Search(Server):
    """
    Class used to look for entries of interest on HGNC.

    >>> Search("BRAF")  # search all searchable fields
    >>> Search("symbol", "BRAF")  # restrict search to symbol field
    >>> Search(symbol="BRAF")  # search with a keyword argument
    >>> Search(symbol=["BRAF", "ZNF"])  # search with OR
    >>> Search(symbol="BRAF", status="Approved")  # search multiple keywords
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

    def frame(self) -> pd.DataFrame:
        """
        Return a pandas dataframe with the retrieved results.
        :return: pd.DataFrame
        """
        return pd.DataFrame.from_records(self.response.get("docs"))

    def trans(self) -> pd.DataFrame:
        """
        Return a simpler view of the dataframe by calling its transpose.
        :return: pd.DataFrame
        """
        return self.frame().T

    def __getitem__(self, item):
        return self.frame().get(item, "{} not found".format(item))

    def __getattr__(self, item):
        return self.frame().get(item, "{} not found".format(item))

    def __len__(self) -> int:
        return self.response.get("numFound", 0)

    def __repr__(self):
        return "HGNC Search results ({} entries found).".format(self.__len__())


class Fetch(Server):
    """
    Class used to look for specific entries on HGNC.

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

    def frame(self) -> pd.DataFrame:
        """
        Return a pandas dataframe with the retrieved results.
        :return: pd.DataFrame
        """
        return pd.DataFrame.from_records(self.response.get("docs"))

    def trans(self) -> pd.DataFrame:
        """
        Return a simpler view of the dataframe by calling its transpose.
        :return: pd.DataFrame
        """
        return self.frame().T

    def __getitem__(self, item):
        return self.frame().get(item, "{} not found".format(item))

    def __getattr__(self, item):
        return self.frame().get(item, "{} not found".format(item))

    def __len__(self) -> int:
        return self.response.get("numFound", 0)

    def __repr__(self):
        return "HGNC Fetch results ({} entries found).".format(self.__len__())
