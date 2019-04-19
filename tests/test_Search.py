#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
from apyhgnc.classes import Search


class TestSearchAll:
    s = Search("BRAF")

    def test_response(self):
        expect = {"numFound": 4, "start": 0, "maxScore": 10.320703,
                  "docs": [{"hgnc_id": "HGNC:1097", "symbol": "BRAF",
                            "score": 10.320703},
                           {"hgnc_id": "HGNC:43877", "symbol": "BANCR",
                            "score": 4.5289807},
                           {"hgnc_id": "HGNC:18615", "symbol": "BRAFP1",
                            "score": 4.5289807},
                           {"hgnc_id": "HGNC:379", "symbol": "AKAP9",
                            "score": 1.2900878}]
                  }
        result = self.s.response

        assert result == expect

    def test_header(self):
        # QTime might be different, so I'm only testing the keys
        expect = {"status": 0, "QTime": 2}.keys()
        result = self.s.header.keys()

        assert result == expect

    def test_frame(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097", "HGNC:43877", "HGNC:18615", "HGNC:379"],
            "score": [10.320703, 4.528981, 4.528981, 1.290088],
            "symbol": ["BRAF", "BANCR", "BRAFP1", "AKAP9"]
        })
        result = self.s.frame()

        assert_frame_equal(result, expect)

    def test_trans(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097", "HGNC:43877", "HGNC:18615", "HGNC:379"],
            "score": [10.320703, 4.528981, 4.528981, 1.290088],
            "symbol": ["BRAF", "BANCR", "BRAFP1", "AKAP9"]
        }).transpose()
        result = self.s.trans()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/BRAF"
        result = self.s.url

        assert result == expect

    def test_getitem(self):
        expect = pd.Series(["HGNC:1097", "HGNC:43877", "HGNC:18615",
                            "HGNC:379"], name="hgnc_id")
        result = self.s["hgnc_id"]

        assert_series_equal(result, expect)

    def test_getattr(self):
        expect = pd.Series(["HGNC:1097", "HGNC:43877", "HGNC:18615",
                            "HGNC:379"], name="hgnc_id")
        result = self.s.hgnc_id

        assert_series_equal(result, expect)

    def test_len(self):
        expect = 4
        result = len(self.s)

        assert result == expect


class TestSearchSymbol:
    s = Search("symbol", "BRAF")

    def test_response(self):
        expect = {"numFound": 1, "start": 0, "maxScore": 10.972663,
                  "docs": [{"hgnc_id": "HGNC:1097", "symbol": "BRAF",
                            "score": 10.972663}]}
        result = self.s.response

        assert result == expect

    def test_header(self):
        # QTime might be different, so I'm only testing the keys
        expect = {"status": 0, "QTime": 2}.keys()
        result = self.s.header.keys()

        assert result == expect

    def test_frame(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [10.972663],
            "symbol": ["BRAF"]
        })
        result = self.s.frame()

        assert_frame_equal(result, expect)

    def test_trans(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [10.972663],
            "symbol": ["BRAF"]
        }).transpose()
        result = self.s.trans()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol/BRAF"
        result = self.s.url

        assert result == expect

    def test_getitem(self):
        expect = pd.Series("HGNC:1097", name="hgnc_id")
        result = self.s["hgnc_id"]

        assert_series_equal(result, expect)

    def test_getattr(self):
        expect = pd.Series("HGNC:1097", name="hgnc_id")
        result = self.s.hgnc_id

        assert_series_equal(result, expect)

    def test_len(self):
        expect = 1
        result = len(self.s)

        assert result == expect


