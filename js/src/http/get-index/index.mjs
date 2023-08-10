import arc from '@architect/functions'

export const handler = arc.http(async req => {
  let count = req.session.count || 0
  return {
    html: `
<!doctype html>
<html>
  <body>
    <form method=post action=/count>
      <button>Count ${ count }</button>
    </form>
    <form method=post action=/reset>
      <button>Reset</button>
    </form>
  </body>
</html>
`
  }
})
