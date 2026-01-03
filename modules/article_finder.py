import requests
from bs4 import BeautifulSoup
import re

class ArticleFinder:
    """Step 2: Article Finder Module"""
    
    # Hardcoded high-quality system design resources
    KNOWN_RESOURCES = {
        "uber": [
            "https://www.geeksforgeeks.org/system-design-of-uber-app-uber-system-architecture/",
            "https://medium.com/@narengowda/uber-system-design-8b2bc95e2cfe"
        ],
        "amazon": [
            "https://www.geeksforgeeks.org/amazon-system-design-interview-questions/",
            "https://medium.com/@sandeep4.verma/system-design-amazon-e-commerce-93380c2c6662"
        ],
        "netflix": [
            "https://www.geeksforgeeks.org/system-design-netflix-a-complete-architecture/",
            "https://medium.com/swlh/system-design-netflix-9f2b8a8feee7"
        ],
        "whatsapp": [
            "https://www.geeksforgeeks.org/design-whatsapp-a-system-design-interview-question/",
            "https://medium.com/@narengowda/system-design-for-whatsapp-or-messenger-e5c445f44155"
        ],
        "instagram": [
            "https://www.geeksforgeeks.org/system-design-of-instagram/",
            "https://medium.com/@narengowda/system-design-instagram-c68e2cce6239"
        ],
        "twitter": [
            "https://www.geeksforgeeks.org/design-twitter-a-system-design-interview-question/",
            "https://medium.com/@narengowda/system-design-for-twitter-e737284afc95"
        ],
        "youtube": [
            "https://www.geeksforgeeks.org/system-design-of-youtube/",
            "https://medium.com/@narengowda/youtube-system-design-2c5d4b2f5cd1"
        ],
        "dns": [
            "https://www.geeksforgeeks.org/domain-name-system-dns-in-application-layer/",
            "https://medium.com/@anuupadhyay/system-design-dns-architecture-80b9a0d4baf9"
        ]
    }
    
    def find_articles(self, topic, design_type):
        """
        Find relevant articles for the given topic
        Returns list of URLs
        """
        # Use hardcoded resources if available
        if topic.lower() in self.KNOWN_RESOURCES:
            return self.KNOWN_RESOURCES[topic.lower()][:3]
        
        # Fallback: construct search query
        query = f"{topic} system design {design_type} architecture"
        
        # For demo purposes, return some generic URLs
        # In production, you'd use Google Custom Search API or similar
        return [
            f"https://www.geeksforgeeks.org/{topic.lower()}-system-design/",
            f"https://medium.com/@narengowda/{topic.lower()}-system-design"
        ]
    
    def _search_google(self, query):
        """
        Simple Google search scraper (for educational purposes)
        In production, use official APIs
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            response = requests.get(url, headers=headers, timeout=5)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            links = []
            
            for a in soup.find_all('a', href=True):
                href = a['href']
                if '/url?q=' in href:
                    link = href.split('/url?q=')[1].split('&')[0]
                    if link.startswith('http') and 'google' not in link:
                        links.append(link)
                        if len(links) >= 3:
                            break
            
            return links
        except:
            return []
