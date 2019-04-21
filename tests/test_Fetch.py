#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
from apyhgnc.classes import Fetch


class TestFetch:
    f = Fetch("symbol", "ZNF3")

    def test_response(self):
        expect = {"numFound": 1, "start": 0, "docs": [
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
             "uuid": "2e1f2c0e-2a51-49c6-ae43-9c642f3f72d1",
             "_version_": 1631389725564600326}]}
        result = self.f.response

        assert result == expect

    def test_header(self):
        # QTime might be different, so I'm only testing the keys
        expect = {"status": 0, "QTime": 1}.keys()
        result = self.f.header.keys()

        assert result == expect

    def test_frame(self):
        expect = pd.DataFrame.from_records([
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
             "uuid": "2e1f2c0e-2a51-49c6-ae43-9c642f3f72d1",
             "_version_": 1631389725564600326}
        ])
        result = self.f.frame()

        assert_frame_equal(result, expect)

    def test_trans(self):
        expect = pd.DataFrame.from_records([
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
             "uuid": "2e1f2c0e-2a51-49c6-ae43-9c642f3f72d1",
             "_version_": 1631389725564600326}
        ]).transpose()
        result = self.f.trans()

        assert_frame_equal(result, expect)

    def test_url(self):
        expect = "http://rest.genenames.org/fetch/symbol/ZNF3"
        result = self.f.url

        assert result == expect

    def test_getitem(self):
        expect = pd.Series("HGNC:13089", name="hgnc_id")
        result = self.f["hgnc_id"]

        assert_series_equal(result, expect)

    def test_getattr(self):
        expect = pd.Series("HGNC:13089", name="hgnc_id")
        result = self.f.hgnc_id

        assert_series_equal(result, expect)

    def test_len(self):
        expect = 1
        result = len(self.f)

        assert result == expect
