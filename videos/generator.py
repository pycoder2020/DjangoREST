import random
import string

# Simple templates for generating mock content
VIDEO_TITLES = [
    "How to {verb} {noun} in {year}",
    "{adjective} {noun} Tutorial",
    "Top 10 {noun} Tips",
    "{noun} Review - Is It Worth It?",
    "Learn {noun} in 10 Minutes",
]

VERBS = ["master", "learn", "build", "create", "improve", "understand"]
NOUNS = ["Python", "Django", "coding", "programming", "web development", "APIs"]
ADJECTIVES = ["Amazing", "Ultimate", "Complete", "Quick", "Easy", "Advanced"]

COMMENT_TEMPLATES = [
    "Great video! {reaction}",
    "This helped me a lot, {thanks}",
    "{reaction} I learned so much!",
    "Can you make a video about {topic}?",
    "Finally someone explains this well!",
    "{greeting} Thanks for sharing!",
]

REACTIONS = ["🔥", "Awesome!", "Love it!", "Perfect!", "Incredible!"]
THANKS = ["thanks!", "thank you!", "appreciate it!", "much appreciated!"]
GREETINGS = ["Hey!", "Hi!", "Hello!", "Nice!"]
TOPICS = ["advanced topics", "more examples", "real projects", "debugging tips"]

AUTHOR_NAMES = [
    "TechFan", "CodeMaster", "DevLearner", "PythonPro", "WebDev",
    "Programmer", "Student", "Developer", "Coder", "Engineer",
]


def generate_video_id():
    """Generate a random YouTube-like video ID."""
    chars = string.ascii_letters + string.digits + "-_"
    return ''.join(random.choice(chars) for _ in range(11))


def generate_video_url(video_id):
    """Generate a fake video URL."""
    return f"https://videourl.example/{video_id}"


def generate_video_title():
    """Generate a random video title."""
    template = random.choice(VIDEO_TITLES)
    return template.format(
        verb=random.choice(VERBS),
        noun=random.choice(NOUNS),
        adjective=random.choice(ADJECTIVES),
        year=random.randint(2025, 2026),
    )


def generate_video_description():
    """Generate a simple video description."""
    noun = random.choice(NOUNS)
    return f"In this video, we explore {noun}. Don't forget to like and subscribe!"


def generate_comment_text():
    """Generate a random comment using templates."""
    template = random.choice(COMMENT_TEMPLATES)
    return template.format(
        reaction=random.choice(REACTIONS),
        thanks=random.choice(THANKS),
        greeting=random.choice(GREETINGS),
        topic=random.choice(TOPICS),
    )


def generate_author_name():
    """Generate a random author name."""
    name = random.choice(AUTHOR_NAMES)
    suffix = random.randint(1, 999)
    return f"{name}{suffix}"
