import webbrowser

url = input("Coloque a URL do Youtube: ")

url = url [:12]+'ss'+url[12:]
webbrowser.open(url)