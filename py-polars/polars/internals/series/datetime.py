from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import TYPE_CHECKING

import polars.internals as pli
from polars.internals.series.utils import expr_dispatch
from polars.utils import _to_python_datetime

if TYPE_CHECKING:
    from polars.internals.type_aliases import EpochTimeUnit, TimeUnit
    from polars.polars import PySeries


@expr_dispatch
class DateTimeNameSpace:
    """Series.dt namespace."""

    _accessor = "dt"

    def __init__(self, series: pli.Series):
        self._s: PySeries = series._s

    def __getitem__(self, item: int) -> date | datetime:
        s = pli.wrap_s(self._s)
        return s[item]

    def min(self) -> date | datetime | timedelta:
        """
        Return minimum as python DateTime.

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2001, 1, 1), datetime(2001, 1, 3), "1d")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.min()
        datetime.datetime(2001, 1, 1, 0, 0)

        """
        # we can ignore types because we are certain we get a logical type
        return pli.wrap_s(self._s).min()  # type: ignore[return-value]

    def max(self) -> date | datetime | timedelta:
        """
        Return maximum as python DateTime.

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2001, 1, 1), datetime(2001, 1, 3), "1d")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.max()
        datetime.datetime(2001, 1, 3, 0, 0)

        """
        return pli.wrap_s(self._s).max()  # type: ignore[return-value]

    def median(self) -> date | datetime | timedelta:
        """
        Return median as python DateTime.

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2001, 1, 1), datetime(2001, 1, 3), "1d")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.median()
        datetime.datetime(2001, 1, 2, 0, 0)

        """
        s = pli.wrap_s(self._s)
        out = int(s.median())
        return _to_python_datetime(out, s.dtype, s.time_unit)

    def mean(self) -> date | datetime:
        """
        Return mean as python DateTime.

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2001, 1, 1), datetime(2001, 1, 3), "1d")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.mean()
        datetime.datetime(2001, 1, 2, 0, 0)

        """
        s = pli.wrap_s(self._s)
        out = int(s.mean())
        return _to_python_datetime(out, s.dtype, s.time_unit)

    def strftime(self, fmt: str) -> pli.Series:
        """
        Format Date/datetime with a formatting rule.

        See `chrono strftime/strptime
        <https://docs.rs/chrono/0.4.19/chrono/format/strftime/index.html>`_.

        Returns
        -------
        Utf8 Series

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 4)
        >>> date = pl.date_range(start, stop, interval="1d")
        shape: (4,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
                2001-01-04 00:00:00
        ]
        >>> date.dt.strftime(fmt="%Y-%m-%d")
        shape: (4,)
        Series: 'date' [str]
        [
                "2001-01-01"
                "2001-01-02"
                "2001-01-03"
                "2001-01-04"
        ]

        """

    def year(self) -> pli.Series:
        """
        Extract the year from the underlying date representation.

        Can be performed on Date and Datetime.

        Returns the year number in the calendar date.

        Returns
        -------
        Year as Int32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2002, 1, 1)
        >>> date = pl.date_range(start, stop, interval="1y")
        shape: (2,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2002-01-01 00:00:00
        ]
        >>> date.dt.year()
        shape: (2,)
        Series: '' [i32]
        [
                2001
                2002
        ]

        """

    def quarter(self) -> pli.Series:
        """
        Extract quarter from underlying Date representation.

        Can be performed on Date and Datetime.

        Returns the quarter ranging from 1 to 4.

        Returns
        -------
        Quarter as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 4, 1)
        >>> date = pl.date_range(start, stop, interval="1mo")
        shape: (4,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-02-01 00:00:00
                2001-03-01 00:00:00
                2001-04-01 00:00:00
        ]
        >>> date.dt.quarter()
        shape: (4,)
        Series: '' [u32]
        [
                1
                1
                1
                2
        ]

        """

    def month(self) -> pli.Series:
        """
        Extract the month from the underlying date representation.

        Can be performed on Date and Datetime

        Returns the month number starting from 1.
        The return value ranges from 1 to 12.

        Returns
        -------
        Month as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 4, 1)
        >>> date = pl.date_range(start, stop, interval="1mo")
        shape: (4,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-02-01 00:00:00
                2001-03-01 00:00:00
                2001-04-01 00:00:00
        ]

        >>> date.dt.month()
        shape: (4,)
        Series: '' [u32]
        [
                1
                2
                3
                4
        ]

        """

    def week(self) -> pli.Series:
        """
        Extract the week from the underlying date representation.

        Can be performed on Date and Datetime

        Returns the ISO week number starting from 1.
        The return value ranges from 1 to 53. (The last week of year differs by years.)

        Returns
        -------
        Week number as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 4, 1)
        >>> date = pl.date_range(start, stop, interval="1mo")
        shape: (4,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-02-01 00:00:00
                2001-03-01 00:00:00
                2001-04-01 00:00:00
        ]
        >>> date.dt.week()
        shape: (4,)
        Series: '' [u32]
        [
                1
                5
                9
                13
        ]

        """

    def weekday(self) -> pli.Series:
        """
        Extract the week day from the underlying date representation.

        Can be performed on Date and Datetime.

        Returns the weekday number where monday = 0 and sunday = 6

        Returns
        -------
        Week day as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 7)
        >>> date = pl.date_range(start, stop, interval="1d")
        shape: (7,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
                2001-01-04 00:00:00
                2001-01-05 00:00:00
                2001-01-06 00:00:00
                2001-01-07 00:00:00
        ]
        >>> date.dt.weekday()
        shape: (7,)
        Series: '' [u32]
        [
                0
                1
                2
                3
                4
                5
                6
        ]

        """

    def day(self) -> pli.Series:
        """
        Extract the day from the underlying date representation.

        Can be performed on Date and Datetime.

        Returns the day of month starting from 1.
        The return value ranges from 1 to 31. (The last day of month differs by months.)

        Returns
        -------
        Day as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 9)
        >>> date = pl.date_range(start, stop, interval="2d")
        shape: (5,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-03 00:00:00
                2001-01-05 00:00:00
                2001-01-07 00:00:00
                2001-01-09 00:00:00
        ]
        >>> date.dt.day()
        shape: (5,)
        Series: '' [u32]
        [
                1
                3
                5
                7
                9
        ]

        """

    def ordinal_day(self) -> pli.Series:
        """
        Extract ordinal day from underlying date representation.

        Can be performed on Date and Datetime.

        Returns the day of year starting from 1.
        The return value ranges from 1 to 366. (The last day of year differs by years.)

        Returns
        -------
        Day as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 3, 1)
        >>> date = pl.date_range(start, stop, interval="1mo")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-02-01 00:00:00
                2001-03-01 00:00:00
        ]
        >>> date.dt.ordinal_day()
        shape: (3,)
        Series: '' [u32]
        [
                1
                32
                60
        ]

        """

    def hour(self) -> pli.Series:
        """
        Extract the hour from the underlying DateTime representation.

        Can be performed on Datetime.

        Returns the hour number from 0 to 23.

        Returns
        -------
        Hour as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 1, 3)
        >>> date = pl.date_range(start, stop, interval="1h")
        shape: (4,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-01 01:00:00
                2001-01-01 02:00:00
                2001-01-01 03:00:00
        ]
        >>> date.dt.hour()
        shape: (4,)
        Series: '' [u32]
        [
                0
                1
                2
                3
        ]

        """

    def minute(self) -> pli.Series:
        """
        Extract the minutes from the underlying DateTime representation.

        Can be performed on Datetime.

        Returns the minute number from 0 to 59.

        Returns
        -------
        Minute as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 1, 0, 4, 0)
        >>> date = pl.date_range(start, stop, interval="2m")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-01 00:02:00
                2001-01-01 00:04:00
        ]
        >>> date.dt.minute()
        shape: (3,)
        Series: 'date' [u32]
        [
                0
                2
                4
        ]

        """

    def second(self) -> pli.Series:
        """
        Extract the seconds the from underlying DateTime representation.

        Can be performed on Datetime.

        Returns the second number from 0 to 59.

        Returns
        -------
        Second as UInt32

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 1, 0, 0, 4)
        >>> date = pl.date_range(start, stop, interval="2s")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-01 00:00:02
                2001-01-01 00:00:04
        ]
        >>> date.dt.second()
        shape: (3,)
        Series: 'date' [u32]
        [
                0
                2
                4
        ]

        """

    def nanosecond(self) -> pli.Series:
        """
        Extract the nanoseconds from the underlying DateTime representation.

        Can be performed on Datetime.

        Returns the number of nanoseconds since the whole non-leap second.
        The range from 1,000,000,000 to 1,999,999,999 represents the leap second.

        Returns
        -------
        Nanosecond as UInt32

        Examples
        --------
        >>> date = pl.date_range(
        ...     start, start + timedelta(milliseconds=1), interval="1ns"
        ... )[:3]
        shape: (3,)
        Series: '' [datetime[ns]]
        [
                2001-01-01 00:00:00
                2001-01-01 00:00:00.000000001
                2001-01-01 00:00:00.000000002
        ]
        >>> date.dt.nanosecond()
        shape: (3,)
        Series: '' [u32]
        [
                0
                1
                2
        ]

        """

    def timestamp(self, tu: TimeUnit = "us") -> pli.Series:
        """
        Return a timestamp in the given time unit.

        Parameters
        ----------
        tu : {'us', 'ns', 'ms'}
            Time unit.

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 3)
        >>> date = pl.date_range(start, stop, interval="1d")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.timestamp()
        shape: (3,)
        Series: '' [i64]
        [
                978307200000000
                978393600000000
                978480000000000
        ]
        >>> date.dt.timestamp(tu="ms")
         shape: (3,)
         Series: '' [i64]
         [
                978307200000
                978393600000
                978480000000
         ]

        """

    def epoch(self, tu: EpochTimeUnit = "us") -> pli.Series:
        """
        Get the time passed since the Unix EPOCH in the give time unit.

        Parameters
        ----------
        tu : {'us', 'ns', 'ms', 's', 'd'}
            Time unit.

        Examples
        --------
        >>> from datetime import datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 3)
        >>> date = pl.date_range(start, stop, interval="1d")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.epoch()
        shape: (3,)
        Series: '' [i64]
        [
                978307200000000
                978393600000000
                978480000000000
        ]
        >>> date.dt.epoch(tu="s")
        shape: (3,)
        Series: '' [i64]
        [
                978307200
                978393600
                978480000
        ]

        """

    def with_time_unit(self, tu: TimeUnit) -> pli.Series:
        """
        Set time unit a Series of dtype Datetime or Duration.

        This does not modify underlying data, and should be used to fix an incorrect
        time unit.

        Parameters
        ----------
        tu : {'ns', 'us', 'ms'}
            Time unit for the ``Datetime`` Series.

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(
        ...     datetime(2001, 1, 1), datetime(2001, 1, 3), "1d", time_unit="ns"
        ... )
        shape: (3,)
        Series: '' [datetime[ns]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.with_time_unit(tu="us")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                +32971-04-28 00:00:00
                +32974-01-22 00:00:00
                +32976-10-18 00:00:00
        ]

        """

    def cast_time_unit(self, tu: TimeUnit) -> pli.Series:
        """
        Cast the underlying data to another time unit. This may lose precision.

        Parameters
        ----------
        tu : {'ns', 'us', 'ms'}
            Time unit for the ``Datetime`` Series.

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2001, 1, 1), datetime(2001, 1, 3), "1d")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.cast_time_unit(tu="ms")
        shape: (3,)
        Series: 'tu_ms' [datetime[ms]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]
        >>> date.dt.cast_time_unit(tu="ns")
        shape: (3,)
        Series: '' [datetime[ns]]
        [
                2001-01-01 00:00:00
                2001-01-02 00:00:00
                2001-01-03 00:00:00
        ]

        """

    def with_time_zone(self, tz: str | None) -> pli.Series:
        """
        Set time zone a Series of type Datetime.

        Parameters
        ----------
        tz
            Time zone for the `Datetime` Series.

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2020, 3, 1), datetime(2020, 5, 1), "1mo")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2020-03-01 00:00:00
                2020-04-01 00:00:00
                2020-05-01 00:00:00
        ]
        >>> date.dt.with_time_zone(tz="Europe/London")
        shape: (3,)
        Series: '' [datetime[μs, Europe/London]]
        [
                2020-03-01 00:00:00 GMT
                2020-04-01 00:00:00 BST
                2020-05-01 00:00:00 BST
        ]

        """

    def days(self) -> pli.Series:
        """
        Extract the days from a Duration type.

        Returns
        -------
        A series of dtype Int64

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2020, 3, 1), datetime(2020, 5, 1), "1mo")
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2020-03-01 00:00:00
                2020-04-01 00:00:00
                2020-05-01 00:00:00
        ]
        >>> date.diff().dt.days()
        shape: (3,)
        Series: '' [i64]
        [
                null
                31
                30
        ]

        """

    def hours(self) -> pli.Series:
        """
        Extract the hours from a Duration type.

        Returns
        -------
        A series of dtype Int64

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2020, 1, 1), datetime(2020, 1, 4), "1d")
        shape: (4,)
        Series: '' [datetime[μs]]
        [
                2020-01-01 00:00:00
                2020-01-02 00:00:00
                2020-01-03 00:00:00
                2020-01-04 00:00:00
        ]
        >>> date.diff().dt.hours()
        shape: (4,)
        Series: '' [i64]
        [
                null
                24
                24
                24
        ]

        """

    def minutes(self) -> pli.Series:
        """
        Extract the minutes from a Duration type.

        Returns
        -------
        A series of dtype Int64

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(datetime(2020, 1, 1), datetime(2020, 1, 4), "1d")
        shape: (4,)
        Series: '' [datetime[μs]]
        [
                2020-01-01 00:00:00
                2020-01-02 00:00:00
                2020-01-03 00:00:00
                2020-01-04 00:00:00
        ]
        >>> date.diff().dt.minutes()
        shape: (4,)
        Series: '' [i64]
        [
                null
                1440
                1440
                1440
        ]

        """

    def seconds(self) -> pli.Series:
        """
        Extract the seconds from a Duration type.

        Returns
        -------
        A series of dtype Int64

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(
        ...     datetime(2020, 1, 1), datetime(2020, 1, 1, 0, 4, 0), "1m"
        ... )
        shape: (5,)
        Series: '' [datetime[μs]]
        [
                2020-01-01 00:00:00
                2020-01-01 00:01:00
                2020-01-01 00:02:00
                2020-01-01 00:03:00
                2020-01-01 00:04:00
        ]
        >>> date.diff().dt.seconds()
        shape: (5,)
        Series: '' [i64]
        [
                null
                60
                60
                60
                60
        ]

        """

    def milliseconds(self) -> pli.Series:
        """
        Extract the milliseconds from a Duration type.

        Returns
        -------
        A series of dtype Int64

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(
        ...     datetime(2020, 1, 1), datetime(2020, 1, 1, 0, 0, 1, 0), "1ms"
        ... )[:3]
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2020-01-01 00:00:00
                2020-01-01 00:00:00.001
                2020-01-01 00:00:00.002
        ]
        >>> date.diff().dt.milliseconds()
        shape: (3,)
        Series: '' [i64]
        [
                null
                1
                1
        ]

        """

    def microseconds(self) -> pli.Series:
        """
        Extract the microseconds from a Duration type.

        Returns
        -------
        A series of dtype Int64

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(
        ...     datetime(2020, 1, 1), datetime(2020, 1, 1, 0, 0, 1, 0), "1ms"
        ... )[:3]
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2020-01-01 00:00:00
                2020-01-01 00:00:00.001
                2020-01-01 00:00:00.002
        ]
        >>> date.diff().dt.microseconds()
        shape: (3,)
        Series: '' [i64]
        [
                null
                1000
                1000
        ]

        """

    def nanoseconds(self) -> pli.Series:
        """
        Extract the nanoseconds from a Duration type.

        Returns
        -------
        A series of dtype Int64

        Examples
        --------
        >>> from datetime import datetime
        >>> date = pl.date_range(
        ...     datetime(2020, 1, 1), datetime(2020, 1, 1, 0, 0, 1, 0), "1ms"
        ... )[:3]
        shape: (3,)
        Series: '' [datetime[μs]]
        [
                2020-01-01 00:00:00
                2020-01-01 00:00:00.001
                2020-01-01 00:00:00.002
        ]
        >>> date.diff().dt.nanoseconds()
        shape: (3,)
        Series: '' [i64]
        [
                null
                1000000
                1000000
        ]

        """

    def offset_by(self, by: str) -> pli.Series:
        """
        Offset this date by a relative time offset.

        This differs from ``pl.col("foo") + timedelta`` in that it can
        take months and leap years into account. Note that only a single minus
        sign is allowed in the ``by`` string, as the first character.

        Parameters
        ----------
        by
            The offset is dictated by the following string language:

            - 1ns   (1 nanosecond)
            - 1us   (1 microsecond)
            - 1ms   (1 millisecond)
            - 1s    (1 second)
            - 1m    (1 minute)
            - 1h    (1 hour)
            - 1d    (1 day)
            - 1w    (1 week)
            - 1mo   (1 calendar month)
            - 1y    (1 calendar year)
            - 1i    (1 index count)

        Returns
        -------
        Date/Datetime expression

        Examples
        --------
        >>> from datetime import datetime
        >>> dates = pl.date_range(datetime(2000, 1, 1), datetime(2005, 1, 1), "1y")
        shape: (6,)
        Series: '' [datetime[μs]]
        [
                2000-01-01 00:00:00
                2001-01-01 00:00:00
                2002-01-01 00:00:00
                2003-01-01 00:00:00
                2004-01-01 00:00:00
                2005-01-01 00:00:00
        ]
        >>> dates.dt.offset_by("1y").alias("date_plus_1y")
        shape: (6,)
        Series: 'date_plus_1y' [datetime[μs]]
        [
                2001-01-01 00:00:00
                2002-01-01 00:00:00
                2003-01-01 00:00:00
                2004-01-01 00:00:00
                2005-01-01 00:00:00
                2006-01-01 00:00:00
        ]
        >>> dates.dt.offset_by("-1y2mo").alias("date_minus_1y_2mon")
        shape: (6,)
        Series: 'date_minus_1y_2mon' [datetime[μs]]
        [
                1998-11-01 00:00:00
                1999-11-01 00:00:00
                2000-11-01 00:00:00
                2001-11-01 00:00:00
                2002-11-01 00:00:00
                2003-11-01 00:00:00
        ]

        """

    def truncate(
        self,
        every: str | timedelta,
        offset: str | timedelta | None = None,
    ) -> pli.Series:
        """
        Divide the date/ datetime range into buckets.

        The `every` and `offset` argument are created with the
        the following string language:

        1ns # 1 nanosecond
        1us # 1 microsecond
        1ms # 1 millisecond
        1s  # 1 second
        1m  # 1 minute
        1h  # 1 hour
        1d  # 1 day
        1w  # 1 week
        1mo # 1 calendar month
        1y  # 1 calendar year

        3d12h4m25s # 3 days, 12 hours, 4 minutes, and 25 seconds

        Parameters
        ----------
        every
            Every interval start and period length
        offset
            Offset the window

        Returns
        -------
        Date/Datetime series

        Warnings
        --------
        This functionality is experimental and may change without it being considered a
        breaking change.

        Examples
        --------
        >>> from datetime import timedelta, datetime
        >>> start = datetime(2001, 1, 1)
        >>> stop = datetime(2001, 1, 2)
        >>> s = pl.date_range(start, stop, timedelta(minutes=30), name="dates")
        >>> s
        shape: (49,)
        Series: 'dates' [datetime[μs]]
        [
            2001-01-01 00:00:00
            2001-01-01 00:30:00
            2001-01-01 01:00:00
            2001-01-01 01:30:00
            2001-01-01 02:00:00
            2001-01-01 02:30:00
            2001-01-01 03:00:00
            2001-01-01 03:30:00
            2001-01-01 04:00:00
            2001-01-01 04:30:00
            2001-01-01 05:00:00
            2001-01-01 05:30:00
            ...
            2001-01-01 18:30:00
            2001-01-01 19:00:00
            2001-01-01 19:30:00
            2001-01-01 20:00:00
            2001-01-01 20:30:00
            2001-01-01 21:00:00
            2001-01-01 21:30:00
            2001-01-01 22:00:00
            2001-01-01 22:30:00
            2001-01-01 23:00:00
            2001-01-01 23:30:00
            2001-01-02 00:00:00
        ]
        >>> s.dt.truncate("1h")
        shape: (49,)
        Series: 'dates' [datetime[μs]]
        [
            2001-01-01 00:00:00
            2001-01-01 00:00:00
            2001-01-01 01:00:00
            2001-01-01 01:00:00
            2001-01-01 02:00:00
            2001-01-01 02:00:00
            2001-01-01 03:00:00
            2001-01-01 03:00:00
            2001-01-01 04:00:00
            2001-01-01 04:00:00
            2001-01-01 05:00:00
            2001-01-01 05:00:00
            ...
            2001-01-01 18:00:00
            2001-01-01 19:00:00
            2001-01-01 19:00:00
            2001-01-01 20:00:00
            2001-01-01 20:00:00
            2001-01-01 21:00:00
            2001-01-01 21:00:00
            2001-01-01 22:00:00
            2001-01-01 22:00:00
            2001-01-01 23:00:00
            2001-01-01 23:00:00
            2001-01-02 00:00:00
        ]
        >>> assert s.dt.truncate("1h") == s.dt.truncate(timedelta(hours=1))

        """
