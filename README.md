# Podcast RSS Analyzer

Feed it any podcast RSS URL and get back AI-generated content intelligence — themes, audience profile, content style, growth recommendations, and competitive positioning. Full episode dataset exports to CSV automatically.

Built this because podcast networks managing dozens of shows need a faster way to audit content strategy across their catalog. Manually listening to thousands of episodes is not realistic — this does the same analysis in seconds.

## What it returns

    TOP THEMES:              Celebrity Interviews, Comedy, Entertainment
    CONTENT STYLE:           Interview
    TARGET AUDIENCE:         Comedy enthusiasts and pop culture followers
    POSTING PATTERN:         Consistent
    GROWTH OPPORTUNITY:      Add audience Q&A segments to boost engagement
    COMPETITIVE POSITIONING: Leverages host's brand for unique guest access
    OVERALL RATING:          8.5/10

## Stack

- Python 3
- OpenAI GPT-4
- feedparser
- pandas
- requests

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    export OPENAI_API_KEY=your-key-here
    python3 app.py

## Architecture

Follows an ETL pipeline pattern used in data engineering at media companies at scale.

- Extract — requests and feedparser pull raw episode data from any RSS feed
- Transform — pandas structures it into clean tabular format
- Enrich — GPT-4 runs content intelligence across the episode catalog
- Load — exports full dataset to CSV for downstream use

Output is intentionally portable. A CSV can go into Excel, a database, a BI tool, or another pipeline without any parsing work.

## Real use cases

- Podcast network content audits across 50+ shows
- Competitive analysis for media companies
- Content strategy optimization for new shows
- Catalog tagging and classification at scale

## What I would add next

- Spotify Podcast API for listener demographic data
- Sentiment analysis per episode summary
- Streamlit dashboard with release frequency and topic trend charts
- Scheduled runs with automated weekly email reports
- Multi-feed batch mode for full network analysis
