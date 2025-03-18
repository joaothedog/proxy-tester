import requests

def test_proxy(proxy):
    try:
        response = requests.get(
            "http://example.com",
            proxies={"http": proxy, "https": proxy},
            timeout=10
        )
        if response.status_code == 200:
            return True
    except:
        return False
    return False

def load_proxies(file_path):
    with open(file_path, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

def main():
    proxies = load_proxies("proxies.txt")
    if not proxies:
        print("Nenhum proxy encontrado no arquivo proxies.txt.")
        return

    working_proxies = []
    for proxy in proxies:
        print(f"Testando proxy: {proxy}...")
        if test_proxy(proxy):
            print(f"Proxy {proxy} está funcionando!")
            working_proxies.append(proxy)
        else:
            print(f"Proxy {proxy} falhou.")

    with open("working_proxies.txt", 'w') as file:
        for proxy in working_proxies:
            file.write(proxy + "\n")

    print(f"Proxies funcionais salvos em 'working_proxies.txt'. Total: {len(working_proxies)}")

if __name__ == "__main__":
    main()