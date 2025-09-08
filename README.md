# Facebook Posting System

This repository contains a Python script for posting advertisements to
Facebook pages, groups, and Marketplace catalogs using the Graph API.

## Requirements

- Python 3
- A Facebook app with appropriate permissions and an access token.

Install dependencies with:

```
pip install -r requirements.txt
```

Set the access token in an environment variable before running the script:

```
export FACEBOOK_ACCESS_TOKEN="<token>"
```

## Usage

Posting to a page:

```
python facebook_poster.py page <PAGE_ID> "Your message" [--link https://example.com]
```

Posting to a group:

```
python facebook_poster.py group <GROUP_ID> "Your message" [--link https://example.com]
```

Creating a Marketplace listing (requires a catalog and commerce permissions):

```
python facebook_poster.py marketplace <CATALOG_ID> "Title" "Description" 100 USD https://example.com/image.jpg
```

