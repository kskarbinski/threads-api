from os import path, mkdir

from whoosh.fields import Schema, TEXT
from whoosh.index import create_in
from whoosh.query import Term

from app_data.users import users


schema = Schema(username=TEXT(stored=True))

if not path.exists("../../../index"):
    mkdir("../../../index")

index = create_in("../../../index", schema)

writer = index.writer()
for user in users:
    writer.update_document(username=user["username"])
writer.commit()

# TODO: Only searches by exact match. Figure out how to search by partial words
with index.searcher() as searcher:
    result = searcher.search(Term("username", u"test_username"))

    print result
    print result[0]
