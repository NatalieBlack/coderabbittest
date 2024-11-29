from database import database

database.articles.create_index(
    [
        ("client_id", 1),
        ("should_suggest", 1),
        ("locale", 1),
        ("updated_source", -1),
    ],
    background=True,
)