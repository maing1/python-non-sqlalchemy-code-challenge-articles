class Article:
    _all = []  # Tracks all Article instances

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if hasattr(self, "_title"):  # Ensure title is immutable
            raise AttributeError("Title cannot be modified after initialization.")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article._all.append(self)

    @property
    def title(self):
        return self._title


        
class Author:
    def __init__(self, name):
        self._name = name
    
    def name(self):
        return self._name
    
    def author_name(self,name):
        if not isinstance(name, str) or len(name) > 0:
            raise ValueError("Name must be a non-empty string.")
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed after the author is instantiated.")
        self._name = name

    def articles(self):
        return [article for article in Article._all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self,magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()})

class Magazine:
    _all = []  # To keep track of all magazine instances

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) > 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article._all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article._all:
            return None
        return max(cls._all, key=lambda mag: len(mag.articles()))


