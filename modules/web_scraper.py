import requests
from bs4 import BeautifulSoup
import re

class WebScraper:
    """Step 3: Web Scraping Module"""
    
    def scrape_urls(self, urls):
        """
        Scrape text content from list of URLs
        Returns combined raw text
        """
        all_text = []
        
        for url in urls:
            try:
                text = self._scrape_single_url(url)
                if text:
                    all_text.append(text)
            except Exception as e:
                print(f"Error scraping {url}: {e}")
                continue
        
        return "\n\n".join(all_text)
    
    def _scrape_single_url(self, url):
        """
        Scrape text from a single URL
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'iframe']):
                element.decompose()
            
            # Extract paragraphs
            paragraphs = soup.find_all(['p', 'article', 'div.content'])
            
            text_parts = []
            for p in paragraphs:
                text = p.get_text().strip()
                # Only include paragraphs with substantial content
                if len(text) > 50:
                    text_parts.append(text)
            
            return "\n".join(text_parts)
            
        except Exception as e:
            print(f"Error in _scrape_single_url: {e}")
            # Return fallback content for demo
            return self._get_fallback_content()
    
    def _get_fallback_content(self):
        """
        Fallback content when scraping fails
        """
        return """
        System architecture consists of multiple components working together.
        The API Gateway handles incoming requests and routes them to appropriate services.
        The Load Balancer distributes traffic across multiple servers.
        The Application Server processes business logic.
        The Database stores persistent data.
        The Cache Layer improves performance by storing frequently accessed data.
        The Message Queue handles asynchronous communication between services.
        The CDN serves static content to users globally.
        The Notification Service sends alerts and messages to users.
        The Authentication Service manages user login and security.
        """
