#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pandas as pd
import apyhgnc as apy

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


def create_fetch_symbol_znf3() -> bool:
    """Create and store Fetch results for symbol = ZNF3.

    :return: bool
    """
    df = apy.fetch("symbol", "ZNF3")
    df.to_pickle(os.path.join(DATADIR, "fetch_symbol_ZNF3.pkl"))
    return True


def create_search_all_braf() -> bool:
    """Create and store Search results for BRAF (all fields).

    :return: bool
    """
    df = apy.search("BRAF")
    df.to_pickle(os.path.join(DATADIR, "search_all_BRAF.pkl"))
    return True


def create_search_symbol_braf() -> bool:
    """Create and store Search results for symbol = BRAF.

    :return: bool
    """
    df = apy.search("symbol", "BRAF")
    df.to_pickle(os.path.join(DATADIR, "search_symbol_BRAF.pkl"))
    return True


def create_search_symbols_braf_znf3() -> bool:
    """Create and store Search results for symbol = ["BRAF", "ZNF3"].

    :return: bool
    """
    df = apy.search(symbol=["BRAF", "ZNF3"])
    df.to_pickle(os.path.join(DATADIR, "search_symbols_BRAF_ZNF3.pkl"))
    return True


def create_search_symbol_and_status() -> bool:
    """Create and store Search results for symbol = "BRAF" AND status = "Approved".

    :return: bool
    """
    df = apy.search(symbol="BRAF", status="Approved")
    df.to_pickle(os.path.join(DATADIR, "search_symbol_and_status.pkl"))
    return True


def main():
    print("Downloading and saving fetch results... ", end="")
    create_fetch_symbol_znf3()
    print("Done.")
    print("Downloading and saving search results... ", end="")
    create_search_all_braf()
    create_search_symbol_braf()
    create_search_symbols_braf_znf3()
    create_search_symbol_and_status()
    print("Done.")


if __name__ == '__main__':
    main()
