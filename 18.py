from abc import ABC, abstractmethod
class Chapter:
	def __init__(self):
		self.title=title
		self.pages=pages
	def show(self):
		print("chapter = ",self.title," pages = ",self.pages)
class Book:
	def __init__(self, name: str):
		self.name = name 
		self.chapters=[]
	def add_chapter(self, chapter: Chapter):
		self.chapters.append(chapter)
	def show_details(self):
		print(f"Book: {self.name}")
		print("Chapters:")
		for chap in self.chapters:
			chap.show()
if __name__=="__main__"
#menu driven program