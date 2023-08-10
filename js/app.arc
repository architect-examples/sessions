@app
sessions-example

@http
get /
post /count
post /reset

@tables
sessions
  _idx *
  ttl ttl
