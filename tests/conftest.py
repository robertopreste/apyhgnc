#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pandas as pd
from typing import List


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
    df = pd.DataFrame.from_records([
            {"hgnc_id": "HGNC:13089", "symbol": "ZNF3",
             "name": "zinc finger protein 3", "status": "Approved",
             "locus_type": "gene with protein product",
             "prev_name": ["zinc finger protein 3 (A8-51)"],
             "alias_symbol": ["A8-51", "KOX25", "PP838", "FLJ20216",
                              "HF.12", "Zfp113"],
             "location": "7q22.1",
             "date_approved_reserved": "1989-05-31T00:00:00Z",
             "date_modified": "2016-10-25T00:00:00Z",
             "date_name_changed": "2006-05-05T00:00:00Z",
             "ena": ["AF027136"], "entrez_id": "7551",
             "mgd_id": ["MGI:1929116"], "kznf_gene_catalog": 460,
             "cosmic": "ZNF3", "refseq_accession": ["NM_017715"],
             "gene_group": ["Zinc fingers C2H2-type"],
             "vega_id": "OTTHUMG00000154596",
             "ensembl_gene_id": "ENSG00000166526",
             "ccds_id": ["CCDS43618", "CCDS43619"],
             "locus_group": "protein-coding gene", "omim_id": ["194510"],
             "uniprot_ids": ["P17036"], "ucsc_id": "uc031syk.2",
             "rgd_id": ["RGD:6489147"], "gene_group_id": [28],
             "location_sortable": "07q22.1",
             "uuid": "fe919e33-ad54-436f-9c3b-06dbc3fd0bf5",
             "_version_": 1631664295862337544}
        ])
    return df


@pytest.fixture
def df_search_all_braf() -> pd.DataFrame:
    """
    Return a dataframe with search results for BRAF (all fields).

    :return: pd.DataFrame
    """
    df = pd.DataFrame({
            "hgnc_id": ["HGNC:1097", "HGNC:43877", "HGNC:18615", "HGNC:379"],
            "score": [10.320703, 4.528981, 4.528981, 1.290088],
            "symbol": ["BRAF", "BANCR", "BRAFP1", "AKAP9"]
        })
    return df


@pytest.fixture
def df_search_symbol_braf() -> pd.DataFrame:
    """
    Return a dataframe with search results for symbol = BRAF.

    :return: pd.DataFrame
    """
    df = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [10.972663],
            "symbol": ["BRAF"]
        })
    return df


@pytest.fixture
def df_search_symbols_braf_znf3() -> pd.DataFrame:
    """
    Return a dataframe with search results for symbol = ["BRAF", "ZNF3"].

    :return: pd.DataFrame
    """
    df = pd.DataFrame({
            "hgnc_id": ["HGNC:13089", "HGNC:1097"],
            "score": [5.1589246, 0.12897311],
            "symbol": ["ZNF3", "BRAF"]
        })
    return df


@pytest.fixture
def df_search_symbol_and_status() -> pd.DataFrame:
    """
    Return a dataframe with search results for symbol = "BRAF"
    AND status = "Approved".

    :return: pd.DataFrame
    """
    df = pd.DataFrame({
            "hgnc_id": ["HGNC:1097"],
            "score": [11.020766],
            "symbol": ["BRAF"]
        })
    return df
