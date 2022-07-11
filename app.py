import pandas as pd

dataFile = './BX-CSV-Dump/BX-Book-Ratings.csv'
data = pd.read_csv(dataFile, encoding= 'unicode_escape', sep=";", header=0, names=["user", "isbn", "rating"])

# print(data.head())

bookFile = './BX-CSV-Dump/BX-Books.csv'
books = pd.read_csv(bookFile, encoding= 'unicode_escape', sep=";", header=0, error_bad_lines=False, usecols=[0,1,2], index_col=0, names=["isbn", "title", "author"])

print(books.head())

def bookMeta(isbn):
  title = books.at[isbn, "title"]
  author = books.at[isbn, "author"]
  return title, author

# print(bookMeta("0671027360"))

def faveBooks(user, N):
  userRatings = data[data["user"]==user]
  sortedRatings = pd.DataFrame.sort_values(userRatings,['rating'], ascending=[0])[:N]
  sortedRatings["title"] = sortedRatings["isbn"].apply(bookMeta)
  return sortedRatings

data = data[data["isbn"].isin(books.index)]

print(faveBooks(204622, 5))