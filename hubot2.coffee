module.exports = (robot) ->
  robot.respond /URL encode( me)? (.*)/i, (res) ->
    if res.message.thread_ts?
      res.send encodeURIComponent(res.match[2])
    else
      res.message.thread_ts = res.message.rawMessage.ts
      res.send encodeURIComponent(res.match[2])
 
  robot.respond /URL decode( me)? (.*)/i, (res) ->
    if res.message.thread_ts?
      res.send decodeURIComponent(res.match[2])
    else
      res.message.thread_ts = res.message.rawMessage.ts
      res.send decodeURIComponent(res.match[2])
 
  robot.respond /URL form encode( me)? (.*)/i, (res) ->
    if res.message.thread_ts?
      res.send urlFormEncode(res.match[2])
    else
      res.message.thread_ts = res.message.rawMessage.ts
      res.send urlFormEncode(res.match[2])
 
  robot.respond /URL form decode( me)? (.*)/i, (res) ->
    if res.message.thread_ts?
      res.send urlFormDecode(res.match[2])
    else
      res.message.thread_ts = res.message.rawMessage.ts
      res.send urlFormDecode(res.match[2])
 
urlFormEncode = (str) ->
  escape(str)
    .replace(new RegExp('\\+','g'),'%2B')
    .replace(new RegExp('%20','g'),'+')
