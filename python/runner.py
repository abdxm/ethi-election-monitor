
import sys

from classifier import classify
from db import get_connection, insert_post, normalize_post_date
from scraper import scrape_all


def run() -> int:
    print("[runner] Starting EthiElection ingestion pipeline")

    try:
        connection = get_connection()
    except Exception as exc:
        print(f"[runner] Database connection failed: {exc}")
        return 1

    try:
        posts = scrape_all()
        print(f"[runner] Scraped {len(posts)} posts")

        inserted = 0
        skipped = 0

        for raw_post in posts:
            classification = classify(raw_post["content"])
            post = {
                "source_url": raw_post["source_url"][:512],
                "content": raw_post["content"],
                "media": raw_post.get("media"),
                "page_name": raw_post["page_name"][:255],
                "post_date": normalize_post_date(raw_post["post_date"]),
                "classification": classification,
            }

            if insert_post(connection, post):
                inserted += 1
                print(f"[runner] Inserted ({classification}): {post['source_url']}")
            else:
                skipped += 1
                print(f"[runner] Skipped duplicate: {post['source_url']}")

        print(f"[runner] Done — inserted: {inserted}, skipped: {skipped}")
        return 0
    except Exception as exc:
        print(f"[runner] Pipeline error: {exc}")
        return 1
    finally:
        connection.close()


if __name__ == "__main__":
    sys.exit(run())
