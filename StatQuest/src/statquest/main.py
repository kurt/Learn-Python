"""
Example module for StatQuest learning
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F


class myNN(nn.Module):
    """a simple neural network model for demonstration purposes"""

    def __init__(self):
        super().__init__()

        self.w1 = torch.tensor(1.43)
        self.b1 = torch.tensor(-0.61)

        self.w2 = torch.tensor(2.63)
        self.b2 = torch.tensor(-0.27)

        self.w3 = torch.tensor(-3.89)
        self.w4 = torch.tensor(1.35)

    def forward(self, input_values: torch.Tensor) -> torch.Tensor:
        """Forward pass of the model.
        https://colab.research.google.com/github/StatQuest/signa/blob/main/chapter_01/chapter_01_basic_nn_in_pytorch.ipynb#scrollTo=948c0fb9-cdf6-48dd-9673-22767064eb3d
        Args:
            x: Input tensor
        Returns:
            Output tensor after applying the model's layers
        """
        ## The forward() method is called by default when we pass
        ## values to an object created from this class.
        ## This is where we do the math associated with running
        ## data through the neural network.

        top_x_axis_values = (input_values * self.w1) + self.b1
        bottom_x_axis_values = (input_values * self.w2) + self.b2

        top_y_axis_values = F.relu(top_x_axis_values)
        bottom_y_axis_values = F.relu(bottom_x_axis_values)

        output_values = (top_y_axis_values * self.w3) + (bottom_y_axis_values * self.w4)

        return output_values


def hello_statquest() -> str:
    """
    A simple hello function for testing.

    Returns:
        str: A greeting message
    """
    return "Hello, StatQuest! Ready to learn some statistics and machine learning!"


def create_sample_data(n_samples: int = 100) -> pd.DataFrame:
    """
    Create sample data for analysis.

    Args:
        n_samples: Number of samples to generate

    Returns:
        pd.DataFrame: Sample dataset
    """
    np.random.seed(42)
    data = {
        "x": np.random.normal(0, 1, n_samples),
        "y": np.random.normal(0, 1, n_samples),
        "category": np.random.choice(["A", "B", "C"], n_samples),
    }
    return pd.DataFrame(data)


def plot_sample_data(df: pd.DataFrame) -> None:
    """
    Create a simple scatter plot of the sample data.

    Args:
        df: DataFrame with x, y, and category columns
    """
    plt.figure(figsize=(8, 6))
    for category in df["category"].unique():
        mask = df["category"] == category
        plt.scatter(df[mask]["x"], df[mask]["y"], label=category, alpha=0.7)

    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Sample Data Visualization")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    # Example usage
    print(hello_statquest())

    # Create and plot sample data
    sample_df = create_sample_data(150)
    print(f"Created dataset with {len(sample_df)} rows")
    print(sample_df.head())

    # Uncomment to show plot
    # plot_sample_data(sample_df)
