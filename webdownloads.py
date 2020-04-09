            url = args[1]
            filepath = args[2]
            filename, headers = urllib.request.urlretrieve(url, filename = filepath)
            
# example using python3
