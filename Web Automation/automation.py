import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' # ADD Chrome Path
    URLS = (
        "github.com/ganeshbhandarkar",
        "codechef.com/users/gbgb1bgbg",
        "codeforces.com/"
    )
    for url in URLS:
        wb.get(chrome_path).open(url)

webauto()