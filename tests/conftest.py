#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
import pickle
import pandas as pd
from typing import List

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


@pytest.fixture
def searchable_fields() -> List[str]:
    fields = ["vega_id", "locus_group", "alias_symbol",
              "rna_central_id", "prev_name", "refseq_accession",
              "hgnc_id", "entrez_id", "symbol", "name", "mgd_id",
              "prev_symbol", "alias_name", "status", "locus_type",
              "rgd_id", "ensembl_gene_id", "omim_id", "ucsc_id",
              "uniprot_ids", "ena", "ccds_id", "gene_group_id",
              "location_sortable"]
    return fields


@pytest.fixture
def stored_fields() -> List[str]:
    fields = ["vega_id", "locus_group", "alias_symbol", "_version_",
              "uuid", "rna_central_id", "prev_name",
              "refseq_accession", "mirbase", "lsdb", "homeodb",
              "hgnc_id", "cosmic", "entrez_id", "symbol",
              "location", "name", "mgd_id", "snornabase",
              "prev_symbol", "bioparadigms_slc", "orphanet",
              "alias_name", "date_approved_reserved", "status",
              "pseudogene.org", "merops", "horde_id", "locus_type",
              "imgt", "iuphar", "rgd_id", "kznf_gene_catalog",
              "ensembl_gene_id", "gtrnadb", "mamit-trnadb",
              "gene_group", "omim_id", "date_name_changed", "cd",
              "date_modified", "lncipedia", "ucsc_id", "lncrnadb",
              "enzyme_id", "uniprot_ids",
              "intermediate_filament_db", "ena", "ccds_id",
              "pubmed_id", "date_symbol_changed", "gene_group_id",
              "location_sortable"]
    return fields


@pytest.fixture
def df_fetch_symbol_znf3() -> pd.DataFrame:
    """
    Return a dataframe with fetch results for symbol = ZNF3.

    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "fetch_symbol_ZNF3.pkl"))
    return df


@pytest.fixture
def df_search_all_braf() -> pd.DataFrame:
    """
    Return a dataframe with search results for BRAF (all fields).

    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "search_all_BRAF.pkl"))
    return df


@pytest.fixture
def df_search_symbol_braf() -> pd.DataFrame:
    """
    Return a dataframe with search results for symbol = BRAF.

    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "search_symbol_BRAF.pkl"))
    return df


@pytest.fixture
def df_search_symbols_braf_znf3() -> pd.DataFrame:
    """
    Return a dataframe with search results for symbol = ["BRAF", "ZNF3"].

    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "search_symbols_BRAF_ZNF3.pkl"))
    return df


@pytest.fixture
def df_search_symbol_and_status() -> pd.DataFrame:
    """
    Return a dataframe with search results for symbol = "BRAF"
    AND status = "Approved".

    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "search_symbol_and_status.pkl"))
    return df
