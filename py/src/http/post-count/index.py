import arc


def handler(req, context):
    session = arc.http.session_read(req)
    count = session.get("count", 0) + 1
    return arc.http.res(req, {"session": {"count": count}, "location": "/"})
