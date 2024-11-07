import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[
        (users["mail"].str.endswith("@leetcode.com"))
        & (users["mail"].str.split("@").str[0].str[0].str.isalpha())
        & (users["mail"].str.match(r"^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$"))
    ]
