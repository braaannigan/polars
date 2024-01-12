import polars as pl

# --8<-- [start:query]
q = (
    pl.scan_csv("docs/data/iris.csv")
    .filter(pl.col("sepal_length") > 5)
    .group_by("species")
    .agg(pl.col("sepal_width").mean())
)
# --8<-- [end:query]

# --8<-- [start:streaming_query_plan]
import polars as pl

q = (
    pl.scan_csv("docs/data/iris.csv")
    .filter(pl.col("sepal_length") > 5)
    .group_by("species")
    .agg(pl.col("sepal_width").mean())
)
q.explain(streaming=True)
# --8<-- [end:streaming_query_plan]


# --8<-- [start:streaming]
df = q.collect(streaming=True)
# --8<-- [end:streaming]

# # --8<-- [start:non_streaming_query]
# q_shift = (
#     pl.scan_csv("docs/data/iris.csv")
#     .with_columns(pl.col("sepal_length").shift(1))
#     .group_by("species")
#     .agg(pl.col("sepal_width").mean())
# )

# # --8<-- [end:non_streaming_query]
# # --8<-- [start:non_streaming_query_plan]
# q_shift.explain(streaming=True)
# # --8<-- [end:non_streaming_query_plan]
