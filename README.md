# Reaper SelfBot
---
### How to get your token?
In order to get your token to put into `.env` you need to run the following command in your Revolt console:
```js
const c = controllers.client.getReadyClient()
console.log(c.session.token)
```
Then simply put the output into the `TOKEN` field in `.env`
