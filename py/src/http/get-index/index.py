import arc


def handler(req, context):
    session = arc.http.session_read(req)
    count = session.get("count", 0)
    return arc.http.res(
        req,
        {
            "html": "<!doctype html>\n"
            "<html>\n"
            "  <body>\n"
            "    <form method=post action=/count>\n"
            "      <button>Count {0}</button>\n"
            "    </form>\n"
            "    <form method=post action=/reset>\n"
            "      <button>Reset</button>\n"
            "    </form>\n"
            "  </body>\n"
            "</html>".format(count)
        },
    )
