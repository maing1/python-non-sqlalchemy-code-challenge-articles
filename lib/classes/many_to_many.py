

class Article:
    _all = []  #store all instances of the Article class

    def __init__(self, author, magazine, title):
        # Make sure that the author is an instance of the Author class
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        # make sudre that the magazine is an instance of the Magazine class
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        # Make sure that the title is a string with a length between 5 and 50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._title = title  
        self.author = author  
        self.magazine = magazine  
        
        Article._all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")# make sure that the name is a non-empty string
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed after the author is instantiated.")# Ensure that the name cannot be changed after the instance is created
        
        self._name = name 

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article._all if article.author == self]  # so that it returns a list of articles written by this author

    def magazines(self):
        return list({article.magazine for article in self.articles()}) #Returns a unique list of magazines for which the author has contributed to


    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()}) # Return a list of unique categories of magazines this author has contributed to the magazine


class Magazine:
    _all = [] 

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.") # makes sure that the name is between 2 and 16 characters
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.") # makes sure that the category is a non-empty string
        
        self._name = name  
        self._category = category 
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.") # to make sure that the magazine's updated name has btwn 2 & 6 characters
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")# to make sure that the magazine's updaded category is a non-empty string
        self._category = value

    def articles(self):
        # Returns a list of all the articles the magazine has published and it must be a type of article
        return [article for article in Article._all if article.magazine == self]

    def contributors(self):
        # Return a list of unique authors who have written for this magazine & it must be a type of author
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Returns a list of the titles strings of all articles written for that magazine
        if not self.articles():
            return None #Returns None if the author has no articles
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Returns a list of authors who have written more than 2 articles for the magazine
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None #Returns None if the magazine has no authors with more than 2 publications

    @classmethod
    def top_publisher(cls):
        # Returns the Magazine instance with the most articles
        if not Article._all:
            return None #Returns None if there are no articles.
        return max(cls._all, key=lambda mag: len(mag.articles()))
   