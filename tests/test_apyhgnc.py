#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import asyncio
from pandas.testing import assert_frame_equal
from apyhgnc import apyhgnc


# apyhgnc.info

def test_info_searchableFields(searchable_fields):
    result = apyhgnc.info().searchableFields
    assert result == searchable_fields


def test_info_storedFields(stored_fields):
    result = apyhgnc.info().storedFields
    assert result == stored_fields


def test_info_url():
    result = apyhgnc.info().url
    assert result == "http://rest.genenames.org/info"


def test_info_numDoc():
    result = apyhgnc.info().numDoc
    assert result == 42969


# apyhgnc.fetch

def test_fetch_symbol_znf3(df_fetch_symbol_znf3):
    result = apyhgnc.fetch("symbol", "ZNF3")
    assert_frame_equal(result, df_fetch_symbol_znf3)


def test_fetch_symbol_znf3_async(df_fetch_symbol_znf3):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        apyhgnc.afetch("symbol", "ZNF3")
    )
    assert_frame_equal(result, df_fetch_symbol_znf3)


# apyhgnc.search

def test_search_all_braf(df_search_all_braf):
    result = apyhgnc.search("BRAF")
    assert_frame_equal(result, df_search_all_braf)


def test_search_all_braf_async(df_search_all_braf):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        apyhgnc.asearch("BRAF")
    )
    assert_frame_equal(result, df_search_all_braf)


def test_search_symbol_braf(df_search_symbol_braf):
    result = apyhgnc.search("symbol", "BRAF")
    assert_frame_equal(result, df_search_symbol_braf)


def test_search_symbol_braf_async(df_search_symbol_braf):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        apyhgnc.asearch("symbol", "BRAF")
    )
    assert_frame_equal(result, df_search_symbol_braf)


def test_search_symbols_braf_znf3(df_search_symbols_braf_znf3):
    result = apyhgnc.search(symbol=["BRAF", "ZNF3"])
    assert_frame_equal(result, df_search_symbols_braf_znf3)


def test_search_symbols_braf_znf3_async(df_search_symbols_braf_znf3):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        apyhgnc.asearch(symbol=["BRAF", "ZNF3"])
    )
    assert_frame_equal(result, df_search_symbols_braf_znf3)


def test_search_symbol_and_status(df_search_symbol_and_status):
    result = apyhgnc.search(symbol="BRAF", status="Approved")
    assert_frame_equal(result, df_search_symbol_and_status)


def test_search_symbol_and_status_async(df_search_symbol_and_status):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        apyhgnc.asearch(symbol="BRAF", status="Approved")
    )
    assert_frame_equal(result, df_search_symbol_and_status)
