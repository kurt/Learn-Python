"""
Tests for the StatQuest package
"""

import pytest
from statquest.main import hello_statquest, create_sample_data


def test_hello_statquest():
    """Test the hello function."""
    result = hello_statquest()
    assert isinstance(result, str)
    assert "StatQuest" in result


def test_create_sample_data():
    """Test sample data creation."""
    df = create_sample_data(50)
    assert len(df) == 50
    assert list(df.columns) == ['x', 'y', 'category']
    assert df['category'].nunique() <= 3


def test_create_sample_data_default():
    """Test sample data creation with default parameters."""
    df = create_sample_data()
    assert len(df) == 100
