#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from apyhgnc.classes import Info


class TestInfo:
    i = Info()

    def test_searchableFields(self, searchable_fields):
        result = self.i.searchableFields

        assert result == searchable_fields

    def test_storedFields(self, stored_fields):
        result = self.i.storedFields

        assert result == stored_fields

    def test_url(self):
        expect = "http://rest.genenames.org/info"
        result = self.i.url

        assert result == expect

    def test_numDoc(self):
        expect = 42969
        result = self.i.numDoc

        assert result == expect

    def test_repr(self):
        expect = "HGNC Info results"
        result = repr(self.i)

        assert result == expect
