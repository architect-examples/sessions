@app
sessions-example

@aws
runtime python

@http
get /
post /count
post /reset

@tables
sessions
  _idx *
  ttl ttl
