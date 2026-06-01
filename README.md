# Podcast RSS Analyzer

A Python application that analyzes podcast RSS feeds and extracts useful information about episodes, publishing activity, and feed metadata.

The project demonstrates how structured podcast data can be collected, processed, and analyzed using Python.

## Why I Built This

Podcasts publish large amounts of information through RSS feeds, but most listeners never see the underlying data that powers podcast platforms.

I built this project to explore RSS parsing, API-style data processing, and data analysis techniques while working with real-world podcast datasets.

## Features

- RSS feed parsing
- Episode metadata extraction
- Podcast publishing analysis
- Feed validation
- Structured data processing
- Summary statistics and reporting

## Tech Stack

- Python
- Feedparser
- Pandas
- Requests
- Streamlit

## How It Works

1. User provides a podcast RSS feed URL
2. The application retrieves the feed
3. Episode metadata is extracted
4. Data is processed and analyzed
5. Results are displayed in a simple dashboard

## Example Insights

The application can be used to examine:

- Total episode count
- Publishing frequency
- Episode release trends
- Feed metadata quality
- Podcast activity patterns

## What I Learned

This project helped me improve my understanding of:

- RSS feed structures
- Data ingestion pipelines
- Working with external data sources
- Python data processing
- Building lightweight analytics tools

## Future Improvements

- Multi-feed comparison
- Podcast recommendation engine
- Sentiment analysis of episode titles
- Topic extraction using AI
- Historical trend tracking
- Exportable reports

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py


Notes:
This project is intended for learning and portfolio purposes. Podcast data availability depends on the quality and structure of the RSS feed being analyzed.

