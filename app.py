import os
import feedparser
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def fetch_feed(url):
    import requests
    print("Fetching feed...")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        feed = feedparser.parse(response.content)
    except Exception as e:
        print(f"Network error: {e}")
        return None, None

    if not feed.entries:
        print("No episodes found. Check the RSS URL.")
        return None, None

    episodes = []
    for entry in feed.entries:
        episodes.append({
            "title": entry.get("title", "Untitled"),
            "published": entry.get("published", "Unknown"),
            "duration": entry.get("itunes_duration", "unknown"),
            "summary": entry.get("summary", "")[:250]
        })

    name = feed.feed.get("title", "Unknown Podcast")
    return pd.DataFrame(episodes), name

    if not feed.entries:
        print("No episodes found. Check the RSS URL.")
        return None, None

    episodes = []
    for entry in feed.entries:
        episodes.append({
            "title": entry.get("title", "Untitled"),
            "published": entry.get("published", "Unknown"),
            "duration": entry.get("itunes_duration", "unknown"),
            "summary": entry.get("summary", "")[:250]
        })

    name = feed.feed.get("title", "Unknown Podcast")
    return pd.DataFrame(episodes), name


def get_insights(titles, podcast_name):
    sample = "\n".join(titles[:30])

    prompt = f"""
You're a senior media analyst at a podcast network.

Analyze the podcast "{podcast_name}" based on these episode titles.
Return exactly this format, no extra text:

TOP THEMES: [3 recurring topics separated by commas]
CONTENT STYLE: [interview / educational / storytelling / news / comedy]
TARGET AUDIENCE: [one sentence]
POSTING PATTERN: [consistent / sporadic / seasonal]
GROWTH OPPORTUNITY: [one specific actionable recommendation]
COMPETITIVE POSITIONING: [one sentence on how this show stands out]
OVERALL RATING: [1-10 as a content strategy score]

Episode titles:
{sample}
"""
    res = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    return res.choices[0].message.content.strip()


def main():
    print()
    print("=" * 52)
    print("  Podcast RSS Analyzer")
    print("  AI content intelligence for media companies")
    print("=" * 52)
    print()

    url = input("Paste podcast RSS URL: ").strip()
    if not url:
        print("No URL entered.")
        return

    df, name = fetch_feed(url)
    if df is None:
        return

    print(f"\nPodcast: {name}")
    print(f"Episodes found: {len(df)}")
    print("\nRunning AI analysis...\n")

    try:
        insights = get_insights(df["title"].tolist(), name)
        print("-" * 52)
        print(insights)
        print("-" * 52)

        filename = name.replace(" ", "_")[:40] + "_analysis.csv"
        df.to_csv(filename, index=False)
        print(f"\nFull episode data saved to: {filename}")

    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
