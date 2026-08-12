import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from django.contrib.auth.models import User
from projects.models import Project
from skills.models import Skill

# Create superuser if not exists
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("Created superuser 'admin' with password 'admin123'")

# Seed initial projects if empty
if Project.objects.count() == 0:
    Project.objects.create(
        title="Portfolio Backend API",
        description="A Django REST Framework backend providing dynamic content management via Django Admin, serving projects and handling contact forms.",
        tech_stack="Python, Django, DRF, SQLite, CORS",
        github_url="https://github.com/HariharanVS-33/portfolio-backend",
        demo_url="http://127.0.0.1:8000/admin/",
        is_active=True
    )
    Project.objects.create(
        title="Portfolio Frontend Web App",
        description="A modern, responsive React + Vite portfolio application that fetches project data dynamically from the Django API.",
        tech_stack="React, Vite, JavaScript, CSS3, HTML5",
        github_url="https://github.com/HariharanVS-33/portfolio-frontend",
        demo_url="http://localhost:5173",
        is_active=True
    )
    Project.objects.create(
        title="AI Chatbot CLI",
        description="A command line tool built for intelligent conversational workflows and data processing.",
        tech_stack="Python, OpenAI, CLI",
        github_url="https://github.com/HariharanVS-33",
        demo_url="",
        is_active=True
    )
    print("Seeded 3 sample projects into the database.")

# Seed initial skills if empty
if Skill.objects.count() == 0:
    initial_skills = [
        {"category": "Frontend", "name": "HTML", "order": 1},
        {"category": "Frontend", "name": "CSS", "order": 2},
        {"category": "Frontend", "name": "JavaScript", "order": 3},
        {"category": "Frontend", "name": "React", "order": 4},

        {"category": "Backend", "name": "Python", "order": 1},
        {"category": "Backend", "name": "Django", "order": 2},
        {"category": "Backend", "name": "REST API", "order": 3},

        {"category": "Data Structures", "name": "C", "order": 1},
        {"category": "Data Structures", "name": "Algorithms", "order": 2},

        {"category": "Tools", "name": "Git", "order": 1},
        {"category": "Tools", "name": "GitHub", "order": 2},
        {"category": "Tools", "name": "VS Code", "order": 3},
    ]
    for item in initial_skills:
        Skill.objects.create(**item)
    print(f"Seeded {len(initial_skills)} skills into the database.")
