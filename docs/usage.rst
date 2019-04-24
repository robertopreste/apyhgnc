=====
Usage
=====

To use apyhgnc in a project::

    import apyhgnc

The apyhgnc package mimics the `HGNC REST service`_, so the main types of requests it can handle are **info**, **fetch** and **search**.

Info
----

From the `HGNC REST service`_ documentation:

    The info request is used to request information about the service rather than fetching any data from the server. The response from info will contain information such as when the data within the server was last updated (lastModified), the number of documents (numDoc), which fields can be queried using search and fetch (searchableFields) and which fields may be returned by fetch (storedFields).

Available information can be retrieved using the ``info()`` function and the related attributes::

    from apyhgnc import info

    i = info()
    i.lastModified      # list of searchable fields
    i.numDoc            # list of stored fields
    i.searchableFields  # date of last HGNC database modification
    i.storedFields      # number of entries in HGNC database

An Info instance can be created using the ``Info`` class, and related attributes can be retrieved easily::

    from apyhgnc import Info

    i = Info()
    i.lastModified
    i.numDoc
    i.searchableFields
    i.storedFields

Fetch
-----

From the `HGNC REST service`_ documentation:

    The fetch request is the main request to retrieve particular records for the server that will return back all the fields as seen in the "storedFields" section of the info response. The fetch method requires the user to add the queriable field (as seen in the "searchableFields" section of the info) and the query term to the url.

Fetch queries can be used to retrieve the available information for an entity in HGNC, and can be issued either synchronously, using the ``fetch()`` function, or asynchronously, using the ``afetch()`` function::

    from apyhgnc import fetch, afetch

    # synchronous query
    f = fetch("symbol", "ZNF3")

    # asynchronous query
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(afetch("symbol", "ZNF3"))

Fetch requests can also be issued using the ``Fetch`` class and specifying a query field and value::

    from apyhgnc import Fetch

    f = Fetch("symbol", "ZNF3")

Entries retrieved from HGNC are returned as a dataframe; queries can be launched either synchronously or asynchronously::

    f.query()   # synchronous query
    f.aquery()  # asynchronous query (will return an asyncio.future)

Search
------

From the `HGNC REST service`_ documentation:

    The search request is more powerful than fetch for querying the database, but search will only returns the fields hgnc_id, symbol and score. This is because this tool is mainly intended to query the server to find possible entries of interest or to check data (such as your own symbols) rather than to fetch information about the genes.

Search queries allow to either search all available fields for a query term (using only one argument), or restrict the search to a specific field (using two arguments). Keyword arguments allow to perform AND/OR queries (see example below). Search queries can be issued either synchronously, using the ``search()`` function, or asynchronously, using the ``asearch()`` function::

    from apyhgnc import search, asearch

    # synchronous query
    s = search("BRAF")
    s = search("symbol", "BRAF")
    s = search(symbol="BRAF")
    s = search(symbol=["BRAF", "ZNF3"])
    s = search(symbol="BRAF", status="Approved")

    # asynchronous query
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asearch("symbol", "BRAF"))


Search requests can also be performed using the ``Search`` class; using a single argument allows to search all available fields for that term, while using two arguments allows to restrict the search to a specific field::

    from apyhgnc import Search

    s1 = Search("BRAF")
    s2 = Search("symbol", "BRAF")

It is also possible to use keyword arguments, and this allows to include powerful AND/OR queries as well::

    s1 = Search(symbol="BRAF")
    s2 = Search(symbol=["BRAF", "ZNF3"])  # will search for BRAF OR ZNF3 in the symbol field
    s3 = Search(symbol="BRAF", status="Approved")  # will search for symbol=BRAF AND status=Approved

Common attributes
-----------------

In addition to the above-mentioned methods and attributes, there are others that are shared among the ``Info``, ``Fetch`` and ``Search`` classes:

* the ``.url`` attribute returns the URL used to retrieve results from HGNC.


.. _`HGNC REST service`: https://www.genenames.org/help/rest/
