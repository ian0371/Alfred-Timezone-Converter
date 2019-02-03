# Alfred Timezone Converter

### Prerequisites & Install
- pip
- Using pip, install the following requirements:
```bash
pip2 install --user -r requirements.txt
```

### Usage
```
tz [options ...]
```

`options` are set to current date and time if not given by user.

If `city` is given, times when the `city` is the date/time in `options` (or the current time if `options` is omitted) are shown.

#### Examples
- `tz 22:30 Seoul`: Shows the date/time of cities when Seoul is 22:30.
- `tz 03/01 22:30 Seoul`: Shows the date/time of cities when Seoul is 22:30, March 1st.

#### Options
- Date
  - `Day`: Two digits (ex) `01`: 1st day of the month
  - `Month/Day`: Two digits for `Month` and `Day`, respectively (ex) `03/01`: March 1st
- Time
  - `Hour:Minute`: Two digits for `Hour` (24hr format) and `Minute`, respectively (ex) `22:30`: Half past ten P.M., `00:01`: 12:01 A.M.
- City
  - `cityname`: Name of city. Case insensitive. (ex) `seoul`

Because the options are in distinguished format, *the order does not matter*.
That is, the followings behave the same way:
- `tz 22:30 03/01 Seoul`
- `tz Seoul 03/01 22:30`
- `tz 22:30 Seoul 03/01`

```
timezone add [city]
```

Add a city in database

```
timezone clear
```

Remove all cities in database

### License
This product includes GeoLite2 data created by MaxMind, available from
[https://www.maxmind.com](https://www.maxmind.com);
images of country flags, available from
[https://www.free-country-flags.com](https://www.free-country-flags.com).

