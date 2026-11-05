import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import (
    CameraAnalytics,
    ComputerActivity,
    ConsentRecord,
    Department,
    Employee,
    Task,
)


class Command(BaseCommand):
    help = "Test data: 3 department, 5 employee, 20 task, activity, camera"

    def handle(self, *args, **options):
        for model in (CameraAnalytics, ComputerActivity, Task,
                      ConsentRecord, Employee, Department):
            model.objects.all().delete()

        depts = [Department.objects.create(name=n) for n in ["IT", "HR", "Sales"]]

        employees = []
        for i, name in enumerate(["Bat", "Dorj", "Saraa", "Tuya", "Ganaa"]):
            emp = Employee.objects.create(
                department=depts[i % 3],
                full_name=name,
                email=f"{name.lower()}@example.com",
            )
            employees.append(emp)
            for ctype in ("computer", "camera"):
                ConsentRecord.objects.create(
                    employee=emp, consent_type=ctype,
                    is_granted=True, granted_at=timezone.now(),
                )

        statuses = ["todo", "in_progress", "done"]
        for i in range(20):
            Task.objects.create(
                employee=random.choice(employees),
                title=f"Task {i + 1}",
                status=random.choice(statuses),
                due_date=date.today() + timedelta(days=random.randint(1, 30)),
            )

        apps = ["chrome.exe", "code.exe", "excel.exe", "teams.exe"]
        for emp in employees:
            for d in range(7):
                ComputerActivity.objects.create(
                    employee=emp,
                    date=date.today() - timedelta(days=d),
                    active_seconds=random.randint(14000, 26000),
                    idle_seconds=random.randint(1000, 6000),
                    key_count=random.randint(3000, 15000),
                    click_count=random.randint(1000, 6000),
                    app_name=random.choice(apps),
                )
            for h in range(8):
                CameraAnalytics.objects.create(
                    employee=emp,
                    observed_at=timezone.now() - timedelta(hours=h),
                    is_at_desk=random.random() > 0.2,
                    confidence=round(random.uniform(0.6, 0.99), 2),
                )

        self.stdout.write(self.style.SUCCESS(
            "Seed duuslaa: 5 employee, 20 task, activity, camera"))
