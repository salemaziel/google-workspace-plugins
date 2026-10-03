# Google Chat Cards v2 Formatting Reference

Reference for sending structured Cards v2 messages via `gws chat +send` or `gws chat spaces messages create`.

## Cards v2 Payload Structure

```json
{
  "cardsV2": [
    {
      "cardId": "unique-card-id",
      "card": {
        "header": {
          "title": "Incident Alert: Production API",
          "subtitle": "Severity P0 • Triggered at 14:02 UTC",
          "imageUrl": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/warning/default/48px.svg",
          "imageType": "CIRCLE"
        },
        "sections": [
          {
            "header": "Incident Details",
            "widgets": [
              {
                "decoratedText": {
                  "topLabel": "Service",
                  "text": "Auth & Token Gateway"
                }
              },
              {
                "decoratedText": {
                  "topLabel": "Impact",
                  "text": "Elevated 500 error rates (~14% of traffic)"
                }
              },
              {
                "buttonList": {
                  "buttons": [
                    {
                      "text": "View Dashboard",
                      "onClick": {
                        "openLink": {
                          "url": "https://monitoring.example.com"
                        }
                      }
                    }
                  ]
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Basic Text Formatting
When sending plain text (`text: "..."`), Google Chat supports:
- `*bold*` -> **bold**
- `_italic_` -> *italic*
- `~strikethrough~` -> ~~strikethrough~~
- `` `inline code` `` -> `inline code`
- ```` ```multiline code``` ```` -> code block
- `<https://example.com|link text>` -> clickable hyperlink
- `<users/all>` -> `@all` mention
