## Creating a Client

Before working with Telegram's API, you need to get your own API ID and hash:

1. Follow this link and login with your phone number.
2. Click on "API Development tools".
3. A "Create new application" window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
4. Click on "Create application" at the end. Remember that your API hash is secret and Telegram won't let you revoke it. Don't post it anywhere!



## Configuring .env File

1. Create a new file in the root directory of your project and name it `.env`.
2. Open the `.env` file and add your configuration variables in the following format: `KEY=VALUE`. For example:

    ```plaintext
    api_id=your-api-id
    api_hash=your-api-hash
    channel_username=AppleP12
    session_name=user

## Installing

```
pip install -r requirement.txt
```

