import contextlib
import os

with contextlib.suppress(ImportError):  # Module not available when building docs
    # ensure the object constructor is known by polars
    # we set this once on import

    # we also set other function pointers needed
    # on the rust side. This function is highly
    # unsafe and should only be called once.
    from polars.polars import __register_startup_deps

    __register_startup_deps()

from polars import api
from polars.config import Config
from polars.convert import (
    from_arrow,
    from_dict,
    from_dicts,
    from_numpy,
    from_pandas,
    from_records,
    from_repr,
)
from polars.dataframe import DataFrame
from polars.datatypes import (
    DATETIME_DTYPES,
    DURATION_DTYPES,
    FLOAT_DTYPES,
    INTEGER_DTYPES,
    NUMERIC_DTYPES,
    TEMPORAL_DTYPES,
    Array,
    Binary,
    Boolean,
    Categorical,
    DataType,
    Date,
    Datetime,
    Decimal,
    Duration,
    Field,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    List,
    Null,
    Object,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Unknown,
    Utf8,
)
from polars.exceptions import (
    ArrowError,
    ChronoFormatWarning,
    ColumnNotFoundError,
    ComputeError,
    DuplicateError,
    InvalidOperationError,
    NoDataError,
    PolarsPanicError,
    SchemaError,
    SchemaFieldNotFoundError,
    ShapeError,
    StructFieldNotFoundError,
)
from polars.expr import Expr
from polars.functions import (
    align_frames,
    all,
    all_horizontal,
    any,
    any_horizontal,
    apply,
    approx_n_unique,
    arange,
    arctan2,
    arctan2d,
    arg_sort_by,
    arg_where,
    avg,
    coalesce,
    col,
    collect_all,
    collect_all_async,
    concat,
    concat_list,
    concat_str,
    corr,
    count,
    cov,
    cumfold,
    cumreduce,
    cumsum,
    cumsum_horizontal,
    date,
    date_range,
    date_ranges,
    datetime,
    datetime_range,
    datetime_ranges,
    duration,
    element,
    exclude,
    first,
    fold,
    format,
    from_epoch,
    groups,
    head,
    implode,
    int_range,
    int_ranges,
    last,
    lit,
    map,
    map_batches,
    map_groups,
    max,
    max_horizontal,
    mean,
    median,
    min,
    min_horizontal,
    n_unique,
    ones,
    quantile,
    reduce,
    repeat,
    rolling_corr,
    rolling_cov,
    select,
    set_random_seed,
    sql_expr,
    std,
    struct,
    sum,
    sum_horizontal,
    tail,
    time,
    time_range,
    time_ranges,
    var,
    when,
    zeros,
)
from polars.interchange.from_dataframe import from_dataframe
from polars.io import (
    read_avro,
    read_csv,
    read_csv_batched,
    read_database,
    read_database_uri,
    read_delta,
    read_excel,
    read_ipc,
    read_ipc_schema,
    read_ipc_stream,
    read_json,
    read_ndjson,
    read_ods,
    read_parquet,
    read_parquet_schema,
    scan_csv,
    scan_delta,
    scan_ipc,
    scan_ndjson,
    scan_parquet,
    scan_pyarrow_dataset,
)
from polars.lazyframe import LazyFrame
from polars.series import Series
from polars.sql import SQLContext
from polars.string_cache import StringCache, enable_string_cache, using_string_cache
from polars.type_aliases import PolarsDataType
from polars.utils import build_info, get_index_type, show_versions, threadpool_size

# TODO: remove need for importing wrap utils at top level
from polars.utils._wrap import wrap_df, wrap_s  # noqa: F401
from polars.utils.polars_version import get_polars_version as _get_polars_version

__version__: str = _get_polars_version()
del _get_polars_version

