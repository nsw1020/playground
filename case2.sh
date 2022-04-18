#!/bin/bash    
curl -X POST 'URI' \
-H 'Content-Type: application/json' \
-d '{
    "username": "app",
    "icon_emoji": ":happy:",
    "attachments": [
        {
            "color": "#2eb886",
            "blocks": [
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Status:*\n:android: Fail alert"
                        }
                    ]
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Report Link"
                            },
                            "style": "primary",
                            "value": "link",
                            "url": "https://www.google.com"
                        }
                    ]
                }
            ]
        }
    ]
}'
