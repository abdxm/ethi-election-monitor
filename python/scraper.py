
from datetime import datetime, timedelta
from typing import Any

from dotenv import load_dotenv

load_dotenv()

SAMPLE_POSTS: list[dict[str, Any]] = [
    {
        "source_url": "https://facebook.com/ethiopolitics/posts/sample-001",
        "content": (
            "The National Election Board announced updated voter registration "
            "schedules for all regions. Citizens are encouraged to verify their "
            "registration status before the deadline. የምርጫ መዝገብ ጊዜ ተሻሽሏል።"
        ),
        "media": None,
        "page_name": "Ethiopia Election Updates",
        "post_date": datetime.utcnow() - timedelta(hours=6),
    },
    {
        "source_url": "https://facebook.com/ethiopolitics/posts/sample-002",
        "content": (
            "Breaking: Clashes reported in downtown Addis Ababa during opposition "
            "protest. Police say several people were injured. "
            "ግጭት በአዲስ አበባ ተመዝግቧል። ተገድለው ቁስለው ነው።"
        ),
        "media": "https://picsum.photos/seed/ethiopolitics1/800/450",
        "page_name": "Addis Political Watch",
        "post_date": datetime.utcnow() - timedelta(hours=4),
    },
    {
        "source_url": "https://facebook.com/ethiopolitics/posts/sample-003",
        "content": (
            "Press release: Three major parties signed a joint statement on "
            "peaceful campaigning ahead of the election. "
            "መግለጫ፡ ሶስት ፓርቲዎች ሰላማዊ ዘመቻ ላይ ተስማምተዋል።"
        ),
        "media": None,
        "page_name": "Ethiopia Election Updates",
        "post_date": datetime.utcnow() - timedelta(hours=2),
    },
    {
        "source_url": "https://facebook.com/ethiopolitics/posts/sample-004",
        "content": (
            "Fire broke out near a polling station in Hawassa. Emergency teams "
            "responded quickly. No casualties reported yet. "
            "እሳት በሀዋሳ ድምጽ መስጫ ማዕከል አቅራቢያ ተከስቷል።"
        ),
        "media": "https://picsum.photos/seed/ethiopolitics2/800/450",
        "page_name": "Southern Region News",
        "post_date": datetime.utcnow() - timedelta(hours=1),
    },
    {
        "source_url": "https://facebook.com/ethiopolitics/posts/sample-005",
        "content": (
            "Candidate debate schedule published for next week. "
            "Topics include economy, security, and democratic reform. "
            "የእርካታ መርሃግብር ተለጠፈ።"
        ),
        "media": None,
        "page_name": "Ethiopia Election Updates",
        "post_date": datetime.utcnow() - timedelta(minutes=30),
    },
]




def get_sample_posts() -> list[dict[str, Any]]:
    return [dict(post) for post in SAMPLE_POSTS]


def scrape_all() -> list[dict[str, Any]]:
 
   
        print("[scraper] Using sample demo posts")
        return get_sample_posts()

