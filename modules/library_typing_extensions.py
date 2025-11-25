from typing import Optional, Dict, List, Union, Any
from datetime import datetime
from dataclasses import dataclass
import statistics
from typing_extensions import (
    TypedDict,
    Literal,
    Final,
    Protocol,
    runtime_checkable,
    Annotated,
    Self,
    NotRequired,
    Required,
    TypeAlias,
    Generic
)

"""
typing_extensions backports newer typing features to older Python versions and provides additional type hints not available in the standard typing module.
"""


# ============================================================================
# 1. TypedDict - Structured dictionaries with type hints
# ============================================================================

class DataSourceConfig(TypedDict):
    """
    Configuration for a data source connection.
    
    TypedDict ensures dictionary keys are typed and documented.
    Useful for: API responses, config files, data validation.
    """
    host: str
    port: int
    database: str
    username: str
    password: str
    timeout: NotRequired[int]  # Optional field (Python 3.11+ feature)
    ssl_enabled: NotRequired[bool]


class MetricDefinition(TypedDict, total=False):
    """
    Define a business metric structure.
    
    total=False makes all fields optional by default.
    Use Required[] to mark specific fields as mandatory.
    """
    name: Required[str]
    formula: Required[str]
    description: str
    unit: str
    category: str


def create_database_connection(config: DataSourceConfig) -> Dict[str, Any]:
    """
    Example: Type-safe configuration handling.
    
    TypedDict provides autocomplete and type checking for dict keys.
    """
    return {
        "connection_string": f"{config['host']}:{config['port']}/{config['database']}",
        "credentials": (config["username"], config["password"]),
        "timeout": config.get("timeout", 30)
    }


# ============================================================================
# 2. Literal - Restrict values to specific literals
# ============================================================================

# Type alias for common report types
ReportFormat = Literal["csv", "json", "parquet", "excel", "pdf"]
AggregationType = Literal["sum", "avg", "count", "min", "max", "median"]
DataQualityStatus = Literal["passed", "failed", "warning", "skipped"]


def export_report(data: List[Dict], format: ReportFormat) -> str:
    """
    Export data in a specific format.
    
    Literal ensures only valid formats are passed.
    IDE will show autocomplete with valid options.
    Type checker catches invalid values at compile time.
    """
    match format:
        case "csv":
            return "data.csv"
        case "json":
            return "data.json"
        case "parquet":
            return "data.parquet"
        case "excel":
            return "data.xlsx"
        case "pdf":
            return "report.pdf"
        case _:
            raise ValueError(f"Unsupported report format: {format}")


def aggregate_metric(values: List[float], method: AggregationType) -> float:
    """
    Aggregate values using specified method.
    
    Literal prevents typos and invalid aggregation methods.
    """

    match method:
        case "sum":
            return sum(values)
        case "avg":
            return statistics.mean(values)
        case "count":
            return float(len(values))
        case "min":
            return min(values)
        case "max":
            return max(values)
        case "median":
            return statistics.median(values)
        case _:
            raise ValueError(f"Unsupported aggregation method: {method}")


# ============================================================================
# 3. Final - Immutable constants and variables
# ============================================================================

# Constants that should never be modified
MAX_RETRY_ATTEMPTS: Final = 3
DEFAULT_PAGE_SIZE: Final = 100
API_VERSION: Final = "v2"


@dataclass
class DataPipeline:
    """
    Data pipeline with immutable configuration.
    
    Final indicates values that shouldn't change after initialization.
    """
    name: str
    source: Final[str]  # Source cannot be changed after creation
    
    def __post_init__(self):
        # Type checker ensures this is not reassigned
        # self.source = "new_source"  # This would trigger a type error
        pass


# ============================================================================
# 4. Protocol - Structural subtyping (Duck typing with types)
# ============================================================================

@runtime_checkable
class DataSource(Protocol):
    """
    Protocol for any data source implementation.
    
    Protocols enable duck typing with type safety.
    Any class implementing these methods is considered a DataSource.
    
    @runtime_checkable allows isinstance() checks.
    """
    
    def start_connection(self) -> bool:
        ...
    
    def execute_query(self, sql: str) -> List[Dict[str, Any]]:
        ...
    
    def close_connection(self) -> None:
        ...


@runtime_checkable
class Transformer(Protocol):
    """Protocol for data transformation logic."""
    
    def transform(self, data: List[Dict]) -> List[Dict]:
        """Transform input data."""
        ...
    
    def validate(self, data: List[Dict]) -> DataQualityStatus:
        """Validate data quality."""
        ...


