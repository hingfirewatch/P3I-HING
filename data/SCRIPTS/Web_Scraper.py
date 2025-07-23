#!/usr/bin/env python3
"""
Unified Fire Scraper & AI Emergency Filter (Multi-page with Emojis + Error Logging + Boot Banner)
Scrapes multiple fire/emergency websites, applies inlined AI filter,
adds "type_of_fire", removes duplicates, reports HTTP errors,
and runs in 10-minute intervals with a boot message.
"""

import requests
from bs4 import BeautifulSoup
import re
import json
import time
from datetime import datetime

# ================================
# 🚀 Boot Banner
# ================================
ascii_art = [
".___________. __    __   _______  __    ______    ____    __    ____  _______ .______           _______.  ______ .______          ___      .______    _______ .______      ",
"|           ||  |  |  | |   ____||  |  /      |   \\   \\  /  \\  /   / |   ____||   _  \\         /       | /      ||   _  \\        /   \\     |   _  \\  |   ____||   _  \\     ",
"`---|  |----`|  |__|  | |  |__   |  | |  ,----'    \\   \\/    \\/   /  |  |__   |  |_)  |       |   (----`|  ,----'|  |_)  |      /  ^  \\    |  |_)  | |  |__   |  |_)  |    ",
"    |  |     |   __   | |   __|  |  | |  |          \\            /   |   __|  |   _  <         \\   \\    |  |     |      /      /  /_\\  \\   |   ___/  |   __|  |      /     ",
"    |  |     |  |  |  | |  |     |  | |  `----.      \\    /\\    /    |  |____ |  |_)  |    .----)   |   |  `----.|  |\\  \\----./  _____  \\  |  |      |  |____ |  |\\  \\----.",
"    |__|     |__|  |__| |__|     |__|  \\______|       \\__/  \\__/     |_______||______/     |_______/     \\______|| _| `._____/__/     \\__\\ | _|      |_______|| _| `._____|"
]
for line in ascii_art:
    print(line)


class WildfireFilter:
    def __init__(self):
        self.fire_incident_keywords = {
            'wildfire', 'wildland fire', 'forest fire', 'brush fire', 'grass fire',
            'blaze', 'inferno', 'conflagration', 'bushfire', 'prairie fire',
            'fire incident', 'fire emergency', 'fire alert', 'fire warning',
            'fire report', 'fire danger', 'fire risk', 'fire hazard',
            'fire outbreak', 'fire broke out', 'fire started', 'fire ignited',
            'red flag warning', 'fire weather', 'fire season',
            'fire suppression', 'fire containment', 'fire perimeter',
            'acres burned', 'hectares burned', 'fire size', 'fire spread',
            'fire behavior', 'vegetation fire', 'structure fire',
            'residential fire', 'commercial fire', 'building fire',
            'arson', 'prescribed burn', 'controlled burn',
            'fire break', 'firebreak', 'fire line', 'fire retardant',
            'air tanker', 'water drop', 'fire aircraft', 'fire bomber'
        }
        self.fire_descriptors = {
            'smoke', 'ash', 'ember', 'flame', 'flames', 'burn', 'burning', 'burnt',
            'charred', 'scorched', 'ignition', 'ignited', 'combustion',
            'firefighter', 'fire crew', 'evacuation', 'evacuate', 'evacuated'
        }
        self.exclusion_patterns = [
            r'\bfire\s*department\b(?!\s+(respond|fighting|battle|combat|suppress))',
            r'\bfire\s*station\b(?!\s+(respond|emergency))',
            r'\bfire\s*chief\b(?!\s+(said|report|warn|alert))',
            r'\bfire\s*marshal\b(?!\s+(said|report|warn|investigate))',
            r'\bfire\s*code\b', r'\bfire\s*safety\b', r'\bfire\s*drill\b',
            r'\bfire\s*inspection\b', r'\bfire\s*permit\b', r'\bfire\s*training\b',
            r'\bunder\s+fire\b', r'\bopen\s+fire\b', r'\bceasefire\b',
            r'\bfire\s+(hiring|employment|job)\b', r'\bfireworks?\b(?!\s+(cause|start|ignit))',
            r'\bfire\s+alarm\b(?!\s+(due\s+to|because\s+of|caused\s+by))'
        ]
        self.fire_incident_patterns = [
            r'\b\d+\s*acres?\s*(burned?|burnt|scorched|destroyed)\b',
            r'\bfire\s*(started|began|ignited|broke\s*out|erupted)\b',
            r'\b(flames?|smoke)\s*(visible|seen|spotted)\b',
            r'\b(burning|fire)\s*(building|home|house|structure)\b'
        ]
        self.compiled_incident_patterns = [re.compile(p, re.IGNORECASE) for p in self.fire_incident_patterns]
        self.compiled_exclusion_patterns = [re.compile(p, re.IGNORECASE) for p in self.exclusion_patterns]

    def is_fire_related(self, text):
        if not isinstance(text, str):
            return False
        text_lower = text.lower()
        for pattern in self.compiled_exclusion_patterns:
            if pattern.search(text_lower):
                return False
        for keyword in self.fire_incident_keywords:
            if keyword in text_lower:
                return True
        for pattern in self.compiled_incident_patterns:
            if pattern.search(text_lower):
                return True
        if any(d in text_lower for d in self.fire_descriptors):
            if any(c in text_lower for c in ['emergency', 'incident', 'evacuat', 'danger']):
                return True
        return False

    def analyze(self, item):
        if isinstance(item, dict):
            combined = ' '.join(str(v) for v in item.values() if v)
        else:
            combined = str(item)
        return self.is_fire_related(combined)