class TestSearchKeyword:
    s = Search(symbol="BRAF")

    def test_response(self):
        expect = {"numFound": 1, "start": 0, "maxScore": 10.972663,
                  "docs": [{"hgnc_id": "HGNC:1097", "symbol": "BRAF",
                            "score": 10.972663}]}
        result = self.s.response

        assert result == expect

    def test_header(self):
        # QTime might be different, so I'm only testing the keys
        expect = {"status": 0, "QTime": 2}.keys()
        result = self.s.header.keys()

        assert result == expect

    def test_frame(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [10.972663],
            "symbol": ["BRAF"]
        })
        result = self.s.frame()

        assert_frame_equal(result, expect)

    def test_trans(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [10.972663],
            "symbol": ["BRAF"]
        }).transpose()
        result = self.s.trans()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol:BRAF"
        result = self.s.url

        assert result == expect

    def test_getitem(self):
        expect = pd.Series("HGNC:1097", name="hgnc_id")
        result = self.s["hgnc_id"]

        assert_series_equal(result, expect)

    def test_getattr(self):
        expect = pd.Series("HGNC:1097", name="hgnc_id")
        result = self.s.hgnc_id

        assert_series_equal(result, expect)

    def test_len(self):
        expect = 1
        result = len(self.s)

        assert result == expect


class TestSearchKeywordOR:
    s = Search(symbol=["BRAF", "ZNF3"])

    def test_response(self):
        expect = {"numFound": 2, "start": 0, "maxScore": 5.1589246,
                  "docs": [{"hgnc_id": "HGNC:13089", "symbol": "ZNF3",
                            "score": 5.1589246},
                           {"hgnc_id": "HGNC:1097", "symbol": "BRAF",
                            "score": 0.12897311}]}
        result = self.s.response

        assert result == expect

    def test_header(self):
        # QTime might be different, so I'm only testing the keys
        expect = {"status": 0, "QTime": 2}.keys()
        result = self.s.header.keys()

        assert result == expect

    def test_frame(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:13089", "HGNC:1097"],
            "score": [5.1589246, 0.12897311],
            "symbol": ["ZNF3", "BRAF"]
        })
        result = self.s.frame()

        assert_frame_equal(result, expect)

    def test_trans(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:13089", "HGNC:1097"],
            "score": [5.1589246, 0.12897311],
            "symbol": ["ZNF3", "BRAF"]
        }).transpose()
        result = self.s.trans()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol:BRAF+OR+ZNF3"
        result = self.s.url

        assert result == expect

    def test_getitem(self):
        expect = pd.Series(["HGNC:13089", "HGNC:1097"], name="hgnc_id")
        result = self.s["hgnc_id"]

        assert_series_equal(result, expect)

    def test_getattr(self):
        expect = pd.Series(["HGNC:13089", "HGNC:1097"], name="hgnc_id")
        result = self.s.hgnc_id

        assert_series_equal(result, expect)

    def test_len(self):
        expect = 2
        result = len(self.s)

        assert result == expect


class TestSearchKeywords:
    s = Search(symbol="BRAF", status="Approved")

    def test_response(self):
        expect = {"numFound": 1, "start": 0, "maxScore": 11.020766,
                  "docs": [{"hgnc_id": "HGNC:1097", "symbol": "BRAF",
                            "score": 11.020766}]}
        result = self.s.response

        assert result == expect

    def test_header(self):
        # QTime might be different, so I'm only testing the keys
        expect = {"status": 0, "QTime": 2}.keys()
        result = self.s.header.keys()

        assert result == expect

    def test_frame(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [11.020766],
            "symbol": ["BRAF"]
        })
        result = self.s.frame()

        assert_frame_equal(result, expect)

    def test_trans(self):
        expect = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [11.020766],
            "symbol": ["BRAF"]
        }).transpose()
        result = self.s.trans()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/search/symbol:BRAF+AND+status:Approved"
        result = self.s.url

        assert result == expect

    def test_getitem(self):
        expect = pd.Series("HGNC:1097", name="hgnc_id")
        result = self.s["hgnc_id"]

        assert_series_equal(result, expect)

    def test_getattr(self):
        expect = pd.Series("HGNC:1097", name="hgnc_id")
        result = self.s.hgnc_id

        assert_series_equal(result, expect)

    def test_len(self):
        expect = 1
        result = len(self.s)

        assert result == expect
