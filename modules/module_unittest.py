import unittest
from unittest.mock import Mock, MagicMock, patch, call
from typing import List, Dict, Any
from datetime import datetime

"""
Practical unittest examples for BI/Data Engineering workflows. Demonstrates common testing patterns for data pipeline validation, ETL operations, and data quality checks.
"""



class DataValidator:
    """Utility class for validating data quality in pipelines."""
    
    def validate_numeric_range(
        self, 
        value: float, 
        min_val: float, 
        max_val: float
    ) -> bool:
        """Check if numeric value falls within acceptable range."""
        return min_val <= value <= max_val
    
    def validate_required_columns(
        self, 
        data: Dict[str, Any], 
        required_cols: List[str]
    ) -> bool:
        """Ensure all required columns exist in dataset."""
        return all(col in data for col in required_cols)
    
    def calculate_business_metric(self, revenue: float, cost: float) -> float:
        """Calculate profit margin percentage."""
        if cost == 0:
            raise ValueError("Cost cannot be zero")
        return ((revenue - cost) / cost) * 100


class TestDataValidator(unittest.TestCase):
    """Test suite for DataValidator class - demonstrates setUp/tearDown."""
    
    def setUp(self) -> None:
        """Initialize test fixtures before each test method."""
        self.validator = DataValidator()
        self.sample_data = {
            "customer_id": 12345,
            "amount": 1500.50,
            "date": "2024-01-15"
        }
    
    def tearDown(self) -> None:
        """Clean up after each test (useful for DB connections, file cleanup)."""
        # In real scenarios: close database connections, remove temp files
        pass
    
    def test_numeric_range_valid(self) -> None:
        """Test numeric validation with valid input."""
        result = self.validator.validate_numeric_range(50, 0, 100)
        self.assertTrue(result)
    
    def test_numeric_range_invalid(self) -> None:
        """Test numeric validation with out-of-range input."""
        result = self.validator.validate_numeric_range(150, 0, 100)
        self.assertFalse(result)
    
    def test_required_columns_present(self) -> None:
        """Test column validation when all required columns exist."""
        required = ["customer_id", "amount"]
        result = self.validator.validate_required_columns(
            self.sample_data, 
            required
        )
        self.assertTrue(result)
    
    def test_required_columns_missing(self) -> None:
        """Test column validation when required column is missing."""
        required = ["customer_id", "missing_column"]
        result = self.validator.validate_required_columns(
            self.sample_data, 
            required
        )
        self.assertFalse(result)
    
    def test_profit_margin_calculation(self) -> None:
        """Test business metric calculation with expected result."""
        result = self.validator.calculate_business_metric(
            revenue=10000, 
            cost=8000
        )
        self.assertAlmostEqual(result, 25.0, places=2)
    
    def test_profit_margin_zero_cost_raises_error(self) -> None:
        """Test error handling when cost is zero."""
        with self.assertRaises(ValueError):
            self.validator.calculate_business_metric(10000, 0)


class TestDataValidatorIntegration(unittest.TestCase):
    """Integration tests for multi-step data workflows."""
    
    def test_complete_data_pipeline_validation(self) -> None:
        """Test end-to-end validation of a data record."""
        validator = DataValidator()
        record = {"customer_id": 100, "revenue": 5000, "cost": 4000}
        
        # Validate structure
        self.assertTrue(
            validator.validate_required_columns(
                record, 
                ["customer_id", "revenue", "cost"]
            )
        )
        
        # Validate values
        self.assertTrue(
            validator.validate_numeric_range(record["revenue"], 0, 10000)
        )
        
        # Calculate metric
        margin = validator.calculate_business_metric(
            record["revenue"], 
            record["cost"]
        )
        self.assertGreater(margin, 0)


class ExternalDataService:
    """Simulates an external data service (API, database, etc)."""
    
    def fetch_customer_data(self, customer_id: int) -> Dict[str, Any]:
        """Fetch customer data from external service."""
        # In real scenario, this would hit an actual API
        return {}
    
    def log_transaction(self, transaction_id: str) -> bool:
        """Record transaction in external system."""
        return False


class DataProcessor:
    """Processes data using external services."""
    
    def __init__(self, service: ExternalDataService):
        self.service = service
    
    def enrich_customer_record(self, customer_id: int) -> Dict[str, Any]:
        """Enrich customer data from external service."""
        external_data = self.service.fetch_customer_data(customer_id)
        return {
            "id": customer_id,
            "external_info": external_data
        }
    
    def process_transaction(self, trans_id: str, amount: float) -> bool:
        """Process transaction and log it."""
        if amount > 0:
            return self.service.log_transaction(trans_id)
        return False