def fetch_soup(url):
    headers = [
        { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' },
        { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)' },
        { 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)' }
    ]
    for h in headers:
        try:
            resp = requests.get(url, headers=h, timeout=15)
            if resp.status_code == 200:
                return BeautifulSoup(resp.text, 'html.parser')
            else:
                print(f"⚠️  HTTP {resp.status_code} - {url}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed for {url}: {str(e)}")
    return None

def extract_articles(soup, base_url):
    results = []

    # 🌐 Default: search for <article>
    articles = soup.find_all('article')
    if articles:
        for article in articles:
            title_elem = article.find(['h1','h2','h3','h4'])
            link_elem = article.find('a', href=True)
            content = article.get_text(" ", strip=True)
            title = title_elem.get_text(strip=True) if title_elem else 'Untitled'
            link = link_elem['href'] if link_elem else None
            if link and link.startswith('/'):
                link = base_url.rstrip('/') + link
            results.append({
                'title': title,
                'link': link,
                'content': content,
                'date': extract_date(content)
            })
        return results

    # 🌐 Fallback for Maui County: <div class="CivicAlertsItem"> inside <div id="CivicAlertsList">
    if "mauicounty.gov" in base_url:
        for item in soup.select("div.CivicAlertsItem"):
            title_elem = item.find('a', href=True)
            title = title_elem.get_text(strip=True) if title_elem else 'Untitled'
            link = title_elem['href'] if title_elem else None
            if link and link.startswith('/'):
                link = base_url.rstrip('/') + link
            content = item.get_text(" ", strip=True)
            results.append({
                'title': title,
                'link': link,
                'content': content,
                'date': extract_date(content)
            })
        return results

    # 🌐 Fallback for Hawaii County: li.news-item
    if "hawaiicounty.gov" in base_url:
        for item in soup.select("li.news-item"):
            title_elem = item.find('a', href=True)
            title = title_elem.get_text(strip=True) if title_elem else 'Untitled'
            link = title_elem['href'] if title_elem else None
            if link and link.startswith('/'):
                link = base_url.rstrip('/') + link
            content = item.get_text(" ", strip=True)
            results.append({
                'title': title,
                'link': link,
                'content': content,
                'date': extract_date(content)
            })
        return results

    # 🌐 Fallback for Kauai: div.press-item or li
    if "kauai.gov" in base_url:
        for item in soup.select("li, div.press-item"):
            title_elem = item.find('a', href=True)
            title = title_elem.get_text(strip=True) if title_elem else 'Untitled'
            link = title_elem['href'] if title_elem else None
            if link and link.startswith('/'):
                link = base_url.rstrip('/') + link
            content = item.get_text(" ", strip=True)
            if len(content) > 50:
                results.append({
                    'title': title,
                    'link': link,
                    'content': content,
                    'date': extract_date(content)
                })
        return results

    # 🚫 Nothing matched
    return results


def extract_date(text):
    match = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}", text)
    return match.group(0) if match else None

def detect_type(content):
    if not content: return None
    content = content.lower()
    if 'structure fire' in content or 'building fire' in content:
        return 'structure'
    elif 'vehicle fire' in content or 'car fire' in content:
        return 'vehicle'
    elif 'brush fire' in content or 'wildfire' in content:
        return 'wildland'
    elif 'residential' in content or 'home fire' in content:
        return 'residential'
    elif 'commercial' in content:
        return 'commercial'
    return 'unknown'

def deduplicate_entries(entries):
    seen = set()
    deduped = []
    for item in entries:
        key = item.get('link') or item.get('title') + item.get('content', '')
        if key not in seen:
            seen.add(key)
            deduped.append(item)
    return deduped

def scrape_multipage(base_url, max_pages=5):
    all_items = []
    for page in range(1, max_pages+1):
        url = f"{base_url}?page={page}" if page > 1 else base_url
        soup = fetch_soup(url)
        if not soup:
            print(f"  ❌ Failed to fetch page {page} (no response or HTML error)")
            break

        articles = extract_articles(soup, base_url)

        if not articles:
            if not soup.find_all('article'):
                print(f"  ⚠️ No <article> tags found on page {page} — structure may differ.")
            else:
                print(f"  ⚠️ No valid articles extracted on page {page}.")
        else:
            print(f"  📄 Page {page}: {len(articles)} entries")

        if not articles:
            break

        all_items.extend(articles)
        time.sleep(1)
    return all_items

def main_loop():
    urls = [
        "https://fire.honolulu.gov/news-and-info/news-releases/",
        "https://www.honolulupd.org/news/",
        "https://www.mauicounty.gov/CivicAlerts.aspx?CID=6,3,7",
        "https://www.hawaiicounty.gov/our-county/county-news/-seldept-7#newsdepts_11355_13347_1411",
        "https://www.hawaiipolice.gov/category/media-releases/",
        "https://www.kauai.gov/County-Press-Releases"
    ]
    wildfire_filter = WildfireFilter()
    while True:
        all_filtered = []
        print(f"🔍 Starting scan @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for url in urls:
            print(f"🌐 Scraping: {url}")
            entries = scrape_multipage(url, max_pages=5)
            fire_entries = []
            for item in entries:
                if wildfire_filter.analyze(item):
                    item['type_of_fire'] = detect_type(item.get('content', ''))
                    fire_entries.append(item)
            print(f"🔥 Fire-related entries found: {len(fire_entries)}")
            all_filtered.extend(fire_entries)

        all_filtered = deduplicate_entries(all_filtered)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"filtered_fire_news_{timestamp}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_filtered, f, indent=2, ensure_ascii=False)
        print(f"✅ Exported {len(all_filtered)} deduplicated entries to {output_file}")
        print("😴 Sleeping for 10 minutes...")
        time.sleep(600)

if __name__ == "__main__":
    main_loop()

