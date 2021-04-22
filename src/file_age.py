import datetime


def parse_file_age(value):
    if not value:
        return datetime.timedelta(seconds=0)
    if isinstance(value, int):
        return datetime.timedelta(seconds=value)
    if isinstance(value, str) or isinstance(value, unicode):
        intval = int(''.join([c for c in value if c >= '0' and c <= '9']))
        value = value.lower()
        if 's' in value:
            return datetime.timedelta(seconds=intval)
        elif 'm' in value:
            return datetime.timedelta(minutes=intval)
        elif 'h' in value:
            return datetime.timedelta(hours=intval)
        elif 'd' in value:
            return datetime.timedelta(days=intval)
    if isinstance(value, datetime.timedelta):
        return value
    raise ValueError("Invalid file age description:", value)


def is_aged_file(filedate, max_file_age):
    max_file_age = parse_file_age(max_file_age)
    filedate = datetime.datetime.fromtimestamp(filedate)
    return datetime.datetime.now()-filedate > max_file_age
