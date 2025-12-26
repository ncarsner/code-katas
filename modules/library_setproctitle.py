import setproctitle
import time
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

"""
The setproctitle library allows you to change your process title as it appears in system monitoring tools (ps, top, htop, etc.). This is invaluable for:
- Monitoring long-running ETL jobs
- Identifying which stage of a pipeline is executing
- Debugging hanging processes in production
- Resource monitoring and process management
"""


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def basic_process_title_example() -> None:
    """
    Basic example: Set a custom process title.

    Use Case: Quickly identify your script in system monitors.
    View with: ps aux | grep python
    """
    original_title = setproctitle.getproctitle()
    print(f"Original process title: {original_title}")

    # Set a descriptive title
    setproctitle.setproctitle("my_etl_pipeline")
    print(f"New process title: {setproctitle.getproctitle()}")

    time.sleep(2)

    # Restore original
    setproctitle.setproctitle(original_title)


def etl_pipeline_with_progress(data_sources: List[str], batch_size: int = 1000) -> None:
    """
    ETL pipeline that updates process title with current progress.

    Args:
        data_sources: List of data source identifiers to process
        batch_size: Number of records to process per batch

    Use Case: Monitor which data source is being processed in real-time.
    """
    base_title = "ETL Pipeline"
    total_sources = len(data_sources)

    for idx, source in enumerate(data_sources, 1):
        # Update process title with current stage
        progress = f"[{idx}/{total_sources}]"
        setproctitle.setproctitle(f"{base_title} {progress} Processing: {source}")

        logger.info(f"Processing {source}")
        # Simulate processing
        time.sleep(1)

        # Update with completion status
        setproctitle.setproctitle(f"{base_title} {progress} Completed: {source}")

    setproctitle.setproctitle(f"{base_title} - COMPLETE")


def data_warehouse_loader(
    table_name: str, record_count: int, update_interval: int = 100
) -> None:
    """
    Simulates loading data into a warehouse with progress tracking.

    Args:
        table_name: Target table name
        record_count: Total records to load
        update_interval: Update process title every N records

    Use Case: Track progress of large data loads in real-time.
    """
    base_title = f"DW Load: {table_name}"

    for i in range(0, record_count, update_interval):
        processed = min(i + update_interval, record_count)
        percent = (processed / record_count) * 100

        # Update title with progress percentage
        setproctitle.setproctitle(
            f"{base_title} - {processed:,}/{record_count:,} ({percent:.1f}%)"
        )

        # Simulate loading
        time.sleep(0.1)

    setproctitle.setproctitle(f"{base_title} - COMPLETE ✓")


def multi_stage_pipeline(stages: List[Dict[str, Any]]) -> None:
    """
    Multi-stage data pipeline with detailed status tracking.

    Args:
        stages: List of stage configurations with 'name' and 'duration' keys

    Use Case: Complex pipelines with multiple transformation stages.
    Example stages:
        [
            {'name': 'Extract from API', 'duration': 5},
            {'name': 'Transform & Validate', 'duration': 10},
            {'name': 'Load to Warehouse', 'duration': 8}
        ]
    """
    pipeline_name = "Data Pipeline"
    total_stages = len(stages)
    start_time = datetime.now()

    for idx, stage in enumerate(stages, 1):
        stage_name = stage.get("name", f"Stage {idx}")
        duration = stage.get("duration", 1)

        # Show current stage
        title = f"{pipeline_name} [{idx}/{total_stages}] {stage_name}"
        setproctitle.setproctitle(title)
        logger.info(f"Starting: {stage_name}")

        # Simulate stage execution with sub-progress
        for sec in range(duration):
            elapsed = (datetime.now() - start_time).seconds
            setproctitle.setproctitle(
                f"{title} - {sec + 1}s/{duration}s (Total: {elapsed}s)"
            )
            time.sleep(1)

    total_time = (datetime.now() - start_time).seconds
    setproctitle.setproctitle(f"{pipeline_name} - COMPLETE (Runtime: {total_time}s)")


def error_handling_example(simulate_error: bool = False) -> None:
    """
    Demonstrates error handling with process title updates.

    Args:
        simulate_error: Whether to simulate an error condition

    Use Case: Quickly identify failed jobs in production monitoring.
    """
    job_name = "Critical ETL Job"

    try:
        setproctitle.setproctitle(f"{job_name} - RUNNING")

        if simulate_error:
            raise ValueError("Simulated data validation error")

        time.sleep(2)
        setproctitle.setproctitle(f"{job_name} - SUCCESS ✓")

    except Exception as e:
        # Update title to show error state
        setproctitle.setproctitle(f"{job_name} - ERROR: {type(e).__name__}")
        logger.error(f"Job failed: {e}")
        raise


def parallel_worker_identifier(worker_id: int, task_name: str) -> None:
    """
    Identify individual workers in parallel processing scenarios.

    Args:
        worker_id: Unique identifier for this worker
        task_name: Description of the task being performed

    Use Case: When using multiprocessing, identify which worker is doing what.
    Great for debugging parallel ETL processes.
    """
    setproctitle.setproctitle(f"Worker-{worker_id}: {task_name}")
    logger.info(f"Worker {worker_id} processing {task_name}")
    time.sleep(2)


def real_world_bi_report_generator(
    report_name: str, query_complexity: str = "medium"
) -> None:
    """
    Realistic BI report generation with status tracking.

    Args:
        report_name: Name of the report being generated
        query_complexity: 'low', 'medium', or 'high' complexity

    Use Case: Track long-running report queries and generation processes.
    """
    base_title = f"BI Report: {report_name}"

    # Phase 1: Query execution
    setproctitle.setproctitle(f"{base_title} - Executing Query")
    time.sleep(2)

    # Phase 2: Data processing
    setproctitle.setproctitle(f"{base_title} - Processing Results")
    time.sleep(1)

    # Phase 3: Report generation
    setproctitle.setproctitle(f"{base_title} - Generating Report")
    time.sleep(1)

    # Phase 4: Complete
    setproctitle.setproctitle(f"{base_title} - Ready for Download")


if __name__ == "__main__":
    """
    To monitor in real-time, open another terminal and run:
    - Linux/Mac: watch -n 1 'ps aux | grep python'
    - Or use: htop (filter by 'python')
    """

    print("Running setproctitle examples...")
    print("Open another terminal and run: ps aux | grep python\n")

    # Example 1: Basic usage
    print("1. Basic process title example")
    basic_process_title_example()
    time.sleep(1)

    # Example 2: ETL with progress
    print("\n2. ETL pipeline with progress tracking")
    etl_pipeline_with_progress(["sales_db", "inventory_db", "customer_db"])
    time.sleep(1)

    # Example 3: Data warehouse loading
    print("\n3. Data warehouse loader")
    data_warehouse_loader("fact_sales", 1000, update_interval=100)
    time.sleep(1)

    # Example 4: Multi-stage pipeline
    print("\n4. Multi-stage pipeline")
    stages = [
        {"name": "Extract from API", "duration": 3},
        {"name": "Transform Data", "duration": 2},
        {"name": "Load to DW", "duration": 2},
    ]
    multi_stage_pipeline(stages)

    print("\n✓ All examples complete!")
