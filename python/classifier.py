
INCIDENT_KEYWORDS = [
    # English
    "attack",
    "violence",
    "protest",
    "clash",
    "arrest",
    "killed",
    "injured",
    "riot",
    "shooting",
    "fire",
    "bomb",
    "conflict",
    "crisis",
    "emergency",
    "displacement",
    "casualty",
    "unrest",
    # Amharic
    "ግጭት",
    "ሰው ተገድሏል",
    "ተገድሏል",
    "ተቆጠሩ",
    "ተደምሰሱ",
    "ተቃውሞ",
    "አመላካች",
    "ድርጊት",
    "ጥቃት",
    "አደጋ",
    "እሳት",
    "ግድግዳ",
    "ሞት",
    "ቁስሎ",
    "አመቸ",
    "አለመሰላሰል",
    "አደጋ",
    "ድንገተኛ",
]

INFORMATION_KEYWORDS = [
    # English
    "announce",
    "statement",
    "press release",
    "campaign",
    "election",
    "vote",
    "candidate",
    "policy",
    "debate",
    "schedule",
    "update",
    "report",
    "meeting",
    "agenda",
    "registration",
    # Amharic
    "ማስታወቂያ",
    "መግለጫ",
    "መረጃ",
    "ምርጫ",
    "ድምጽ",
    "መዝገብ",
    "ወረቀት",
    "የምርጫ",
    "የድምጽ",
    "የዜና",
    "የፖለቲካ",
    "የመንግስት",
    "የአዲስ",
    "የቀን",
    "የጊዜ",
]


def classify(content: str) -> str:
   
    normalized = content.lower()

    incident_score = sum(1 for kw in INCIDENT_KEYWORDS if kw.lower() in normalized)
    information_score = sum(1 for kw in INFORMATION_KEYWORDS if kw.lower() in normalized)

    if incident_score > 0 and incident_score >= information_score:
        return "incident"
    if information_score > 0:
        return "information"
    return "information"
