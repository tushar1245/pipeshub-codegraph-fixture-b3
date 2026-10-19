"""Builds the monthly analytics report, one section per metric."""
from statistics import mean, median


class ReportBuilder:
    def __init__(self, rows: list[dict]) -> None:
        self.rows = rows

    def section_revenue_total(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "revenue",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_revenue_average(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "revenue",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_revenue_median(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "revenue",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_revenue_peak(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "revenue",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_revenue_floor(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "revenue",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_revenue_spread(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "revenue",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_revenue_count(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "revenue",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_revenue_share(self) -> dict:
        values = [float(r.get("revenue", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "revenue",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_total(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "orders",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_average(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "orders",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_median(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "orders",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_peak(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "orders",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_floor(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "orders",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_spread(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "orders",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_count(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "orders",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_orders_share(self) -> dict:
        values = [float(r.get("orders", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "orders",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_total(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "refunds",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_average(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "refunds",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_median(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "refunds",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_peak(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "refunds",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_floor(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "refunds",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_spread(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "refunds",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_count(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "refunds",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_refunds_share(self) -> dict:
        values = [float(r.get("refunds", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "refunds",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_total(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "sessions",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_average(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "sessions",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_median(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "sessions",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_peak(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "sessions",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_floor(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "sessions",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_spread(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "sessions",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_count(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "sessions",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_sessions_share(self) -> dict:
        values = [float(r.get("sessions", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "sessions",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_total(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "signups",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_average(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "signups",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_median(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "signups",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_peak(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "signups",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_floor(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "signups",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_spread(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "signups",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_count(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "signups",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_signups_share(self) -> dict:
        values = [float(r.get("signups", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "signups",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_total(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "churn",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_average(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "churn",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_median(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "churn",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_peak(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "churn",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_floor(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "churn",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_spread(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "churn",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_count(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "churn",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_churn_share(self) -> dict:
        values = [float(r.get("churn", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "churn",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_total(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "latency",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_average(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "latency",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_median(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "latency",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_peak(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "latency",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_floor(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "latency",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_spread(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "latency",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_count(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "latency",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_latency_share(self) -> dict:
        values = [float(r.get("latency", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "latency",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_total(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "errors",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_average(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "errors",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_median(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "errors",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_peak(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "errors",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_floor(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "errors",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_spread(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "errors",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_count(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "errors",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_errors_share(self) -> dict:
        values = [float(r.get("errors", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "errors",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_total(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "carts",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_average(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "carts",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_median(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "carts",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_peak(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "carts",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_floor(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "carts",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_spread(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "carts",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_count(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "carts",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_carts_share(self) -> dict:
        values = [float(r.get("carts", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "carts",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_total(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "checkouts",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_average(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "checkouts",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_median(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "checkouts",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_peak(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "checkouts",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_floor(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "checkouts",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_spread(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "checkouts",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_count(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "checkouts",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_checkouts_share(self) -> dict:
        values = [float(r.get("checkouts", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "checkouts",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_total(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "coupons",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_average(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "coupons",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_median(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "coupons",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_peak(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "coupons",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_floor(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "coupons",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_spread(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "coupons",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_count(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "coupons",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_coupons_share(self) -> dict:
        values = [float(r.get("coupons", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "coupons",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_total(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "returns",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_average(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "returns",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_median(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "returns",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_peak(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "returns",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_floor(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "returns",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_spread(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "returns",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_count(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "returns",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_returns_share(self) -> dict:
        values = [float(r.get("returns", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "returns",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_total(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "reviews",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_average(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "reviews",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_median(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "reviews",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_peak(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "reviews",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_floor(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "reviews",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_spread(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "reviews",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_count(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "reviews",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_reviews_share(self) -> dict:
        values = [float(r.get("reviews", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "reviews",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_total(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "searches",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_average(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "searches",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_median(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "searches",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_peak(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "searches",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_floor(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "searches",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_spread(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "searches",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_count(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "searches",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_searches_share(self) -> dict:
        values = [float(r.get("searches", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "searches",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_total(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "shipments",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_average(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "shipments",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_median(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "shipments",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_peak(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "shipments",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_floor(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "shipments",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_spread(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "shipments",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_count(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "shipments",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_shipments_share(self) -> dict:
        values = [float(r.get("shipments", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "shipments",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_total(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "invoices",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_average(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "invoices",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_median(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "invoices",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_peak(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "invoices",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_floor(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "invoices",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_spread(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "invoices",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_count(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "invoices",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_invoices_share(self) -> dict:
        values = [float(r.get("invoices", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "invoices",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_total(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "payments",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_average(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "payments",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_median(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "payments",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_peak(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "payments",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_floor(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "payments",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_spread(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "payments",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_count(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "payments",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_payments_share(self) -> dict:
        values = [float(r.get("payments", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "payments",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_total(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "visits",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_average(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "visits",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_median(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "visits",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_peak(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "visits",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_floor(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "visits",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_spread(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "visits",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_count(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "visits",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_visits_share(self) -> dict:
        values = [float(r.get("visits", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "visits",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_total(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "bounces",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_average(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "bounces",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_median(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "bounces",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_peak(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "bounces",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_floor(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "bounces",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_spread(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "bounces",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_count(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "bounces",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_bounces_share(self) -> dict:
        values = [float(r.get("bounces", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "bounces",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_total(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values)
        return {
            "metric": "clicks",
            "aggregate": "total",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_average(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = mean(values) if values else 0.0
        return {
            "metric": "clicks",
            "aggregate": "average",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_median(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = median(values) if values else 0.0
        return {
            "metric": "clicks",
            "aggregate": "median",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_peak(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = max(values, default=0.0)
        return {
            "metric": "clicks",
            "aggregate": "peak",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_floor(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = min(values, default=0.0)
        return {
            "metric": "clicks",
            "aggregate": "floor",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_spread(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = (max(values) - min(values)) if values else 0.0
        return {
            "metric": "clicks",
            "aggregate": "spread",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_count(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = float(len(values))
        return {
            "metric": "clicks",
            "aggregate": "count",
            "value": round(result, 4),
            "rows": len(values),
        }

    def section_clicks_share(self) -> dict:
        values = [float(r.get("clicks", 0)) for r in self.rows]
        total = sum(values)
        result = sum(values) / total if total else 0.0
        return {
            "metric": "clicks",
            "aggregate": "share",
            "value": round(result, 4),
            "rows": len(values),
        }

    def build(self) -> list[dict]:
        return [
            self.section_revenue_total(),
            self.section_refunds_total(),
            self.section_signups_total(),
            self.section_latency_total(),
            self.section_carts_total(),
            self.section_coupons_total(),
            self.section_reviews_total(),
            self.section_shipments_total(),
            self.section_payments_total(),
            self.section_bounces_total(),
        ]
