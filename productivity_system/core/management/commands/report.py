from django.core.management.base import BaseCommand
from django.db.models import Avg, Count, Sum

from core.models import CameraAnalytics, ComputerActivity


class Command(BaseCommand):
    help = "Aggregate query tailan (employee bureer)"

    def handle(self, *args, **options):
        self.stdout.write("== Computer activity ==")
        rows = (
            ComputerActivity.objects.values("employee__full_name")
            .annotate(
                active=Sum("active_seconds"),
                idle=Sum("idle_seconds"),
                keys=Sum("key_count"),
                clicks=Sum("click_count"),
            )
            .order_by("employee__full_name")
        )
        for r in rows:
            self.stdout.write(
                f"{r['employee__full_name']:<8} active={r['active']}s "
                f"idle={r['idle']}s keys={r['keys']} clicks={r['clicks']}"
            )

        self.stdout.write("== Camera ==")
        cams = (
            CameraAnalytics.objects.values("employee__full_name")
            .annotate(n=Count("id"), avg_conf=Avg("confidence"))
            .order_by("employee__full_name")
        )
        for r in cams:
            self.stdout.write(
                f"{r['employee__full_name']:<8} records={r['n']} "
                f"avg_confidence={r['avg_conf']:.2f}"
            )