class TestMockBasics(unittest.TestCase):
    """Demonstrate basic Mock object creation and configuration."""
    
    def test_mock_basic_creation(self) -> None:
        """Create a simple Mock object and verify method calls."""
        # Create a mock object
        mock_service = Mock()
        
        # Configure return value for a method
        mock_service.fetch_data.return_value = {"id": 1, "name": "John"}
        
        # Use the mock
        result = mock_service.fetch_data(123)
        
        # Verify it was called and returns expected value
        self.assertEqual(result, {"id": 1, "name": "John"})
        mock_service.fetch_data.assert_called_once_with(123)
    
    def test_mock_multiple_calls(self) -> None:
        """Track multiple calls to mock methods."""
        mock_db = Mock()
        
        # Simulate database operations
        mock_db.query.return_value = [{"id": 1}, {"id": 2}]
        
        # Make multiple calls
        mock_db.query("SELECT *")
        mock_db.query("SELECT * WHERE active=true")
        
        # Verify calls were made as expected
        self.assertEqual(mock_db.query.call_count, 2)
        mock_db.query.assert_called_with("SELECT * WHERE active=true")
    
    def test_mock_call_arguments(self) -> None:
        """Verify exact sequence of mock method calls."""
        mock_api = Mock()
        
        # Make calls with different arguments
        mock_api.post("endpoint1", data="test1")
        mock_api.post("endpoint2", data="test2")
        
        # Verify all calls in order
        expected_calls = [
            call("endpoint1", data="test1"),
            call("endpoint2", data="test2")
        ]
        mock_api.post.assert_has_calls(expected_calls)


class TestMockWithDependencies(unittest.TestCase):
    """Demonstrate mocking dependencies in classes."""
    
    def test_processor_with_mocked_service(self) -> None:
        """Mock external service dependency for isolated testing."""
        # Create mock service
        mock_service = Mock(spec=ExternalDataService)
        mock_service.fetch_customer_data.return_value = {
            "subscription": "premium",
            "credits": 1000
        }
        
        # Inject mock into processor
        processor = DataProcessor(mock_service)
        
        # Use processor with mocked service
        result = processor.enrich_customer_record(42)
        
        # Verify behavior
        self.assertEqual(result["id"], 42)
        self.assertIn("external_info", result)
        mock_service.fetch_customer_data.assert_called_once_with(42)
    
    def test_transaction_processing_success(self) -> None:
        """Test transaction processing with successful service call."""
        mock_service = Mock(spec=ExternalDataService)
        mock_service.log_transaction.return_value = True
        
        processor = DataProcessor(mock_service)
        result = processor.process_transaction("TXN001", 99.99)
        
        self.assertTrue(result)
        mock_service.log_transaction.assert_called_once_with("TXN001")
    
    def test_transaction_processing_negative_amount(self) -> None:
        """Test that service is not called for invalid transactions."""
        mock_service = Mock(spec=ExternalDataService)
        
        processor = DataProcessor(mock_service)
        result = processor.process_transaction("TXN002", -50.0)
        
        self.assertFalse(result)
        # Verify service was never called
        mock_service.log_transaction.assert_not_called()


class TestMockWithPatch(unittest.TestCase):
    """Demonstrate patch decorator and context manager for mocking."""
    
    @patch('datetime.datetime')
    def test_patch_datetime_decorator(self, mock_datetime) -> None:
        """Use patch decorator to mock datetime module."""
        # Configure mock
        mock_datetime.now.return_value = datetime(2024, 1, 15, 10, 30, 0)
        
        # Use the mocked datetime
        result = datetime.now()
        
        # Verify mock was used
        self.assertEqual(result.year, 2024)
        self.assertEqual(result.month, 1)
        mock_datetime.now.assert_called_once()
    
    def test_patch_with_context_manager(self) -> None:
        """Use patch as context manager for temporary mocking."""
        with patch.object(ExternalDataService, 'fetch_customer_data') as mock_fetch:
            mock_fetch.return_value = {"status": "active"}
            
            # Create service and call method
            service = ExternalDataService()
            result = service.fetch_customer_data(123)
            
            # Verify mocking worked
            self.assertEqual(result["status"], "active")
            mock_fetch.assert_called_once_with(123)


