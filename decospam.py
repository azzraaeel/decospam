import requests

print("""

 .S_sSSs      sSSs    sSSs    sSSs_sSSs     .S_sSSs     .S       S.   sdSS_SSSSSSbs  
.SS~YS%%b    d%%SP   d%%SP   d%%SP~YS%%b   .SS~YS%%b   .SS       SS.  YSSS~S%SSSSSP  
S%S   `S%b  d%S'    d%S'    d%S'     `S%b  S%S   `S%b  S%S       S%S       S%S       
S%S    S%S  S%S     S%S     S%S       S%S  S%S    S%S  S%S       S%S       S%S       
S%S    S&S  S&S     S&S     S&S       S&S  S%S    S&S  S&S       S&S       S&S       
S&S    S&S  S&S_Ss  S&S     S&S       S&S  S&S    S&S  S&S       S&S       S&S       
S&S    S&S  S&S~SP  S&S     S&S       S&S  S&S    S&S  S&S       S&S       S&S       
S&S    S&S  S&S     S&S     S&S       S&S  S&S    S&S  S&S       S&S       S&S       
S*S    d*S  S*b     S*b     S*b       d*S  S*S    S*S  S*b       d*S       S*S       
S*S   .S*S  S*S.    S*S.    S*S.     .S*S  S*S    S*S  S*S.     .S*S       S*S       
S*S_sdSSS    SSSbs   SSSbs   SSSbs_sdSSS   S*S    S*S   SSSbs_sdSSS        S*S       
SSS~YSSY      YSSP    YSSP    YSSP~YSSY    S*S    SSS    YSSP~YSSY         S*S       
                                           SP                              SP        
                                           Y                               Y         
                                                                                     
                                                                                    """)
      
code = input("URL Code:")
url = "https://deco-my-tree-web.com/api/v1/message/" + (code)
name = input("Name:")
msg = input("Message:")
auth = input("Authorization Key:")
payload = {
    "name": name,
    "content": msg,
    "deco_index": 0,
    "only_for_user": False
}

headers = {
    "Content-Type": "application/json",
    "Authorization": auth,  
}

while True:
    response = requests.post(url, json=payload, headers=headers)

    # Check the status code of the response
    if response.status_code == 200:
        print("POST request successful!")
        print("Response content:", response.json())
    else:
        print(f"POST request failed with status code {response.status_code}")
        print("Response content:", response.text)
