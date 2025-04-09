from enum import Enum, auto


class ReportType(Enum):
    """
    Enum to represent different types of business intelligence reports.
    Using `auto()` ensures that values are automatically assigned and
    reduces the risk of human error when adding new report types.
    """

    SALES = auto()
    INVENTORY = auto()
    CUSTOMER_FEEDBACK = auto()
    FINANCIAL = auto()
    MARKETING = auto()


class ReportStatus(Enum):
    """
    Enum to represent the status of a report in the workflow.
    """

    DRAFT = auto()
    IN_REVIEW = auto()
    APPROVED = auto()
    PUBLISHED = auto()


def generate_report(report_type: ReportType, status: ReportStatus) -> str:
    """
    Simulates the generation of a report based on its type and status.

    Args:
        report_type (ReportType): The type of report to generate.
        status (ReportStatus): The current status of the report.

    Returns:
        str: A message indicating the report generation status.
    """

    if status == ReportStatus.DRAFT:
        return f"Generating a draft version of the {report_type.name.title()} report."
    elif status == ReportStatus.IN_REVIEW:
        return f"{report_type.name.title()} report is under review."
    elif status == ReportStatus.APPROVED:
        return f"{report_type.name.title()} report has been approved and is ready for publishing."
    elif status == ReportStatus.PUBLISHED:
        return f"{report_type.name.title()} report has been published."
    else:
        return "Invalid report status."


if __name__ == "__main__":
    # Generate a draft sales report
    print(generate_report(ReportType.SALES, ReportStatus.DRAFT))

    # Generate a report that is under review
    print(generate_report(ReportType.INVENTORY, ReportStatus.IN_REVIEW))

    # Generate an approved financial report
    print(generate_report(ReportType.FINANCIAL, ReportStatus.APPROVED))

    # Generate a published marketing report
    print(generate_report(ReportType.MARKETING, ReportStatus.PUBLISHED))
