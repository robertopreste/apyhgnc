#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from apyhgnc.classes import Search


class TestSearchAll:
    s = Search("BRAF")

    def test_query(self, df_search_all_braf):
        result = self.s.query()

        assert_frame_equal(result, df_search_all_braf)

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

    def test_query(self, df_search_symbol_braf):
        result = self.s.query()

        assert_frame_equal(result, df_search_symbol_braf)

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

    def test_query(self, df_search_symbol_braf):
        result = self.s.query()

        assert_frame_equal(result, df_search_symbol_braf)

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

    def test_query(self, df_search_symbols_braf_znf3):
        result = self.s.query()

        assert_frame_equal(result, df_search_symbols_braf_znf3)

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

    def test_query(self, df_search_symbol_and_status):
        result = self.s.query()

        assert_frame_equal(result, df_search_symbol_and_status)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol:BRAF+AND+status:Approved"
        # python 3.5 has random order of arguments
        expect2 = "http://rest.genenames.org/search/status:Approved+AND+symbol:BRAF"
        result = self.s.url

        assert result == expect or result == expect2

    def test_repr(self):
        expect = "HGNC Search results"
        result = repr(self.s)

        assert result == expect
