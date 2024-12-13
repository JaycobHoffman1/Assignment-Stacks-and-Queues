# Task 1
# Design a Stack-based structure to represent your browsing history where you have the ability to: 
# Add a new page (add to the Stack)
# Remove a page (Remove from the Stack)
# Check to see how many pages you have viewed in your browsing session
# Check to see if you current browsing session is empty.

class BrowsingHistoryStack():
    def __init__(self):
        self.browsing_history = []

    def is_empty(self):
        return len(self.browsing_history) == 0

    def add_page(self, page):
        self.browsing_history.append(page)

        print("Page added!")

    def remove_page(self):
        if not self.is_empty():
            removed_page = self.browsing_history.pop()

            print("Page removed!")

            return removed_page
        
        print("Browsing history is empty!")

    def get_viewed_pages(self):
        viewed_pages = len(self.browsing_history)

        print(f"You have viewed {viewed_pages} pages!")

        return viewed_pages
    
browsing_history = BrowsingHistoryStack()

browsing_history.add_page("Funny Cat Videos")
browsing_history.add_page("Try Not To Laugh Memes")
browsing_history.add_page("Migos - Walk It Talk It")
browsing_history.remove_page()
browsing_history.get_viewed_pages()