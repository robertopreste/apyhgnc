#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from apyhgnc.classes import Info


class TestInfo:
    i = Info()

    def test_searchableFields(self):
        expect = ["vega_id", "locus_group", "alias_symbol",
                  "rna_central_id", "prev_name", "refseq_accession",
                  "hgnc_id", "entrez_id", "symbol", "name", "mgd_id",
                  "prev_symbol", "alias_name", "status", "locus_type",
                  "rgd_id", "ensembl_gene_id", "omim_id", "ucsc_id",
                  "uniprot_ids", "ena", "ccds_id", "gene_group_id",
                  "location_sortable"]
        result = self.i.searchableFields

        assert result == expect

    def test_storedFields(self):
        expect = ["vega_id", "locus_group", "alias_symbol", "_version_",
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
        result = self.i.storedFields

        assert result == expect

    def test_url(self):
        expect = "http://rest.genenames.org/info"
        result = self.i.url

        assert result == expect

    def test_header(self):
        # QTime might be different, so I'm only testing the keys
        expect = {"status": 0, "QTime": 1}.keys()
        result = self.i.header.keys()

        assert result == expect
