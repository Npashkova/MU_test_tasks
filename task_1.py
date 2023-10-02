import pandas as pd
import datapane as dp

from schemas import schema

# Convert json file to pandas data frame
jsonl_file = 'data/playstore.jsonl'
data_frame = pd.read_json(jsonl_file, lines=True, dtype=schema, encoding='utf8')


def check_url(df):
    """Checks if urls match pattern"""
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls_list = ['icon', 'icon_72', 'market_url', 'promo_video', 'promo_video_image',
                 'website', 'privacy_policy']
    for url in urls_list:
        urls = pd.Series(df[url])
        invalid_rows = urls[urls.str.match(url_pattern) == False]
        print(f'Data that does not match url pattern in {url}\n{invalid_rows}')


def check_email(df):
    """Checks if email matches pattern"""
    email_pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    email = pd.Series(df['email'])
    invalid_email = email[email.str.match(email_pattern) == False]
    print(f'Data that does not match email pattern \n{invalid_email}')


def check_date(df):
    """Checks if date matches pattern"""
    iso8601_date_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}$'
    date_list = ['market_update', 'created']
    for date in date_list:
        urls = pd.Series(df[date])
        invalid_rows = urls[urls.str.match(iso8601_date_pattern) == False]
        print(f'Data that does not match iso8601 date pattern in {date}\n{invalid_rows}')


def null_check(df):
    """Indicates null values in data frame"""
    null_counts = df.isnull().sum()
    return null_counts


def generate_report(df):
    """Generates html file with data from json file provided"""
    report = dp.App(dp.DataTable(df))
    report.save(path='report.html')


def missing_data_report(df):
    """Generates html file with number of empty values(nulls)"""
    df_is_null_sum = pd.DataFrame(null_check(df), columns=['nulls_number'])
    missing = dp.Report(df_is_null_sum)
    missing.save(path='missing.html')


if __name__ == '__main__':
    print(check_email(data_frame))
    print(check_url(data_frame))
    print(check_date(data_frame))
    generate_report(data_frame)
    missing_data_report(data_frame)
