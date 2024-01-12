# Streaming API

One additional benefit of the lazy API is that it allows queries to be executed in a streaming manner. Instead of processing the data all-at-once Polars can execute the query in batches allowing you to process datasets that are larger-than-memory.

To illustrate streaming we generate an example query on the Iris dataset.
{{code_block('user-guide/concepts/streaming','query',[''])}}

## Can my query be executed in streaming mode?
We can check which portions of a query plan can be executed in streaming mode by passing `streaming=True` to `explain`.

{{code_block('user-guide/concepts/streaming','streaming_query_plan',['explain'])}}
```python exec="on" session="user-guide/concepts/streaming"
--8<-- "python/user-guide/concepts/streaming.py:streaming_query_plan"
```

In a query plan the part of the query within the `---STREAMING` to `---END STREAMING` block can be executed in streaming mode. The rest of the query will be executed in non-streaming mode (i.e. all at once rather than in batches).

## Using the streaming API

To tell Polars we want to execute a query in streaming mode we pass the `streaming=True` argument to `collect`

{{code_block('user-guide/concepts/streaming','streaming',['collect'])}}



## When is streaming available?

Streaming is still in development. We can ask Polars to execute any lazy query in streaming mode. However, not all lazy operations support streaming. If there is an operation for which streaming is not supported Polars will run the query in non-streaming mode.

Streaming is supported for many operations including:

- `filter`,`slice`,`head`,`tail`
- `with_columns`,`select`
- `group_by`
- `join`
- `sort`
- `explode`,`melt`
- `scan_csv`,`scan_parquet`,`scan_ipc`
