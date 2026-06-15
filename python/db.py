
import os
from datetime import datetime
from typing import Any

import pymysql
from dotenv import load_dotenv

load_dotenv()


def get_connection() -> pymysql.connections.Connection:
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "election_db"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def ensure_posts_table(connection: pymysql.connections.Connection) -> None:
    create_sql = """
        CREATE TABLE IF NOT EXISTS posts (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            source_url VARCHAR(512) NOT NULL,
            content TEXT NOT NULL,
            media VARCHAR(512) NULL,
            page_name VARCHAR(255) NOT NULL,
            post_date DATETIME NOT NULL,
            classification ENUM('information', 'incident') NOT NULL,
            created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            UNIQUE KEY posts_source_url_unique (source_url)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    """
    with connection.cursor() as cursor:
        cursor.execute(create_sql)
    connection.commit()


def insert_post(
    connection: pymysql.connections.Connection,
    post: dict[str, Any],
) -> bool:
   
    sql = """
        INSERT INTO posts (source_url, content, media, page_name, post_date, classification)
        VALUES (%(source_url)s, %(content)s, %(media)s, %(page_name)s, %(post_date)s, %(classification)s)
        ON DUPLICATE KEY UPDATE source_url = source_url
    """
    with connection.cursor() as cursor:
        affected = cursor.execute(sql, post)
    connection.commit()
    return affected == 1


def normalize_post_date(value: datetime | str) -> str:
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return str(value)
