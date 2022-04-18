#!/bin/bash    
## Slack - API test with proxy
curl \
-H "X-SENDER: slack" \
-d "channel=Test summary" \
-d "color=green" \
-d "message=API Alert Test. " \
-d "nickname=alert" \
URI
