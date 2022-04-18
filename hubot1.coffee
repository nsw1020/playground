module.exports = (robot) ->
  robot.hear /base64 encode( me)? (.*)/i, (res) ->
    if res.message.thread_ts?
      res.send "test"
    else
      res.message.thread_ts =res.message.rawMessage.ts
      res.send '```' + new Buffer(res.match[2]).toString('base64') + '```'
 
  robot.hear /base64 decode( me)? (.*)/i, (res) ->
    if res.message.thread_ts?
      res.send "test"
    else
      res.message.thread_ts =res.message.rawMessage.ts
      res.send '```' + new Buffer(res.match[2], 'base64').toString('utf8') + '```'
