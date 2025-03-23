from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class JobStatus:
    job_name: str
    start_time: datetime
    end_time: datetime = None
    success: bool = False

    @property
    def duration(self) -> float:
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0

    @duration.setter
    def duration(self, value: float):
        raise AttributeError("Duration is a read-only property")


@dataclass
class PipelineJob:
    job_name: str
    status: JobStatus = field(
        default_factory=lambda: JobStatus(job_name="", start_time=datetime.now())
    )

    def start(self):
        self.status.start_time = datetime.now()
        self.status.success = False
        print(f"Job {self.job_name} started at {self.status.start_time}")

    def end(self, success: bool):
        self.status.end_time = datetime.now()
        self.status.success = success
        print(
            f"Job {self.job_name} ended at {self.status.end_time} with success={self.status.success}"
        )


@dataclass
class DataPipeline:
    pipeline_name: str
    jobs: List[PipelineJob] = field(default_factory=list)

    @property
    def is_successful(self) -> bool:
        return all(job.status.success for job in self.jobs)

    @property
    def total_duration(self) -> float:
        return sum(job.status.duration for job in self.jobs)

    def add_job(self, job: PipelineJob):
        self.jobs.append(job)
        print(f"Job {job.job_name} added to pipeline {self.pipeline_name}")


# Example usage
pipeline = DataPipeline(pipeline_name="Daily ETL Pipeline")

job1 = PipelineJob(job_name="Extract Data")
job2 = PipelineJob(job_name="Transform Data")
job3 = PipelineJob(job_name="Load Data")

pipeline.add_job(job1)
pipeline.add_job(job2)
pipeline.add_job(job3)

job1.start()
# Simulate job duration
job1.end(success=True)

job2.start()
# Simulate job duration
job2.end(success=True)

job3.start()
# Simulate job duration
job3.end(success=False)

print(f"Pipeline {pipeline.pipeline_name} success: {pipeline.is_successful}")
print(f"Total pipeline duration: {pipeline.total_duration} seconds")
