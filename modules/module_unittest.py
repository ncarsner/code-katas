import unittest
from typing import List, Dict, Any
from datetime import datetime, timedelta

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