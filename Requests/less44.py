import requests


def download(q: str, p: str) -> None:
    header = {"Authorization": "s9OfGsrQyEZfjsPQuEbzwBquWUQHFLp5JjHbtrgR6AgzVmEMDxDnIyZY"}
    i = 1
    while i <= int(p):
        url =f"https://api.pexels.com/v1/search?query={q}&per_page=1&page={i}"
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            _r = r.json()
            # print(_r)
            for item in _r.get("photos"):
                print(item.get("url"))
        else:
            print(r.text) 
        i += 1       

def main() -> None:
    q = input("Query: ")
    p = input("Count pages: ")
    download(q, p)


main()    