class TestMagicMock(unittest.TestCase):
    """Demonstrate MagicMock for mocking special methods and complex behavior."""
    
    def test_magic_mock_iteration(self) -> None:
        """MagicMock supports iteration and other special methods."""
        mock_iterator = MagicMock()
        mock_iterator.__iter__.return_value = iter([1, 2, 3])
        
        # Can iterate over magic mock
        result = list(mock_iterator)
        
        self.assertEqual(result, [1, 2, 3])
    
    def test_magic_mock_context_manager(self) -> None:
        """MagicMock can simulate context manager protocol."""
        mock_file = MagicMock()
        mock_file.read.return_value = "file contents"
        
        # Use as context manager
        with mock_file as f:
            content = f.read()
        
        self.assertEqual(content, "file contents")
        mock_file.__enter__.assert_called_once()
        mock_file.__exit__.assert_called_once()
    
    def test_magic_mock_arithmetic(self) -> None:
        """MagicMock supports arithmetic operations."""
        mock_number = MagicMock()
        mock_number.__add__.return_value = 15
        
        # Perform arithmetic operation
        result = mock_number + 5
        
        self.assertEqual(result, 15)
        mock_number.__add__.assert_called_once_with(5)


class TestMockSideEffects(unittest.TestCase):
    """Demonstrate side effects and exception handling with mocks."""
    
    def test_side_effect_exception(self) -> None:
        """Configure mock to raise exception on call."""
        mock_api = Mock()
        mock_api.connect.side_effect = ConnectionError("Network unavailable")
        
        # Verify exception is raised
        with self.assertRaises(ConnectionError):
            mock_api.connect()
    
    def test_side_effect_sequence(self) -> None:
        """Configure mock to return different values for successive calls."""
        mock_sensor = Mock()
        # First call returns 20, second returns 25, third raises error
        mock_sensor.read_temperature.side_effect = [20, 25, ValueError("Sensor malfunction")]
        
        # First call
        temp1 = mock_sensor.read_temperature()
        self.assertEqual(temp1, 20)
        
        # Second call
        temp2 = mock_sensor.read_temperature()
        self.assertEqual(temp2, 25)
        
        # Third call raises exception
        with self.assertRaises(ValueError):
            mock_sensor.read_temperature()
    
    def test_side_effect_callable(self) -> None:
        """Configure mock with callable side effect for custom behavior."""
        mock_processor = Mock()
        
        def process_logic(x):
            return x * 2 if x > 0 else 0
        
        mock_processor.transform.side_effect = process_logic
        
        # Use mock with custom logic
        self.assertEqual(mock_processor.transform(5), 10)
        self.assertEqual(mock_processor.transform(-5), 0)


class TestMockAttributes(unittest.TestCase):
    """Demonstrate accessing and configuring mock attributes."""
    
    def test_mock_attribute_access(self) -> None:
        """Access attributes on mock objects."""
        mock_config = Mock()
        mock_config.database.host = "localhost"
        mock_config.database.port = 5432
        
        self.assertEqual(mock_config.database.host, "localhost")
        self.assertEqual(mock_config.database.port, 5432)
    
    def test_mock_attribute_assertions(self) -> None:
        """Verify attributes were accessed."""
        mock_logger = Mock()
        mock_logger.level = "INFO"
        
        # Verify the attribute value
        self.assertEqual(mock_logger.level, "INFO")
    
    def test_configure_multiple_return_values(self) -> None:
        """Configure different return values for chained calls."""
        mock_chain = Mock()
        mock_chain.get_user.return_value.get_profile.return_value = {
            "name": "Alice",
            "role": "admin"
        }
        
        result = mock_chain.get_user(1).get_profile()
        
        self.assertEqual(result["name"], "Alice")
        self.assertEqual(result["role"], "admin")


class TestSuiteRunner(unittest.TestCase):
    """Demonstrates parameterized testing for multiple datasets."""
    
    @unittest.skip("Skipping to demonstrate skip functionality")
    def test_deprecated_function(self) -> None:
        """This test is skipped (useful for WIP or deprecated features)."""
        pass
    
    @unittest.skipIf(
        datetime.now().month == 2, 
        "Skipping February data tests"
    )
    def test_seasonal_data_validation(self) -> None:
        """Skip this test under specific conditions."""
        self.assertTrue(True)


def run_specific_test_class(test_class: type) -> None:
    """Utility to run a single test class programmatically."""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    # Run all tests in this module with detailed output
    unittest.main(verbosity=2)