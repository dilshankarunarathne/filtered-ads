# Filtered Ads Recommender
 Querying ads based on a specific interest, using various social networks and cloud APIs.

[![Version](https://img.shields.io/badge/version-0.1-brightgreen.svg)](https://pypi.org/project/ad-topic-recommender/)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Description

This project is a proof of concept for a recommender system that queries ads based on a specific interest, 
using various social networks and cloud APIs. The system is designed to be used by a user who is interested 
in a specific topic and wants to find ads related to that topic. 

This has implementations in Python, to query ads from Facebook, Google and TikTok.

## Installation

### Requirements

- Python 3.6+
- [Facebook Ads API](https://developers.facebook.com/docs/marketing-apis/)
- [Google Ads API](https://developers.google.com/google-ads/api/docs/start)
- [TikTok Ads API](https://ads.tiktok.com/marketing_api/docs?rid=1x9q2xq3x1&id=1678521271494146)

### Install

```bash
pip install ad-topic-recommender
```

## Usage

### Facebook

```python
from ad_topic_recommender import FacebookAds
```

#### Authentication

```python
