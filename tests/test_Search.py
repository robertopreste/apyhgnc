#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from apyhgnc.classes import Search


class TestSearchAll:
    s = Search("BRAF")

    def test_query(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097", "HGNC:43877", "HGNC:18615", "HGNC:379"],
            "score": [10.320703, 4.528981, 4.528981, 1.290088],
            "symbol": ["BRAF", "BANCR", "BRAFP1", "AKAP9"]
        })
        result = self.s.query()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/BRAF"
        result = self.s.url

        assert result == expect

    def test_repr(self):
        expect = "HGNC Search results"
        result = repr(self.s)

        assert result == expect


class TestSearchSymbol:
    s = Search("symbol", "BRAF")

    def test_query(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [10.972663],
            "symbol": ["BRAF"]
        })
        result = self.s.query()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol/BRAF"
        result = self.s.url

        assert result == expect

    def test_repr(self):
        expect = "HGNC Search results"
        result = repr(self.s)

        assert result == expect


class TestSearchKeyword:
    s = Search(symbol="BRAF")

    def test_query(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [10.972663],
            "symbol": ["BRAF"]
        })
        result = self.s.query()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol:BRAF"
        result = self.s.url

        assert result == expect

    def test_repr(self):
        expect = "HGNC Search results"
        result = repr(self.s)

        assert result == expect


class TestSearchKeywordOR:
    s = Search(symbol=["BRAF", "ZNF3"])

    def test_query(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:13089", "HGNC:1097"],
            "score": [5.1589246, 0.12897311],
            "symbol": ["ZNF3", "BRAF"]
        })
        result = self.s.query()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol:BRAF+OR+ZNF3"
        result = self.s.url

        assert result == expect

    def test_repr(self):
        expect = "HGNC Search results"
        result = repr(self.s)

        assert result == expect


class TestSearchKeywords:
    s = Search(symbol="BRAF", status="Approved")

    def test_query(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [11.020766],
            "symbol": ["BRAF"]
        })
        result = self.s.query()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol:BRAF+AND+status:Approved"
        result = self.s.url

        assert result == expect

    def test_repr(self):
        expect = "HGNC Search results"
        result = repr(self.s)

        assert result == expect
