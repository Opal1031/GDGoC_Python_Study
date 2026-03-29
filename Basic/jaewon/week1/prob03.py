play = True

sentence = [ ]

while play:
    line = input("")

    if line == "#":
        play = False
    else:
        sentence.append(line)

for sentences in sentence:
    a = sentences.count("a")
    b = sentences.count("i")
    c = sentences.count("u")
    d = sentences.count("e")
    e = sentences.count("o")
    print(a+b+c+d+e)
