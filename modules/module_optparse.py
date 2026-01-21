from optparse import OptionParser, OptionGroup
from typing import Tuple

"""
Demonstration of Python's optparse module for command-line argument parsing.

Note: optparse is deprecated since Python 3.2 in favor of argparse.
This module is shown for legacy code understanding purposes.

For new projects, use argparse instead.
"""


def create_data_pipeline_parser() -> OptionParser:
    """
    Create an OptionParser for a data pipeline script.

    Returns:
        OptionParser: Configured parser with data pipeline options
    """
    usage = "usage: %prog [options] input_file output_file"
    parser = OptionParser(usage=usage, version="%prog 1.0")

    # Basic options
    parser.add_option(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="Enable verbose output for debugging",
    )

    parser.add_option(
        "-q",
        "--quiet",
        action="store_false",
        dest="verbose",
        help="Disable verbose output",
    )

    # String options for configuration
    parser.add_option(
        "-c",
        "--config",
        type="string",
        dest="config_file",
        default="config.yml",
        help="Path to configuration file [default: %default]",
        metavar="FILE",
    )

    parser.add_option(
        "-f",
        "--format",
        type="choice",
        choices=["csv", "json", "parquet", "excel"],
        dest="output_format",
        default="csv",
        help="Output format: csv, json, parquet, or excel [default: %default]",
    )

    # Integer options for performance tuning
    parser.add_option(
        "-b",
        "--batch-size",
        type="int",
        dest="batch_size",
        default=1000,
        help="Number of records to process per batch [default: %default]",
    )

    parser.add_option(
        "-t",
        "--threads",
        type="int",
        dest="num_threads",
        default=4,
        help="Number of parallel threads [default: %default]",
    )

    # Float option for sampling
    parser.add_option(
        "-s",
        "--sample-rate",
        type="float",
        dest="sample_rate",
        default=1.0,
        help="Data sampling rate (0.0-1.0) [default: %default]",
    )

    # Store action - default behavior
    parser.add_option(
        "-d", "--database", dest="database_name", help="Database name for connection"
    )

    # Count action - useful for verbosity levels
    parser.add_option(
        "-V",
        action="count",
        dest="verbosity_level",
        default=0,
        help="Increase verbosity (can be repeated: -VVV)",
    )

    # Append action - for multiple values
    parser.add_option(
        "-e",
        "--exclude",
        action="append",
        dest="exclude_columns",
        default=[],
        help="Column to exclude (can be used multiple times)",
    )

    # Option groups for better organization
    etl_group = OptionGroup(
        parser, "ETL Options", "Options specific to Extract, Transform, Load operations"
    )

    etl_group.add_option(
        "--extract-mode",
        type="choice",
        choices=["full", "incremental", "delta"],
        dest="extract_mode",
        default="full",
        help="Data extraction mode [default: %default]",
    )

    etl_group.add_option(
        "--transform-sql",
        dest="transform_sql",
        help="SQL file for transformation logic",
        metavar="FILE",
    )

    etl_group.add_option(
        "--skip-validation",
        action="store_true",
        dest="skip_validation",
        default=False,
        help="Skip data quality validation",
    )

    parser.add_option_group(etl_group)

    # Database connection group
    db_group = OptionGroup(parser, "Database Connection Options")

    db_group.add_option(
        "--db-host",
        dest="db_host",
        default="localhost",
        help="Database host [default: %default]",
    )

    db_group.add_option(
        "--db-port",
        type="int",
        dest="db_port",
        default=5432,
        help="Database port [default: %default]",
    )

    db_group.add_option("--db-user", dest="db_user", help="Database username")

    parser.add_option_group(db_group)

    return parser


def validate_options(options, args: list) -> Tuple[bool, str]:
    """
    Validate parsed options and arguments.

    Args:
        options: Parsed options object from OptionParser
        args: Remaining positional arguments

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check required positional arguments
    if len(args) < 2:
        return False, "Error: Missing required input_file and output_file arguments"

    # Validate sample rate range
    if not 0.0 <= options.sample_rate <= 1.0:
        return False, "Error: Sample rate must be between 0.0 and 1.0"

    # Validate batch size
    if options.batch_size <= 0:
        return False, "Error: Batch size must be positive"

    # Validate threads
    if options.num_threads <= 0:
        return False, "Error: Number of threads must be positive"

    return True, ""


def main():
    """
    Main function demonstrating optparse usage in a BI/data engineering context.
    """
    # Create and configure parser
    parser = create_data_pipeline_parser()

    # Parse command line arguments
    (options, args) = parser.parse_args()

    # Validate options
    is_valid, error_msg = validate_options(options, args)
    if not is_valid:
        parser.error(error_msg)

    # Extract positional arguments
    input_file = args[0]
    output_file = args[1]

    # Display parsed configuration
    print("=" * 60)
    print("Data Pipeline Configuration")
    print("=" * 60)
    print(f"Input File:        {input_file}")
    print(f"Output File:       {output_file}")
    print(f"Output Format:     {options.output_format}")
    print(f"Config File:       {options.config_file}")
    print(f"Verbose Mode:      {options.verbose}")
    print(f"Verbosity Level:   {options.verbosity_level}")
    print(f"Batch Size:        {options.batch_size}")
    print(f"Threads:           {options.num_threads}")
    print(f"Sample Rate:       {options.sample_rate}")
    print(f"Extract Mode:      {options.extract_mode}")
    print(f"Skip Validation:   {options.skip_validation}")

    if options.database_name:
        print(f"Database:          {options.database_name}")

    if options.exclude_columns:
        print(f"Excluded Columns:  {', '.join(options.exclude_columns)}")

    if options.transform_sql:
        print(f"Transform SQL:     {options.transform_sql}")

    print(f"\nDatabase Connection:")
    print(f"  Host:            {options.db_host}")
    print(f"  Port:            {options.db_port}")
    if options.db_user:
        print(f"  User:            {options.db_user}")

    print("=" * 60)

    # Your actual data pipeline logic would go here
    if options.verbose:
        print("\n[DEBUG] Starting data pipeline execution...")


if __name__ == "__main__":
    # Example usage (comment out main() and uncomment these for testing):
    # sys.argv = [
    #     'module_optparse.py',
    #     '-v', '-VVV',
    #     '--format', 'parquet',
    #     '--batch-size', '5000',
    #     '--exclude', 'id',
    #     '--exclude', 'timestamp',
    #     '--extract-mode', 'incremental',
    #     '--db-host', 'prod-server.company.com',
    #     '--db-user', 'analyst',
    #     'sales_data.csv',
    #     'output/sales_processed.parquet'
    # ]
    main()
