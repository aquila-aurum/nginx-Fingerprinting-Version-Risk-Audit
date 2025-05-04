import shodan

API_KEY = "YOUR_API_KEY"
api = shodan.Shodan(API_KEY)

query = 'product:nginx http.title:"Welcome"'
results = api.search(query)

for result in results['matches']:
    ip = result['ip_str']
    version = result['product']
    print(f"[+] {ip} | Version: {version}")
