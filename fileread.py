            filepath = os.path.join(workingDir, args[1])
            f = open(filepath, "r")
            contents = f.read()
            i = 0
            while (i < len(contents)):
                print(contents[i])
                i+= 1
