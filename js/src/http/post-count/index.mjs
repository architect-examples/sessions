import arc from '@architect/functions'

export const handler = arc.http(async req => {
  let count = (req.session.count || 0) + 1

  return {
    session: { count },
    location: '/'
  }
})
