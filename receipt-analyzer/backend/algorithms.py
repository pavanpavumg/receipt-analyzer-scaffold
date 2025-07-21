import re
from collections import Counter
from statistics import mean, median, mode
from datetime import datetime
import pandas as pd

def linear_search(records, keyword=None, field=None, pattern=None, range_=None):
    results = []
    for rec in records:
        if keyword and field and keyword.lower() in str(rec.get(field, '')).lower():
            results.append(rec)
        elif pattern and field and re.search(pattern, str(rec.get(field, ''))):
            results.append(rec)
        elif range_ and field:
            val = rec.get(field)
            if val is not None and range_[0] <= val <= range_[1]:
                results.append(rec)
    return results

def hash_search(records, field, value):
    index = {str(rec[field]).lower(): rec for rec in records if field in rec}
    return index.get(str(value).lower())

def sort_records(records, field, reverse=False):
    return sorted(records, key=lambda x: x.get(field, 0), reverse=reverse)

def aggregate_stats(records, field):
    values = [rec[field] for rec in records if field in rec and isinstance(rec[field], (int, float))]
    stats = {
        'sum': sum(values),
        'mean': mean(values) if values else 0,
        'median': median(values) if values else 0,
        'mode': mode(values) if values else None
    }
    return stats

def vendor_histogram(records):
    vendors = [rec['vendor'] for rec in records if 'vendor' in rec]
    return Counter(vendors)

def monthly_trend(records, date_field='date', amount_field='amount'):
    df = pd.DataFrame(records)
    if date_field in df and amount_field in df:
        df[date_field] = pd.to_datetime(df[date_field], errors='coerce')
        df = df.dropna(subset=[date_field])
        monthly = df.groupby(df[date_field].dt.to_period('M'))[amount_field].sum()
        return monthly
    return pd.Series()