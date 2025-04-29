import json


class JsonRenderer:
    def __init__(self, data: dict):
        """
        Initialize the JsonRenderer with a dictionary.

        Args:
            data (dict): The data to render as JSON.
        """
        self.data = data

    def render(self) -> str:
        """
        Public method to render the JSON.

        Returns:
            str: The rendered JSON string.
        """
        return self.__render_json()

    def __render_json(self) -> str:
        """
        Private method to render the JSON.

        Returns:
            str: The JSON string representation of the data.
        """
        return json.dumps(self.data, indent=4)


# Example for a BI developer/analyst
"""
{
    "Render JSON Data": {
        "prefix": "renderJson",
        "body": [
            "sales_data = {",
            "    \"region\": \"${1:Region}\",",
            "    \"total_revenue\": ${2:1000000},",
            "    \"top_products\": [",
            "        {\"name\": \"${3:Product A}\", \"revenue\": ${4:500000}},",
            "        {\"name\": \"${5:Product B}\", \"revenue\": ${6:300000}},",
            "        {\"name\": \"${7:Product C}\", \"revenue\": ${8:200000}}",
            "    ],",
            "    \"quarter\": \"${9:Q1}\",",
            "    \"year\": ${10:2023}",
            "}",
            "",
            "renderer = JsonRenderer(sales_data)",
            "print(\"\\nSales Data Report (JSON):\")",
            "print(renderer.render())"
        ],
        "description": "Render a JSON data report using the JsonRenderer class"
    }
}
"""

# Snippet example
sales_data = {
    "region": "North America",
    "total_revenue": 1500000,
    "top_products": [
        {"name": "Product A", "revenue": 700000},
        {"name": "Product B", "revenue": 500000},
        {"name": "Product C", "revenue": 300000},
    ],
    "quarter": "Q2",
    "year": 2023,
}

renderer = JsonRenderer(sales_data)
print("\nSales Data Report (JSON):")
print(renderer.render())
