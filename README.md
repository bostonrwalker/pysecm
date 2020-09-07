# pysecm
A lightweight Python framework for parsing common financial symbologies

Supported symbologies:
- RIC (Reuters Instrument Code)

Supported instruments:
- Equities (common, preferred)
- Fixed income (governments)
- Commodities (spot)
- FX (spot)
- Indices

Examples:
```
> from pysecm.ric import RIC
> RIC('AAPL.N')
AAPL.N [CommmonEquity]
```
```
> RIC('.VIX')
.VIX [Index]
```

```
> RIC('UST BILL 03-DEC-2020')
UST BILL 03-DEC-2020 [Government]
```
