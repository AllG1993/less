import ParserClass

parser = ParserClass.Parser('https://www.ua-football.com/sport', 'news.txt')
parser.run()
print(parser.results)