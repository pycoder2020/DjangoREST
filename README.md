# YouTube Integration Simulation

A Django project that simulates YouTube video and comment management with scheduled content generation.

## Tech Stack

- Django 4.2 + Django REST Framework
- PostgreSQL
- Celery + Redis (scheduled tasks)
- Docker Compose

## Setup

```bash
# Start all services (migrations run automatically)
docker compose up --build

# Create superuser (optional)
docker compose exec web uv run python manage.py createsuperuser

# Generate initial data (optional)
docker compose exec web uv run python manage.py shell -c "
from videos.tasks import generate_video, generate_comments
for _ in range(5): generate_video()
generate_comments(20)
"
```

**Note:** Migrations run automatically on startup via `entrypoint.sh`. Celery services wait for the web service to be healthy before starting.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/videos/` | GET | List videos (paginated) |
| `/api/videos/` | POST | Create a new video |
| `/api/videos/{id}/` | GET | Video detail |
| `/api/videos/{id}/comments/` | GET | Comments for a video (paginated) |
| `/api/videos/{id}/comments/` | POST | Add comment to video |
| `/api/stats/` | GET | Engagement statistics |
| `/admin/` | - | Django admin panel |

## Celery Tasks

Available tasks in `videos/tasks.py`:

- `generate_video()` - Create a simulated video
- `generate_comments(count)` - Generate random comments
- `simulate_activity()` - Simulate YouTube-like activity

### Schedule tasks via Django Admin

1. Go to `/admin/`
2. Navigate to "Periodic Tasks"
3. Create a task pointing to `videos.tasks.simulate_activity`
4. Set interval (e.g., every 30 seconds)

## Assumptions & Shortcuts

- Video IDs are randomly generated (11 chars like YouTube)
- Comment generation uses simple template-based logic
- No authentication required for API endpoints

## Future Improvements

- Add user authentication
- Implement video view counts
- Add comment likes/replies
- Rate limiting on endpoints
- Integrate 3rd party AI services for comments generation
- Optimization
- Add SCA
- Add automated tests
