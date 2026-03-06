books = [['Python',500],['Black Box',900],['C#',300]]
books.sort()
print(books)
books.sort(key=lambda item:item[1])
print("sort by price:",books)
min_price = min(books, key=lambda item:item[1])
print("min:",min_price)
max_price = max(books, key=lambda item:item[1])
print("max:",max_price)

filtered = list(filter(lambda item: item[1]>500, books))
print("List:",filtered)

mapped = list(map(lambda item: [123, item[0].title(),item[1]],books))
print("Map:",mapped)

colors_data = [{'Name':'Red','Rating':65},
                {'Name':'Black','Rating':90},
                {'Name':'Blue','Rating':50},
                {'Name':'Green','Rating':15}]

sort_by_rating = sorted(colors_data, key=lambda item: item['Rating'])
sort_by_rating.reverse()
print("sorted by rating:",sort_by_rating)

filteredc = list(filter(lambda item: item['Rating']>60, colors_data))
print("rating filter (above 60):",filteredc)

most_fav = max(colors_data, key=lambda item: item['Rating'])
print("most rated:",most_fav)

least_fav = min(colors_data, key=lambda item: item['Rating'])
print("least rated:",least_fav)