__all__ = [
    "api",
    "exceptions",
    # exceptions/errors
    "ArrowError",
    "ColumnNotFoundError",
    "ComputeError",
    "ChronoFormatWarning",
    "DuplicateError",
    "InvalidOperationError",
    "NoDataError",
    "PolarsPanicError",
    "SchemaError",
    "SchemaFieldNotFoundError",
    "ShapeError",
    "StructFieldNotFoundError",
    # core classes
    "DataFrame",
    "Expr",
    "LazyFrame",
    "Series",
    # polars.datatypes
    "Array",
    "Binary",
    "Boolean",
    "Categorical",
    "DataType",
    "Date",
    "Datetime",
    "Decimal",
    "Duration",
    "Field",
    "Float32",
    "Float64",
    "Int16",
    "Int32",
    "Int64",
    "Int8",
    "List",
    "Null",
    "Object",
    "Struct",
    "Time",
    "UInt16",
    "UInt32",
    "UInt64",
    "UInt8",
    "Unknown",
    "Utf8",
    # polars.datatypes: dtype groups
    "DATETIME_DTYPES",
    "DURATION_DTYPES",
    "FLOAT_DTYPES",
    "INTEGER_DTYPES",
    "NUMERIC_DTYPES",
    "TEMPORAL_DTYPES",
    # polars.type_aliases
    "PolarsDataType",
    # polars.io
    "read_avro",
    "read_csv",
    "read_csv_batched",
    "read_database",
    "read_database_uri",
    "read_delta",
    "read_excel",
    "read_ipc",
    "read_ipc_schema",
    "read_ipc_stream",
    "read_json",
    "read_ndjson",
    "read_ods",
    "read_parquet",
    "read_parquet_schema",
    "scan_csv",
    "scan_delta",
    "scan_ipc",
    "scan_ndjson",
    "scan_parquet",
    "scan_pyarrow_dataset",
    # polars.stringcache
    "StringCache",
    "enable_string_cache",
    "using_string_cache",
    # polars.config
    "Config",
    # polars.functions.whenthen
    "when",
    # polars.functions
    "align_frames",
    "arg_where",
    "concat",
    "date_range",
    "date_ranges",
    "datetime_range",
    "datetime_ranges",
    "element",
    "ones",
    "repeat",
    "time_range",
    "time_ranges",
    "zeros",
    # polars.functions.aggregation
    "all",
    "any",
    "cumsum",
    "max",
    "min",
    "sum",
    "all_horizontal",
    "any_horizontal",
    "cumsum_horizontal",
    "max_horizontal",
    "min_horizontal",
    "sum_horizontal",
    # polars.functions.lazy
    "apply",
    "approx_n_unique",
    "arange",
    "arctan2",
    "arctan2d",
    "arg_sort_by",
    "avg",
    "coalesce",
    "col",
    "collect_all",
    "collect_all_async",
    "concat_list",
    "concat_str",
    "corr",
    "count",
    "cov",
    "cumfold",
    "cumreduce",
    "date",  # named date_, see import above
    "datetime",  # named datetime_, see import above
    "duration",
    "exclude",
    "first",
    "fold",
    "format",
    "from_epoch",
    "groups",
    "head",
    "implode",
    "int_range",
    "int_ranges",
    "last",
    "lit",
    "map",
    "map_batches",
    "map_groups",
    "mean",
    "median",
    "n_unique",
    "quantile",
    "reduce",
    "rolling_corr",
    "rolling_cov",
    "select",
    "std",
    "struct",
    "tail",
    "time",  # named time_, see import above
    "var",
    # polars.functions.random
    "set_random_seed",
    # polars.convert
    "from_arrow",
    "from_dataframe",
    "from_dict",
    "from_dicts",
    "from_numpy",
    "from_pandas",
    "from_records",
    "from_repr",
    # polars.sql
    "SQLContext",
    # polars.utils
    "build_info",
    "get_index_type",
    "show_versions",
    "threadpool_size",
    # selectors
    "selectors",
    "sql_expr",
]

os.environ["POLARS_ALLOW_EXTENSION"] = "true"
