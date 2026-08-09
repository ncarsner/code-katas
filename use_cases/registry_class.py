"""Registry pattern examples for API routing and BI data pulls.

What this does:
  A registry is an approved-name-to-function lookup. ``data_pullers`` maps a
  source name, such as ``warehouse`` or ``salesforce``, to the function that
  knows how to pull that source's metrics. ``run_daily_report`` receives the
  configured source name and date, finds its function, and runs it. Adding a
  source means registering one function; no central if/elif dispatcher changes.

How to run this example manually:
  From the repository root, run ``python3 use_cases/registry_class.py``.
  It only prints sample data. It makes no database or API connection and writes
  no report. Call ``run_daily_report("warehouse", "YYYY-MM-DD")`` from a
  notebook, script, or application to test a selected source.

Schedule and triggers:
  This file has no scheduler and does not run by itself. The ``__main__`` block
  runs only when someone invokes the command above. In production, an
  orchestrator such as Airflow, Dagster, a cloud scheduler, or cron would call
  ``run_daily_report`` on its schedule. A manual backfill, a report request, or
  an API endpoint could call the same function with a chosen date.

Production environment:
  Treat this module as application code deployed with the reporting job, often
  in a container or managed job runner. Store source credentials and connection
  details in the platform's secret manager or environment variables, never in
  this file. Replace the sample pull functions with authenticated queries and
  add logging, retries, validation, and a destination for the report output.
"""


class Registry:
  """Map approved names to functions, classes, or other objects."""

  def __init__(self, name):
    self.name = name
    self._registry = {}

  def register(self, key):
    def decorator(obj):
      if key in self._registry:
        raise KeyError(f"{key!r} is already registered in {self.name!r}")
      self._registry[key] = obj
      return obj
    return decorator

  def get(self, key):
    if key not in self._registry:
      raise KeyError(
        f"{key!r} not found in {self.name!r}. "
        f"Available: {list(self._registry)}"
      )
    return self._registry[key]

  def __contains__(self, key):
    return key in self._registry

  def keys(self):
    return self._registry.keys()


# API design: choose a serializer from an accepted request format.
response_serializers = Registry("response serializers")


@response_serializers.register("json")
def serialize_json(customer):
  return {"id": customer["id"], "name": customer["name"]}


@response_serializers.register("csv")
def serialize_csv(customer):
  return f'{customer["id"]},{customer["name"]}'


def build_customer_response(customer, requested_format):
  """An API controller can call this after validating requested_format."""
  serializer = response_serializers.get(requested_format)
  return serializer(customer)


# Business intelligence: schedule configuration selects a data source.
data_pullers = Registry("BI data pullers")


@data_pullers.register("salesforce")
def pull_salesforce_metrics(report_date):
  # Replace with the Salesforce query in production.
  return {"source": "salesforce", "date": report_date, "leads": 42}


@data_pullers.register("warehouse")
def pull_warehouse_metrics(report_date):
  # Replace with the warehouse query in production.
  return {"source": "warehouse", "date": report_date, "orders": 318}


def run_daily_report(source_name, report_date):
  """A scheduled job can pick its source from configuration, not conditionals."""
  pull_metrics = data_pullers.get(source_name)
  return pull_metrics(report_date)


if __name__ == "__main__":
  customer = {"id": 7, "name": "Avery"}
  print(build_customer_response(customer, "json"))
  print(run_daily_report("warehouse", "2026-08-05"))
