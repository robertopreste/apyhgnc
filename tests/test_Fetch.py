#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from pandas.testing import assert_frame_equal
from apyhgnc.classes import Fetch


class TestFetch:
    f = Fetch("symbol", "ZNF3")

    def test_query(self, df_fetch_symbol_znf3):
        result = self.f.query()

        assert_frame_equal(result, df_fetch_symbol_znf3)

    def test_url(self):
        expect = "http://rest.genenames.org/fetch/symbol/ZNF3"
        result = self.f.url

        assert result == expect

    def test_repr(self):
        expect = "HGNC Fetch results"
        result = repr(self.f)

        assert result == expect
