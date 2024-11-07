import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return (
        views.loc[views["author_id"] == views["viewer_id"], ["author_id"]]
        .drop_duplicates()
        .sort_values(by="author_id", ascending=True)
        .rename(columns={"author_id": "id"})
    )
