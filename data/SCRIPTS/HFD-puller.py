#!/usr/bin/env python3
"""
HFD News Scraper - Fire News Only
Scrapes news from Honolulu Fire Department website and keeps only fire-related reports
"""

import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
from typing import List, Dict
import time

class HPDFireNewsScraper:
    def __init__(self):
        self.base_url = "https://fire.honolulu.gov/"
        self.news_url = f"{self.base_url}news-and-info/news-releases/"
        self.session = requests.Session()
        
        # Enhanced headers to avoid 403 errors
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        })
        
        # Fire-related keywords to filter FOR (expanded list)
        self.fire_keywords = [
            # Basic fire terms
            'fire', 'fires', 'burning', 'burn', 'burned', 'burnt',
            'blaze', 'flames', 'flame', 'smoke', 'smoking', 'smoky',
            'arson', 'wildfire', 'brush fire', 'grass fire',
            
            # Structure fires
            'structure fire', 'house fire', 'home fire', 'building fire',
            'apartment fire', 'condo fire', 'residential fire',
            'commercial fire', 'vehicle fire', 'car fire', 'truck fire',
            
            # Fire department related
            'fire department', 'hfd', 'honolulu fire department',
            'firefighter', 'firefighters', 'fire crew', 'fire personnel',
            'fire truck', 'fire engine', 'fire apparatus', 'fire station',
            'fire company', 'ladder truck', 'rescue truck',
            
            # Fire safety and equipment
            'fire alarm', 'fire suppression', 'fire safety', 'fire prevention',
            'fire extinguisher', 'sprinkler system', 'fire drill',
            'fire escape', 'fire exit', 'fire code', 'fire marshal',
            
            # Fire processes
            'combustion', 'ignition', 'ignite', 'ignited', 'flammable',
            'inflammable', 'fuel', 'accelerant', 'ember', 'embers',
            'ash', 'ashes', 'soot', 'char', 'charred',
            
            # Fire incidents
            'fire call', 'fire response', 'fire scene', 'fire damage',
            'fire investigation', 'fire cause', 'fire origin',
            'fire suppression', 'fire containment', 'fire control',
            
            # Emergency response to fires
            'responded to fire', 'fire reported', 'fire emergency',
            'fire incident', 'fire hazard', 'fire risk'
        ]
    
    def get_news_page(self, page_num: int = 1) -> BeautifulSoup:
        """Fetch and parse a news page with enhanced error handling"""
        try:
            url = f"{self.news_url}?page={page_num}" if page_num > 1 else self.news_url
            
            # Add delay to avoid being flagged as bot
            time.sleep(2)
            
            # Try multiple approaches to get clean content
            approaches = [
                # Approach 1: Standard request with proper headers
                {
                    'headers': {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1'
                    }
                },
                # Approach 2: Disable compression
                {
                    'headers': {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Connection': 'keep-alive'
                    }
                },
                # Approach 3: Mobile user agent
                {
                    'headers': {
                        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5'
                    }
                }
            ]
            
            for i, approach in enumerate(approaches, 1):
                try:
                    print(f"Trying approach {i} for page {page_num}...")
                    
                    response = requests.get(url, headers=approach['headers'], timeout=15)
                    response.raise_for_status()
                    
                    # Check if content looks like HTML
                    content_type = response.headers.get('content-type', '')
                    if 'text/html' not in content_type.lower():
                        print(f"Warning: Content type is {content_type}")
                    
                    # Try to decode content properly
                    try:
                        # Let requests handle encoding automatically
                        html_content = response.text
                        
                        # Check if we got valid HTML
                        if '<html' in html_content.lower() or '<head' in html_content.lower():
                            print(f"✓ Successfully got HTML content with approach {i}")
                            return BeautifulSoup(html_content, 'html.parser')
                        else:
                            print(f"Content doesn't look like HTML, trying next approach...")
                            continue
                            
                    except UnicodeDecodeError:
                        print(f"Unicode decode error with approach {i}, trying next...")
                        continue
                        
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 403:
                        print(f"403 Forbidden with approach {i}")
                        continue
                    else:
                        print(f"HTTP Error {e.response.status_code} with approach {i}")
                        continue
                except Exception as e:
                    print(f"Error with approach {i}: {e}")
                    continue
            
            # If all approaches failed, try a basic request
            print("All approaches failed, trying basic request...")
            try:
                response = requests.get(url, timeout=15)
                response.raise_for_status()
                
                # Force UTF-8 encoding
                response.encoding = 'utf-8'
                return BeautifulSoup(response.text, 'html.parser')
                
            except Exception as e:
                print(f"Basic request also failed: {e}")
                return None
            
        except Exception as e:
            print(f"Unexpected error fetching page {page_num}: {e}")
            return None
    
    def extract_news_items(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract news items from the parsed HTML"""
        news_items = []
        
        # Based on actual HPD website structure - WordPress format
        # Look for article elements and other containers
        selectors = [
            'article',
            '.post',
            '.entry',
            '.news-item',
            '.wp-block-post',
            '.post-content'
        ]
        
        # Try different selectors
        for selector in selectors:
            items = soup.select(selector)
            if items:
                print(f"Found {len(items)} items using selector: {selector}")
                for item in items:
                    news_item = self.parse_news_item(item)
                    if news_item:
                        news_items.append(news_item)
                break
        
        # If no articles found, try to extract from links and text blocks
        if not news_items:
            print("No articles found, trying link extraction...")
            news_items = self.extract_from_links(soup)
        
        return news_items
    
    def extract_from_links(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract news from links when article structure isn't available"""
        news_items = []
        
        # Look for links that appear to be news articles
        links = soup.find_all('a', href=True)
        
        for link in links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # Skip if it's not a news article link
            if not href or not text:
                continue
                
            # Skip navigation, social media, and other non-news links
            skip_patterns = [
                'facebook.com', 'twitter.com', 'instagram.com', 'youtube.com',
                'mailto:', 'tel:', '#', 'javascript:', 'wp-content/uploads',
                '/wp-admin/', '/wp-login/', '.jpg', '.png', '.gif', '.pdf'
            ]
            
            if any(pattern in href.lower() for pattern in skip_patterns):
                continue
            
            # Look for article-like URLs
            if any(pattern in href.lower() for pattern in ['news', 'press', 'release', 'story', 'article']):
                # Make sure it's a full URL
                if href.startswith('/'):
                    href = self.base_url + href
                
                # Try to get more context from surrounding elements
                parent = link.parent
                context = ""
                if parent:
                    context = parent.get_text(strip=True)
                
                news_item = {
                    'title': text,
                    'link': href,
                    'date': None,
                    'content': context[:200] + "..." if len(context) > 200 else context
                }
                
                news_items.append(news_item)
        
        return news_items
    
    def parse_news_item(self, item) -> Dict:
        """Parse individual news item"""
        try:
            # Extract title - look for various title elements
            title_elem = item.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) or item.find(['a'])
            title = title_elem.get_text(strip=True) if title_elem else "No title"
            
            # Extract link
            link_elem = item.find('a', href=True)
            if not link_elem and hasattr(item, 'get') and item.get('href'):
                link_elem = item
            
            link = link_elem.get('href') if link_elem else None
            if link and link.startswith('/'):
                link = self.base_url + link
            
            # Extract date - look for time elements or date patterns
            date_elem = item.find(['time', '.date', '.published', '.created'])
            date = None
            if date_elem:
                date = date_elem.get_text(strip=True)
            else:
                # Try to find date in text content
                text_content = item.get_text()
                import re
                date_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}'
                date_match = re.search(date_pattern, text_content)
                if date_match:
                    date = date_match.group(0)
            
            # Extract content/summary
            content = ""
            # Remove title text from content
            full_text = item.get_text(strip=True)
            if title in full_text:
                content = full_text.replace(title, "", 1).strip()
            else:
                content = full_text
            
            # Clean up content
            content = content[:500] + "..." if len(content) > 500 else content
            
            return {
                'title': title,
                'link': link,
                'date': date,
                'content': content,
                'full_text': full_text
            }
        except Exception as e:
            print(f"Error parsing news item: {e}")
            return None
    
    def contains_fire_keywords(self, text: str) -> bool:
        """Check if text contains fire-related keywords"""
        if not text:
            return False
            
        text_lower = text.lower()
        
        # Check for fire keywords
        for keyword in self.fire_keywords:
            if keyword.lower() in text_lower:
                return True
        
        # Additional pattern matching for fire-related content
        fire_patterns = [
            r'\bfire\b',  # Word boundary for "fire"
            r'\bburn\w*\b',  # burn, burning, burned, etc.
            r'\bflame\w*\b',  # flame, flames, etc.
            r'\bsmoke\w*\b',  # smoke, smoking, smoky, etc.
            r'\bhfd\b',  # Honolulu Fire Department
            r'fire\s+department',  # fire department
            r'fire\s+truck',  # fire truck
            r'fire\s+engine',  # fire engine
        ]
        
        import re
        for pattern in fire_patterns:
            if re.search(pattern, text_lower):
                return True
        
        return False
    
    def filter_for_fire_news(self, news_items: List[Dict]) -> List[Dict]:
        """Filter to keep ONLY fire-related news items"""
        fire_items = []
        
        for item in news_items:
            # Safely get text content for filtering
            title_text = item.get('title', '') or ''
            content_text = item.get('content', '') or ''
            full_text = item.get('full_text', '') or ''
            
            # Check all text fields for fire keywords
            is_fire_related = (
                self.contains_fire_keywords(title_text) or 
                self.contains_fire_keywords(content_text) or 
                self.contains_fire_keywords(full_text)
            )
            
            if is_fire_related:
                print(f"🔥 KEEPING fire-related news: {title_text[:60]}...")
                # Remove full_text from final output (used only for filtering)
                filtered_item = {k: v for k, v in item.items() if k != 'full_text'}
                fire_items.append(filtered_item)
            else:
                print(f"❌ SKIPPING non-fire news: {title_text[:60]}...")
        
        return fire_items

    def save_to_json(self, news_items: List[Dict], filename: str = "HFD_Fire_News.json"):
    #Save news items to JSON file with timestamp in filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        full_filename = f"{filename}_{timestamp}.json"
        with open(full_filename, "w", encoding="utf-8") as f:
            json.dump(news_items, f, ensure_ascii=False, indent=4)
        
        output_data = {
            "scrape_timestamp": timestamp,
            "scrape_date": datetime.now().strftime("%Y-%m-%d"),
            "filter_type": "fire_news_only",
            "total_items": len(news_items),
            "news_items": news_items
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            print(f"✓ Saved {len(news_items)} fire-related news items to {filename}")
            print(f"✓ Scrape timestamp: {timestamp}")
        except Exception as e:
            print(f"Error saving to JSON: {e}")
    
    def scrape_fire_news(self, max_pages: int = 3) -> List[Dict]:
        """Main scraping function - returns only fire-related news"""
        print("Starting HPD fire news scraping...")
        print("=" * 50)
        
        all_news = []
        
        for page in range(1, max_pages + 1):
            print(f"Scraping page {page}...")
            
            soup = self.get_news_page(page)
            if not soup:
                print(f"Failed to fetch page {page}")
                continue
            
            # Debug: Print some of the HTML structure
            print(f"Page {page} HTML preview:")
            print(soup.get_text()[:200] + "..." if len(soup.get_text()) > 200 else soup.get_text())
            print("-" * 30)
            
            news_items = self.extract_news_items(soup)
            if not news_items:
                print(f"No news items found on page {page}")
                # Debug: Try to find any links at all
                all_links = soup.find_all('a', href=True)
                news_links = [link for link in all_links if link.get('href', '').startswith('/') and link.get_text(strip=True)]
                print(f"Found {len(news_links)} potential news links")
                
                if news_links:
                    print("Sample links found:")
                    for link in news_links[:5]:
                        print(f"  - {link.get_text(strip=True)[:50]}... -> {link.get('href')}")
                continue
            
            print(f"Found {len(news_items)} items on page {page}")
            all_news.extend(news_items)
            
            # Be respectful with requests
            time.sleep(2)
        
        print(f"\nTotal items scraped: {len(all_news)}")
        
        if not all_news:
            print("No news items found. This might be due to:")
            print("- Changes in website structure")
            print("- Content loaded dynamically with JavaScript")
            print("- Different URL structure than expected")
            print("\nTrying alternative extraction method...")
            
            # Try one more time with the first page using a more aggressive approach
            soup = self.get_news_page(1)
            if soup:
                all_news = self.extract_aggressive(soup)
        
        # Filter FOR fire-related news with detailed logging
        print("\n" + "=" * 30)
        print("FIRE FILTERING PROCESS")
        print("=" * 30)
        print(f"Total items before filtering: {len(all_news)}")
        
        fire_news = self.filter_for_fire_news(all_news)
        
        print(f"\nTotal fire-related items found: {len(fire_news)}")
        print(f"Items skipped (non-fire): {len(all_news) - len(fire_news)}")
        print("=" * 30)
        
        # Save to JSON
        self.save_to_json(fire_news)
        
        return fire_news
    
    def extract_aggressive(self, soup: BeautifulSoup) -> List[Dict]:
        """More aggressive extraction method for difficult sites"""
        news_items = []
        
        # Look for any links that might be news articles
        links = soup.find_all('a', href=True)
        
        for link in links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # Skip empty or very short text
            if not text or len(text) < 10:
                continue
                
            # Skip common non-news links
            skip_terms = [
                'login', 'admin', 'wp-content', 'facebook', 'twitter', 
                'instagram', 'youtube', 'mailto', 'tel:', '#top', 
                'privacy', 'terms', 'contact', 'about'
            ]
            
            if any(term in href.lower() for term in skip_terms):
                continue
            
            # Look for article-like characteristics
            if (href.startswith('/') and 
                len(text) > 15 and 
                not href.endswith('.jpg') and 
                not href.endswith('.png') and
                not href.endswith('.pdf')):
                
                # Make full URL
                full_url = self.base_url + href if href.startswith('/') else href
                
                # Try to extract date from surrounding content
                parent = link.parent
                date_text = parent.get_text() if parent else ""
                
                news_item = {
                    'title': text,
                    'link': full_url,
                    'date': None,
                    'content': date_text[:200] + "..." if len(date_text) > 200 else date_text,
                    'full_text': text + " " + date_text
                }
                
                news_items.append(news_item)
        
        print(f"Aggressive extraction found {len(news_items)} potential news items")
        return news_items

def create_manual_fire_news_template():
    """Create a template with fire-related news examples"""
    template = {
        "scrape_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scrape_date": datetime.now().strftime("%Y-%m-%d"),
        "source": "Manual entry - HPD website fire news",
        "filter_type": "fire_news_only",
        "total_items": 0,
        "news_items": [
            {
                "title": "HPD Assists HFD in Structure Fire Response",
                "link": "https://www.honolulupd.org/example-fire-response/",
                "date": "July 2025",
                "content": "Honolulu Police Department officers assisted the Honolulu Fire Department in responding to a structure fire in the Kalihi area..."
            },
            {
                "title": "Brush Fire Causes Traffic Delays on H-1",
                "link": "https://www.honolulupd.org/brush-fire-traffic/",
                "date": "July 2025",
                "content": "A brush fire near the H-1 freeway required police traffic control and caused significant delays during rush hour..."
            },
            {
                "title": "Arson Investigation Leads to Arrest",
                "link": "https://www.honolulupd.org/arson-arrest/",
                "date": "July 2025",
                "content": "HPD detectives arrested a suspect in connection with a series of suspicious fires in the Waikiki area..."
            }
        ]
    }
    
    # These are already fire-related, so no need to filter
    template["total_items"] = len(template["news_items"])
    
    # Save template
    with open("HPD_Fire_News_Manual_Template.json", 'w', encoding='utf-8') as f:
        json.dump(template, f, indent=2, ensure_ascii=False)
    
    print("✓ Created manual fire news template: HPD_Fire_News_Manual_Template.json")
    print("✓ This contains sample fire-related news items")
    print("✓ Update this file manually with current fire news items")
    
    return template

def main():
    """Main function to run the fire news scraper"""
    scraper = HPDFireNewsScraper()
    
    try:
        print("HPD Fire News Scraper - Fire Stories Only")
        print("=" * 50)
        print("This scraper will find and keep ONLY fire-related news stories")
        print("=" * 50)
        
        # Test connection first
        print("Testing connection...")
        soup = scraper.get_news_page(1)
        if not soup:
            print("\n⚠️  Unable to connect to HPD website")
            print("This may be due to:")
            print("- Website blocking automated requests")
            print("- Temporary server issues")
            print("- Network connectivity problems")
            
            # Offer to create manual template
            create_template = input("\nWould you like to create a manual fire news template? (y/n): ")
            if create_template.lower() == 'y':
                create_manual_fire_news_template()
            return
        
        print("✓ Connection successful!")
        
        # Scrape fire news only
        fire_news = scraper.scrape_fire_news(max_pages=3)
        
        # Display summary
        print("\n" + "=" * 50)
        print("FIRE NEWS SCRAPING COMPLETE")
        print("=" * 50)
        print(f"Fire-related news items found: {len(fire_news)}")
        
        # Show fire news items
        if fire_news:
            print("\nFire-related news items:")
            for i, item in enumerate(fire_news, 1):
                print(f"{i}. {item['title']}")
                if item['date']:
                    print(f"   Date: {item['date']}")
                if item['link']:
                    print(f"   Link: {item['link']}")
                print()
        else:
            print("\nNo fire-related news found. This could be due to:")
            print("- No recent fire incidents reported")
            print("- Website structure changes")
            print("- Connection issues")
            
            # Offer to create manual template
            create_template = input("\nWould you like to create a manual fire news template? (y/n): ")
            if create_template.lower() == 'y':
                create_manual_fire_news_template()
        
    except KeyboardInterrupt:
        print("\nScraping interrupted by user")
    except Exception as e:
        print(f"Error during scraping: {e}")
        print("Consider trying alternative news sources or manual data collection")

def test_fire_filter():
    """Test function to verify fire filtering is working correctly"""
    scraper = HPDFireNewsScraper()
    
    # Test news items - mix of fire and non-fire content
    test_items = [
        {
            'title': 'HPD Responds to Structure Fire in Kalihi',
            'content': 'Honolulu Police Department assisted firefighters at a house fire...',
            'full_text': 'HPD Responds to Structure Fire in Kalihi. Honolulu Police Department assisted firefighters at a house fire...',
            'link': 'https://example.com/fire-news',
            'date': '2025-07-08'
        },
        {
            'title': 'Community Meeting on Traffic Safety',
            'content': 'HPD will host a community meeting to discuss traffic safety measures...',
            'full_text': 'Community Meeting on Traffic Safety. HPD will host a community meeting to discuss traffic safety measures...',
            'link': 'https://example.com/traffic-news',
            'date': '2025-07-08'
        },
        {
            'title': 'HFD Responds to Brush Fire Near Diamond Head',
            'content': 'Honolulu Fire Department crews worked to contain a brush fire...',
            'full_text': 'HFD Responds to Brush Fire Near Diamond Head. Honolulu Fire Department crews worked to contain a brush fire...',
            'link': 'https://example.com/brush-fire',
            'date': '2025-07-08'
        },
        {
            'title': 'Drug Bust in Downtown Honolulu',
            'content': 'HPD arrested three individuals in a drug trafficking operation...',
            'full_text': 'Drug Bust in Downtown Honolulu. HPD arrested three individuals in a drug trafficking operation...',
            'link': 'https://example.com/drug-bust',
            'date': '2025-07-08'
        },
        {
            'title': 'Arson Investigation Underway',
            'content': 'Police are investigating a series of suspicious fires in Waikiki...',
            'full_text': 'Arson Investigation Underway. Police are investigating a series of suspicious fires in Waikiki...',
            'link': 'https://example.com/arson',
            'date': '2025-07-08'
        }
    ]
    
    print("Testing fire filter with sample data...")
    print("=" * 50)
    
    fire_items = scraper.filter_for_fire_news(test_items)
    
    print(f"\nResults:")
    print(f"Original items: {len(test_items)}")
    print(f"Fire-related items kept: {len(fire_items)}")
    print(f"Non-fire items filtered out: {len(test_items) - len(fire_items)}")
    
    print("\nFire-related items kept:")
    for item in fire_items:
        print(f"- {item['title']}")
    
    return fire_items

if __name__ == "__main__":
    # Test fire filtering first
    print("Testing fire filtering functionality...")
    test_fire_filter()
    
    print("\n" + "=" * 50)
    print("Starting main fire news scraper...")
    print("=" * 50)
    
    # Run main scraper
    main()