class PostgresDataSource:
    """
    Concrete implementation satisfying DataSource protocol.
    No explicit inheritance needed!
    """
    
    def start_connection(self) -> bool:
        return True
    
    def execute_query(self, sql: str) -> List[Dict[str, Any]]:
        return [{"id": 1, "value": "data"}]
    
    def close_connection(self) -> None:
        pass


def execute_etl(source: DataSource, transformer: Transformer) -> List[Dict]:
    """
    ETL pipeline accepting any compatible implementations.
    
    Works with any class implementing DataSource and Transformer protocols.
    Enables flexible, testable architecture.
    """
    source.start_connection()
    raw_data = source.execute_query("SELECT * FROM table")
    transformed = transformer.transform(raw_data)
    source.close_connection()
    return transformed


# ============================================================================
# 5. Annotated - Add metadata to types
# ============================================================================

# Annotated adds runtime metadata to types
UserId = Annotated[int, "Positive integer representing user ID"]
Revenue = Annotated[float, "USD", "Must be >= 0"]
EmailAddress = Annotated[str, "Valid email format"]
Percentage = Annotated[float, "Value between 0 and 100"]


class DataValidation:
    """
    Use Annotated for validation metadata.
    
    Third-party libraries (pydantic, etc.) can inspect these annotations
    for validation rules.
    """
    
    @staticmethod
    def validate_percentage(value: Percentage) -> bool:
        """Validate percentage is in valid range."""
        return 0 <= value <= 100
    
    @staticmethod
    def validate_revenue(value: Revenue) -> bool:
        """Validate revenue is non-negative."""
        return value >= 0


# ============================================================================
# 6. Self - Return type is the class itself
# ============================================================================

class QueryBuilder:
    """
    Fluent API using Self for method chaining.
    
    Self indicates method returns instance of the same class.
    Enables proper type inference in method chains.
    """
    
    def __init__(self) -> None:
        self.query_parts: List[str] = []
    
    def select(self, *columns: str) -> Self:
        """Add SELECT clause. Returns self for chaining."""
        self.query_parts.append(f"SELECT {', '.join(columns)}")
        return self
    
    def from_table(self, table: str) -> Self:
        """Add FROM clause. Returns self for chaining."""
        self.query_parts.append(f"FROM {table}")
        return self
    
    def where(self, condition: str) -> Self:
        """Add WHERE clause. Returns self for chaining."""
        self.query_parts.append(f"WHERE {condition}")
        return self
    
    def build(self) -> str:
        """Generate final query string."""
        return " ".join(self.query_parts)


# ============================================================================
# 7. TypeAlias - Explicit type aliases
# ============================================================================

# Complex type aliases for clarity
JSONData: TypeAlias = Dict[str, Union[str, int, float, List, Dict]]
DataFrame: TypeAlias = List[Dict[str, Any]]
MetricValue: TypeAlias = Union[int, float, None]
TimeSeries: TypeAlias = Dict[datetime, float]


def process_json_payload(payload: JSONData) -> DataFrame:
    """
    Process JSON with explicit type alias.
    
    TypeAlias makes complex types readable and reusable.
    """
    return [{"processed": True, "data": payload}]


def calculate_kpi(timeseries: TimeSeries) -> MetricValue:
    """
    Calculate KPI from time series data.
    
    Type aliases improve readability of complex signatures.
    """
    if not timeseries:
        return None
    return sum(timeseries.values()) / len(timeseries)


# ============================================================================
# PRACTICAL USAGE EXAMPLES
# ============================================================================

def main() -> None:
    """Demonstrate practical usage of typing_extensions features."""
    
    # TypedDict for configuration
    db_config: DataSourceConfig = {
        "host": "localhost",
        "port": 5432,
        "database": "analytics",
        "username": "analyst",
        "password": "secret",
        "timeout": 60,
    }
    
    # Literal for type-safe options
    report_file = export_report([{"sales": 1000}], "csv")
    metric = aggregate_metric([10.5, 20.3, 15.7], "avg")

    # Protocol for flexible architecture
    postgres = PostgresDataSource()
    if isinstance(postgres, DataSource):  # runtime_checkable enables this
        print("Valid data source")

    # Self for fluent APIs
    query = (QueryBuilder()
             .select("user_id", "revenue")
             .from_table("sales")
             .where("date >= '2024-01-01'")
             .build())
    print(query)
    
    # Annotated with validation
    user_conversion_rate: Percentage = 23.5
    annual_revenue: Revenue = 1_000_000.50
    
    print(f"Validation: {DataValidation.validate_percentage(user_conversion_rate)}")


if __name__ == "__main__":
    main()