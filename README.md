# smpp_send_sms
Test program for sending a sms using smpp and SMSC Simulator

## Dependencies
Install dependencies with:

```python
pip install -r requirements.txt
```

> for system wide installation use **sudo**

## Settings
The settings for the test server can be found and modified in the file *settings.py*:
```python
SMS_SYSTEM_HOSTNAME = "smscsim.melroselabs.com"
SMS_SYSTEM_PORT = 2775
SMS_SYSTEM_ID = "7298786"
SMS_SYSTEM_PASSWORD = "XWFLST"
```
in this case those are the settings for the test server found [here](https://melroselabs.com/services/smsc-simulator/#smsc-simulator-try)

## Running the program
Run the following command:

```bash
$ python send_sms.py
```