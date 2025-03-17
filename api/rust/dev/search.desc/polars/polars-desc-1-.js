searchState.loadedDescShard("polars", 1, "Reduce memory consumption at the expense of performance\nWhether maintain the order of equal elements. Default <code>false</code>…\nWhether to maintain the order of equal elements. Default …\nCreates a new <code>Field</code> with metadata.\nSet the microsecond\nSet the microseconds\nSet the milliseconds\nSet the minute\nSet the minutes\nTreat missing fields as null.\nTreat missing fields as null.\nSet the month\nWhether sort in multiple threads. Default <code>true</code>.\nWhether to sort in multiple threads. Default <code>true</code>.\nConfigure the row limit.\nTry to stop parsing when <code>n</code> rows are parsed. During …\nTry to stop parsing when <code>n</code> rows are parsed. During …\nStop reading when <code>n</code> rows are read.\nStop reading when <code>n</code> rows are read.\nLimits the number of rows to read.\nNumber of threads to use for reading. Defaults to the size …\nReturn this <code>ChunkedArray</code> with a new name.\nReturns this <code>Field</code>, renamed.\nReturn this Series with a new name.\nSet the nanoseconds\nSet the CSV file’s null value representation.\nSet values that will be interpreted as missing/ null.\nSet values that will be interpreted as missing/null.\nWhether place null values last. Default <code>false</code>.\nWhether to place null values last. Default <code>false</code>.\nSpecify whether to place nulls last, per-column. Defaults …\nSet allowed optimizations.\nSpecify sorting order for the column. Default <code>false</code>.\nSort order for all columns. Default <code>false</code> which is …\nSpecify order for each column. Defaults all <code>false</code>.\nReverse the order of sorting.\nReverse the order of sorting for each column.\nSets the CSV parsing options. See map_parse_options for an …\nSet paths of the scanned files.\nToggle predicate pushdown optimization.\nSet the reader’s column projection. This counts from 0, …\nSet the reader’s column projection. This counts from 0, …\nSet the reader’s column projection: the names of the …\nSet the reader’s column projection. This counts from 0, …\nWhich columns to select denoted by their index. The index …\nToggle projection pushdown optimization.\nSet the <code>char</code> used as quote char. The default is <code>b&#39;&quot;&#39;</code>. If …\nSet the single byte character used for quoting.\nSet the character used for field quoting. This is most …\nSet the CSV file’s quoting behavior. See more on …\nRaise an error if CSV is empty (otherwise return an empty …\nWhether to raise an error if the frame is empty. By …\nRechunk the memory to contiguous chunks when parsing is …\nRechunk the memory to contiguous chunks when parsing is …\nRechunk the memory to contiguous chunks when parsing is …\nWhether to makes the columns contiguous in memory.\nTry to estimate the number of rows so that joins can …\nSet the row group size (in number of rows) during writing. …\nConfigure the row index.\nAdd a new column at index 0 that counts the rows.\nAdd a row index column.\nAdd a row index column.\nAdd a row index column.\nAdd a row index column.\nAdd a row index column.\nAdds a row index column.\nAdd a new column at index 0 that counts the rows.\nAdd a row index column in place.\nField with the same dtype.\nSet the CSV file’s schema\nSet the JSON file’s schema\nSet the JSON file’s schema\nSet the schema to use for CSV file. The length of the …\nModify a schema before we run the lazy scanning.\nSet the JSON file’s schema\nOverwrite parts of the inferred schema.\nOverwrites the data types in the schema by column name.\nSet the second\nSet the seconds\nSet the CSV file’s column separator as a byte character\nSet the CSV file’s column separator as a byte character.\nThe character used to separate fields in the CSV file. This\nToggle expression simplification optimization on or off.\nSkip the first <code>n</code> lines during parsing. The header will be …\nStart reading after <code>skip_lines</code> lines. The header will be …\nSkip the first <code>n</code> rows during parsing. The header will be …\nStart reading after <code>skip_rows</code> rows. The header will be …\nSkip this number of rows after the header location.\nNumber of rows to skip after the header row.\nOnly positive offsets are supported for simplicity - the …\nToggle slice pushdown optimization.\nSet the ‘sorted’ bit meta info.\nSet sources of the scanned files.\nCompute and write statistic\nSet the CSV file’s time format.\nTruncate lines that are longer than the schema.\nTruncate lines that are longer than the schema.\nAutomatically try to parse dates/datetimes and time. If …\nAutomatically try to parse dates/datetimes and time. If …\nToggle type check optimization.\nToggle type coercion optimization.\nReturns this array with a new validity.\nSet the weeks\nSet the year\nTurn off all optimizations.\nWrite a partitioned parquet dataset. This functionality is …\nBitwise “xor” operation.\nGet the bitwise XOR of the Series as a new Series of …\nGet the bitwise XOR of the Series as a new Series of …\nExtract month from underlying NaiveDate representation. …\nExtract month from underlying NaiveDate representation. …\nExtract month from underlying NaiveDateTime representation.\nExtract month from underlying NaiveDateTime representation.\nExtract year from underlying NaiveDateTime representation. …\nExtract year from underlying NaiveDateTime representation. …\nZip with a <code>ChunkedArray</code> then apply a binary function <code>F</code> …\nZip with a <code>ChunkedArray</code> then apply a binary function <code>F</code> …\nCombine the validities of two structs.\nCreate a new ChunkedArray with values from self where the …\nCreate a new ChunkedArray with values from self where the …\nLocal use cases often repeatedly collect the same <code>LazyFrame</code>…\nMaterialized at IR except for AnonymousScan.\nfunction to apply\nAlso has the input. i.e. avg(“foo”)\nfunction to apply\nfunction arguments\nfunction arguments\nlength is not yet known so we accept negative offsets\noutput dtype of the function\nA single value that’s used for all columns\nA different null value per column, computed from …\nAnalyzes a chunk of CSV data.\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nSplits datatypes that cannot be natively read into a …\nUtility to ensure the dtype of the column in <code>current_schema</code>…\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nHelper that combines the groups into a parallel iterator …\nSame helper as <code>_agg_helper_idx</code> but for aggregations that …\nSafety\nApplies a kernel that produces <code>Array</code> types.\nApply elementwise binary function which produces string, …\nApplies a kernel that produces <code>Array</code> types.\nApplies a kernel that produces <code>Array</code> types.\nApplies a kernel that produces <code>Array</code> types.\nApplies a kernel that produces <code>ArrayRef</code> of the same type.\nApplies a kernel that produces <code>Array</code> types.\nApplies a kernel that produces <code>ArrayRef</code> of the same type.\nApplies a kernel that produces <code>Array</code> types.\nApplies a kernel that produces <code>Array</code> types.\nApplies a kernel that produces <code>Array</code> types.\nApplies a kernel that produces <code>Array</code> types.\nSpecialized expressions for <code>Series</code> of <code>DataType::String</code>.\nCheck if a binary value contains a literal binary.\nCheck if a binary value ends with the given sequence.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nReturn the size (number of bytes) in each element.\nCheck if a binary value starts with the given sequence.\nStores the Utf8 fields and the total string length seen …\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nDynamic dispatch to async functions.\nByte source backed by a <code>MemSlice</code>, which can potentially be …\nSupports both cloud and local files.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nPanics\nNote: This will mutably sort ranges for coalescing.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nSpecialized expressions for Categorical dtypes.\nWhich side windows should be closed.\nExtract the days from a <code>Duration</code>\nOptional parameters for the rolling\nExtract hour from underlying NaiveDateTime representation. …\nExtract the hours from a <code>Duration</code>\nExtract the microseconds from a <code>Duration</code>\nExtract the milliseconds from a <code>Duration</code>\nAmount of elements in the window that should be filled …\nExtract minute from underlying NaiveDateTime …\nExtract the minutes from a <code>Duration</code>\nExtract second from underlying NaiveDateTime …\nExtract the nanoseconds from a <code>Duration</code>\nExtract second from underlying NaiveDateTime …\nExtract the seconds from a <code>Duration</code>\nThe length of the window.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nA location on cloud storage, may have wildcards.\nOptions to connect to various cloud providers.\nAdaptor which wraps the interface of ObjectStore::BufWriter…\nPolars wrapper around <code>ObjectStore</code> functionality. This …\nThe bucket name.\nBuild an <code>ObjectStore</code> based on the URL and passed in url. …\nExecutes the given command directly.\nThe path components that need to be expanded.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nParse a configuration from a Hashmap. This is the …\nFetch byte ranges into a HashMap keyed by the range start. …\nList files with a prefix derived from the pattern.\nFetch the metadata of the parquet file, do not memoize it.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nConstructs a new CloudWriter from a path and an optional …\nParse a CloudLocation from an url.\nConstruct a new CloudWriter, re-using the given …\nConstruct an object_store <code>Path</code> from a string without any …\nThe prefix inside the bucket, this will be the full key …\nQueues the given command for further execution.\nThe scheme (s3, …).\nPerforms a set of actions within a synchronous update.\nGets the underlying <code>ObjectStore</code> implementation.\nSet the maximum number of retries.\nWrapper that implements <code>IntoCredentialProvider</code>, <code>Debug</code>, …\nPrefer using <code>PlCredentialProvider::from_func</code> instead of …\nFor testing purposes\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nAccepts a function that returns (credential, expiry time …\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nOptions to connect to various cloud providers.\nRepresents the compression algorithms that we have …\nIf the given byte slice starts with the “magic” bytes …\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nDecompress <code>bytes</code> if compression is detected, otherwise …\nNote: The caller must ensure all columns in <code>args</code> have the …\nA nested list with a fixed size in each row\nThe set of supported logical types in this crate.\nThe time units defined in Arrow.\nOpaque binary data of variable length whose offsets are …\nA binary type that inlines small values and can intern …\nA binary true or false.\n<code>true</code> and <code>false</code>.\nA 32-bit date representing the elapsed time since UNIX …\nA 32-bit date representing the elapsed time since UNIX …\nAn <code>i32</code> representing the elapsed time since UNIX epoch …\nAn <code>i64</code> representing the elapsed time since UNIX epoch …\nA 64-bit date representing the elapsed time since UNIX …\nA 64-bit date representing the elapsed time since UNIX …\nA 64-bit date representing the elapsed time since UNIX …\nA 128-bit fixed point decimal number with a scale.\nFixed point decimal type optional precision and …\nDecimal value with precision and scale precision is the …\nDecimal backed by 256 bits\nA dictionary encoded array (<code>key_type</code>, <code>value_type</code>), where …\nA 64-bit integer representing difference between …\n64-bit integer representing difference between times in …\nMeasure of elapsed time. This elapsed time is a physical …\nExtension type.\nCharacterizes the name and the <code>DataType</code> of a column.\nOpaque binary data of fixed size. Enum parameter specifies …\nA list of some logical data type with a fixed number of …\nAn 16-bit float\nA 32-bit floating point number.\nA <code>f32</code>\nA 64-bit floating point number.\nA <code>f64</code>\nHashmap: maps the indexes from the global …\nA 128-bit integer number.\nAn <code>i128</code>\nA 16-bit integer number.\nAn <code>i16</code>\nA 32-bit integer number.\nAn <code>i32</code>\nA 64-bit integer number.\nAn <code>i64</code>\nAn 8-bit integer number.\nAn <code>i8</code>\nA “calendar” interval modeling elapsed time that takes …\nOpaque binary data of variable length whose offsets are …\nA list of some logical data type whose offsets are …\nA variable-length UTF-8 encoded string whose offsets are …\nNested type, contains arrays that are filled with one of …\nA nested list with a variable size in each row\nA list of some logical data type whose offsets are …\nUtf8Array: caches the string values and a hash of all …\nMaps a logical type to a chunked array implementation of …\nA nested type that is represented as\nTime in microseconds.\nTime in milliseconds.\nTime in nanoseconds.\nNull type\nCan be used to fmt and implements Any, so can be …\nA generic type that can be used in a <code>Series</code> &amp;’static str …\nThis hashmap uses an IdHasher\nString type that inlines small strings.\nSafety\nA dimension in a reshape.\nTime in seconds.\nA UTF8 encoded string type.\nString data\nAn UTF8 encoded string type.\nA nested <code>ArrowDataType</code> with a given number of <code>Field</code>s.\nA 64-bit time representing the elapsed time since midnight …\nA 64-bit time representing the elapsed time since midnight …\nA 32-bit time representing the elapsed time since midnight …\nA 64-bit time representing the elapsed time since midnight …\nA <code>i64</code> representing a timestamp measured in <code>TimeUnit</code> with …\nAn unsigned 16-bit integer number.\nAn <code>u16</code>\nAn unsigned 32-bit integer number.\nAn <code>u32</code>\nAn unsigned 64-bit integer number.\nAn <code>u64</code>\nAn unsigned 8-bit integer number.\nAn <code>u8</code>\nA nested datatype that can represent slots of differing …\nA type unknown to Arrow.\nA variable-length UTF-8 encoded string whose offsets are …\nA string type that inlines small values and can intern …\nGet data type of <code>ChunkedArray</code>.\nGets <code>AnyValue</code> from <code>LogicalType</code>\nSafety\nSafety\nSafety\nSafety\nHashmap: maps the indexes from the global …\nUtf8Array: caches the string values and a hash of all …\nHashmap: maps the indexes from the global …\nUtf8Array: caches the string values and a hash of all …\nEnable the global string cache as long as the object is …\nDisable and clear the global string cache.\nEnable the global string cache.\nCheck whether the global string cache is enabled.\nIf <code>ambiguous</code> is length-1 and not equal to “null”, we …\nSafety\nSafety\nSpecialized expressions for <code>Series</code> with dates/datetimes.\nGet the base offset from UTC.\nChange the underlying <code>TimeUnit</code>. And update the data …\nGet the century of a Date/Datetime\nCombine an existing Date/Datetime with a Time, creating a …\nChange the underlying <code>TimeZone</code> of the <code>Series</code>. This does …\nGet the (local) date of a Date/Datetime.\nGet the (local) datetime of a Datetime.\nGet the month of a Date/Datetime.\nGet the additional offset from UTC currently in effect …\nReturns the argument unchanged.\nGet the hour of a Datetime/Time64.\nCalls <code>U::from(self)</code>.\nGet the iso-year of a Date/Datetime. This may not …\nGet the microsecond of a Time64 (scaled from nanosecs).\nGet the millennium of a Date/Datetime\nGet the millisecond of a Time64 (scaled from nanosecs).\nGet the minute of a Datetime/Time64.\nGet the month of a Date/Datetime.\nGet the nanosecond part of a Time64.\nGet the ordinal_day of a Date/Datetime.\nExtract quarter from underlying NaiveDateTime …\nReplace the time units of a value\nRound the Datetime/Date range into buckets.\nGet the second of a Datetime/Time64.\nConvert from Date/Time/Datetime into String with the given …\nGet the (local) time of a Date/Datetime/Time.\nReturn the timestamp (UNIX epoch) of a Datetime/Date.\nConvert from Date/Time/Datetime into String with the given …\nExpress a Duration in terms of its total number of integer …\nExpress a Duration in terms of its total number of integer …\nExpress a Duration in terms of its total number of …\nExpress a Duration in terms of its total number of …\nExpress a Duration in terms of its total number of integer …\nExpress a Duration in terms of its total number of …\nExpress a Duration in terms of its total number of integer …\nTruncate the Datetime/Date range into buckets.\nExtract the week from the underlying Date representation. …\nExtract the ISO week day from the underlying Date …\nChange the underlying <code>TimeUnit</code> of the <code>Series</code>. This does …\nGet the year of a Date/Datetime\nOpen a path for writing. Supports cloud paths.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nSafety\nSafety\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nSafety\nSafety\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nReplace specific time component of a <code>DateChunked</code> with a …\nReplace specific time component of a <code>DatetimeChunked</code> with …\nGet the <code>RowEncodingContext</code> for a certain <code>DataType</code>.\nReturns the argument unchanged.\nInfer the data type of a record\nInfer the schema of a CSV file by reading through the …\nCalls <code>U::from(self)</code>.\nSearch through a series of chunks for the first position …\nUtility trait to slice concrete arrow arrays whilst …\nSlices this <code>Array</code>.\nSlices the <code>Array</code>.\nReturn the indices of the bottom k elements.\nUtility trait to slice concrete arrow arrays whilst …\nSort options for multi-series sorting.\nOptions for single series sorting.\nIf true sort in descending order. Default <code>false</code>.\nOrder of the columns. Default all `false``.\nLimit a sort output, this is for optimization purposes and …\nLimit a sort output, this is for optimization purposes and …\nIf true maintain the order of equal elements. Default <code>false</code>…\nWhether maintain the order of equal elements. Default <code>false</code>…\nIf true sort in multiple threads. Default <code>true</code>.\nWhether sort in multiple threads. Default <code>true</code>.\nWhether place null values last. Default <code>false</code>.\nWhether place null values last. Default <code>false</code>.\nSlices this <code>Array</code>.\nSlices the <code>Array</code>.\nConcat with the values from a second StringChunked.\nCheck if strings contain a regex pattern.\nCheck if strings contain a given literal\nCount all successive non-overlapping regex matches.\nCount all successive non-overlapping regex matches.\nExtract the nth capture group from pattern.\nExtract each successive non-overlapping regex match in an …\nExtract each successive non-overlapping regex match in an …\nExtract all capture groups from pattern and return as a …\nReturn the index position of a regular expression …\nReturn the index position of a literal substring in the …\nHorizontally concatenate all strings.\nReplace the leftmost regex-matched (sub)string with …\nReplace all regex-matched (sub)strings with another string\nReplace the leftmost literal (sub)string with another …\nReplace all matching literal (sub)strings with another …\nCheck if strings starts with a substring\nThis is more performant than the BinaryChunked version …\nEscapes all regular expression meta characters in the …\nSlice the first <code>n</code> values of the string.\nGet the length of the string values as number of bytes.\nGet the length of the string values as number of chars.\nReverses the string values\nSlice the string values.\nSlice the last <code>n</code> values of the string.\nModify the strings to their lowercase equivalent.\nModify the strings to their titlecase equivalent.\nModify the strings to their uppercase equivalent.\nRepresents a user-defined function\nThe function implementation.\nThe function signature.\nname\nOptions for the function.\nThe function output type.\nCompare <code>Series</code> and <code>ChunkedArray</code>’s and get a <code>boolean</code> mask …\nUsed to convert a <code>ChunkedArray</code>, <code>&amp;dyn SeriesTrait</code> and <code>Series</code>\nSeries\nGet a hold of the <code>ChunkedArray</code>, <code>Logical</code> or <code>NullChunked</code> as …\nGet a hold of the <code>ChunkedArray</code>, <code>Logical</code> or <code>NullChunked</code> as …\nGet the lengths of the underlying chunks\nUnderlying chunks.\nUnderlying chunks.\nClone inner ChunkedArray and wrap in a new Arc\nCheck for equality.\nCheck for equality where <code>None == None</code>.\nFilter by boolean mask. This operation clones data.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nGet a single value by index. Don’t use this operation …\nReturn if any the chunks in this <code>ChunkedArray</code> have nulls.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nGet a mask of the non-null values.\nGet a mask of the null values.\nGet length of series.\nName of series.\nCreate a new Series filled with values from the given …\nCheck for inequality.\nCheck for inequality where <code>None == None</code>.\nCount the null values.\nAggregate all chunks to a contiguous array of memory.\nRename the Series.\nreturn a Series in reversed order\nShift the values by a given period and fill the parts that …\nGet a zero copy view of the data.\nGet a zero copy view of the data.\nTake from <code>self</code> at the indexes given by <code>idx</code>.\nTake from <code>self</code> at the indexes given by <code>idx</code>.\nTake from <code>self</code> at the indexes given by <code>idx</code>.\nTake from <code>self</code> at the indexes given by <code>idx</code>.\nA <code>Series</code> that amortizes a few allocations during iteration.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nSwaps inner state with the <code>array</code>. Prefer …\nTemporary swaps out the array, and restores the original …\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nChecked integer division. Computes self / rhs, returning …\nChecked integer division. Computes self / rhs, returning …\ndrop nulls\nignore nulls\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.")