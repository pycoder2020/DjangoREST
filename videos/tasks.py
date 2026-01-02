import random
from celery import shared_task
from .models import Video, Comment
from .generator import (
    generate_video_id,
    generate_video_url,
    generate_video_title,
    generate_video_description,
    generate_comment_text,
    generate_author_name,
)


@shared_task
def generate_video():
    """Create a new simulated video."""
    video_id = generate_video_id()
    video = Video.objects.create(
        id=video_id,
        title=generate_video_title(),
        description=generate_video_description(),
        url=generate_video_url(video_id),
    )
    return f"Created video: {video.title}"


@shared_task
def generate_comments(count=5):
    """Generate random comments on random videos."""
    videos = Video.objects.all()
    if not videos.exists():
        return "No videos available for comments"

    created = 0
    for _ in range(count):
        video = random.choice(list(videos))
        Comment.objects.create(
            video=video,
            author=generate_author_name(),
            text=generate_comment_text(),
        )
        created += 1

    return f"Created {created} comments"


@shared_task
def simulate_activity():
    """Simulate YouTube-like activity: create videos and comments."""
    # 20% chance to create a new video
    if random.random() < 0.2:
        generate_video.delay()

    # Generate 1-3 comments
    generate_comments.delay(count=random.randint(1, 3))

    return "Activity simulated"
