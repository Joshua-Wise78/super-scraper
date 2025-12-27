from bs4 import BeautifulSoup
import aiohttp

from jsonUtils import retrieve_from_json

async def get_fandom(key, query):
    success, value = retrieve_from_json(key)
    if not success:
        return False, value

    site_domain = value
    api_url = f"{site_domain}/api.php"

    async with aiohttp.ClientSession() as session:
        searchParams = {
            "action": "opensearch",
            "format": "json",
            "search": query,
            "limit": 1,
            "redirects": "resolve"
        }

        try:
            async with session.get(api_url, params=searchParams) as response:
                if response.status != 200:
                    return False, f"API Error: {response.status}"

                searchData = await response.json()

                if not searchData or len(searchData) < 2 or not searchData[1]:
                    return False, f"No items found for '{query}'"

                bestMatch = searchData[1][0]

        except Exception as e:
            return False, f"Search failed: {str(e)}"

        page_url = f"{site_domain}/wiki/{bestMatch.replace(' ', '_')}"

        try:
            async with session.get(page_url) as response:
                if response.status != 200:
                    return False, "Failed to load page HTML."
                
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')

                description = "No description found."
                content_div = soup.find('div', {'class': 'mw-parser-output'})
                if content_div:
                    for p in content_div.find_all('p', recursive=False):
                        if p.text.strip():
                            description = p.text.strip()
                            break

                image_url = None
                infobox = soup.find('aside', {'class': 'portable-infobox'})
                
                if infobox:
                    image_figure = infobox.find('figure', {'class': 'pi-image'})
                    
                    if image_figure:
                        img_tag = image_figure.find('img')
                        if img_tag:
                            image_url = img_tag.get('data-src') or img_tag.get('src')
                    
                    if not image_url:
                        first_img = infobox.find('img')
                        if first_img:
                             image_url = first_img.get('data-src') or first_img.get('src')

                stats = []
                if infobox:
                    rows = infobox.find_all('div', {'class': 'pi-data'})
                    for row in rows[:5]:
                        label = row.find('h3', {'class': 'pi-data-label'})
                        value = row.find('div', {'class': 'pi-data-value'})
                        if label and value:
                            stats.append(f"{label.text.strip()}: {value.text.strip()}")

                if stats:
                    description += "\n\n" + "\n".join(stats)

                return True, {
                    "title": bestMatch,
                    "summary": description,
                    "image": image_url,
                    "url": page_url
                }

        except Exception as e:
            return False, f"Scraping failed: {str(e)}"
