
with open('cook_book.txt', encoding='utf-8') as f:
      cook_book = dict()
      new_list = ['ingredient_name', 'quantity', 'measure']
      for line in f:
              title = line.strip()
              counter = int(f.readline().strip())
              list = []
              for i in range(counter):
                   line =f.readline().strip().split('|')
                   kk = zip(new_list, line)
                   list += kk
                   cook_book[title] = list
              f.readline()
for i in cook_book.items():
      print(i)


