text = "Задача: В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.\
Не учитывать знаки препинания и регистр символов.hi За основу возьмите любую статью из\
википедии или из документации к языку.\
Статья : Python — это язык программирования, который широко используется в интернет-приложениях,\
разработке программного обеспечения,но hi науке о данных и машинном обучении (ML). \
Разработчики используют Python, и потому что  он эффективен, прост в изучении и работает на разных платформах.\
Программы нj язык Python можно скачать скачать скачать скачать скачать бесплатно, но hi они\
 совместимы со всеми типами разработке систем и повышают скорость hi \
разработки.".lower()

for symbol in ".,;:":
    text = text.replace(symbol, " ")

words_list = text.split()
words_set = set(words_list)

word_dict = {}

for word in words_set:
    word_dict[word] = words_list.count(word)

sorted_tuple = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

# вернуть 10 самых частых
for i in range(10):
    print(f"Слово ({'), встречается в тексте->  '.join(str(item) for item in sorted_tuple[i])} раз(а)")
