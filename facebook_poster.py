import os
import argparse
import requests

API_URL = "https://graph.facebook.com/v18.0"


def _access_token() -> str:
    token = os.getenv("FACEBOOK_ACCESS_TOKEN")
    if not token:
        raise RuntimeError("FACEBOOK_ACCESS_TOKEN is not set")
    return token


def post_to_page(page_id: str, message: str, link: str | None = None) -> dict:
    """Post a message to a Facebook page.

    Requires the ``pages_manage_posts`` permission.
    """
    url = f"{API_URL}/{page_id}/feed"
    data = {"message": message, "access_token": _access_token()}
    if link:
        data["link"] = link
    response = requests.post(url, data=data, timeout=30)
    response.raise_for_status()
    return response.json()


def post_to_group(group_id: str, message: str, link: str | None = None) -> dict:
    """Post a message to a Facebook group.

    Requires the ``publish_to_groups`` permission.
    """
    url = f"{API_URL}/{group_id}/feed"
    data = {"message": message, "access_token": _access_token()}
    if link:
        data["link"] = link
    response = requests.post(url, data=data, timeout=30)
    response.raise_for_status()
    return response.json()


def create_marketplace_listing(
    catalog_id: str,
    title: str,
    description: str,
    price: float,
    currency: str,
    image_url: str,
) -> dict:
    """Create a listing in a Facebook catalog for Marketplace.

    This uses the Commerce API. Your app must have appropriate permissions and
    the catalog must be associated with a commerce account.
    """
    url = f"{API_URL}/{catalog_id}/products"
    data = {
        "retailer_id": title,
        "name": title,
        "description": description,
        "price": price,
        "currency": currency,
        "image_url": image_url,
        "access_token": _access_token(),
    }
    response = requests.post(url, data=data, timeout=30)
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser(description="Post content to Facebook")
    sub = parser.add_subparsers(dest="command", required=True)

    page_parser = sub.add_parser("page", help="Post to a page")
    page_parser.add_argument("page_id")
    page_parser.add_argument("message")
    page_parser.add_argument("--link")

    group_parser = sub.add_parser("group", help="Post to a group")
    group_parser.add_argument("group_id")
    group_parser.add_argument("message")
    group_parser.add_argument("--link")

    mp_parser = sub.add_parser("marketplace", help="Create a marketplace listing")
    mp_parser.add_argument("catalog_id")
    mp_parser.add_argument("title")
    mp_parser.add_argument("description")
    mp_parser.add_argument("price", type=float)
    mp_parser.add_argument("currency")
    mp_parser.add_argument("image_url")

    args = parser.parse_args()
    if args.command == "page":
        print(post_to_page(args.page_id, args.message, args.link))
    elif args.command == "group":
        print(post_to_group(args.group_id, args.message, args.link))
    elif args.command == "marketplace":
        print(
            create_marketplace_listing(
                args.catalog_id,
                args.title,
                args.description,
                args.price,
                args.currency,
                args.image_url,
            )
        )


if __name__ == "__main__":
    main()
