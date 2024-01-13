import MeCab

FILE_NAME = r""

with open(FILE_NAME, "r", encoding="utf-8") as f:
    CONTENT = f.read()

try:
    tagger = MeCab.Tagger("-Owakati")
    parse = tagger.parse(CONTENT)
    node = tagger.parseToNode(parse).next #node != BOS
    
    mining = [['表層系', ',', '品詞', ',', '品詞細分類1', ',', '品詞細分類2', ',', '原形']]
    print(mining[0])
    while node.next: #node != EOS
        word = node.surface
        data = node.feature.split(',')
        delimiter = parse.split()

        if word != ',':
            if data[6] == None: 
                mining.append((word, ',', data[0], ',', data[1], ',', data[2], ',', " "))
                
            else:
                mining.append((word, ',', data[0], ',', data[1], ',', data[2], ',', data[6]))

        #pos = node.feature.split(",")[0]
        #print('{0} , {1}'.format(word, pos))

        #print(len(mining))
        #print(mining)

        print(len(mining)-1, '{0} , {1}'.format(word, data))
        node = node.next 
    #print(parse) 
    
    print(mining)
    print(type(mining))
    
    FILE_NAME = r"C:\Users\coff-\OneDrive\デスクトップ\Hack\real.csv"
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for result in mining:
            f.writelines(result)
            f.write('\n')

except RuntimeError as e:
    print(e.args)
    print(e.encoding)
    print(e.end)
    print(e.object)
    print(e.reason)
    print(e.start)
    print(e.with_traceback)

    

  
