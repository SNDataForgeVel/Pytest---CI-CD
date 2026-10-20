from pathlib import Path

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,inline

from CommonLib import FilterRows


@pytest.fixture(scope="module")
def spark():
    session = (
        SparkSession.builder
        .appName("test-commonlib")
        .getOrCreate()
    )
    yield session
    session.stop()


def test_filterrows_removes_null_product_names_from_sample(spark):
    sample_file = (
        Path(__file__).resolve().parents[1]
        / "SampleFile"
        / "Products_Formatted.json"
    )

    raw = spark.read.option("multiLine", True).json(str(sample_file))
    products = (
        raw.select(inline(col("Products")))
    )
    result = FilterRows(products, "ProductId", "NULL", "==")
    print(result.count)
    assert result.filter(col("ProductId").isNull()).count() == 0