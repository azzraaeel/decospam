# DecoSpam Python Script

This Python script facilitates a POST request to the DecomYTree site.

## Usage

Follow these steps to use the script and obtain your authorization token:

1. Open the target site and access the message sending interface.
2. Press `F12` to open the browser developer tools.
   
   ![Step 2](screenshot.png)

3. Navigate to the `Network` tab and monitor network activity.
4. Send a test message; you will observe something similar to the following:

   ![Step 4](screenshot2.png)

5. This screenshot illustrates how to obtain your authorization token.
   
   ```python
   # Enter your auth token in the script
   auth_token = "your_auth_token_here"
