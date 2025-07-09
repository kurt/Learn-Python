import lightning as L
import matplotlib.pyplot as plt
import seaborn as sns
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD
from torch.utils.data import DataLoader, TensorDataset


class myNN(L.LightningModule):

    def __init__(self):
        """
        A simple neural network with three parameters.
        """
        super().__init__()

        self.w1 = nn.Parameter(torch.tensor(0.06))
        self.b1 = nn.Parameter(torch.tensor(0.0))

        self.w2 = nn.Parameter(torch.tensor(3.49))
        self.b2 = nn.Parameter(torch.tensor(0.0))

        self.w3 = nn.Parameter(torch.tensor(-4.11))
        self.w4 = nn.Parameter(torch.tensor(1.35))  # Added missing w4 parameter
        self.b3 = nn.Parameter(torch.tensor(2.74))

        self.loss = nn.MSELoss(reduction="sum")

    def forward(self, input_values):
        """
        Forward pass of the neural network.
        """
        top_x_axis_values = (input_values * self.w1) + self.b1
        bottom_x_axis_values = (input_values * self.w2) + self.b2

        top_y_axis_values = F.relu(top_x_axis_values)
        bottom_y_axis_values = F.relu(bottom_x_axis_values)

        output_values = (top_y_axis_values * self.w3) + (bottom_y_axis_values * self.w4)

        return output_values

    def configure_optimizers(self):
        """
        Configure the optimizer for training.
        """
        return SGD(self.parameters(), lr=0.01)

    def training_step(self, batch, batch_idx):
        """
        Training step for the neural network.
        """
        input_data, labels = batch
        output = self.forward(input_data)
        loss = self.loss(output, labels)
        self.log("train_loss", loss)
        return loss


if __name__ == "__main__":
    training_data = torch.tensor([0.0, 0.5, 1.0])
    training_labels = torch.tensor([0.0, 1.0, 0.0])

    training_dataset = TensorDataset(training_data, training_labels)
    dataloader = DataLoader(training_dataset)
    # Initialize the neural network
    model = myNN()

    trainer = L.Trainer(
        max_epochs=500,  # how many times to go through the training data
        logger=False,
        enable_checkpointing=False,
        enable_progress_bar=False,
    )

    trainer.fit(model, train_dataloaders=dataloader)

    ## Now that we've trained the model, let's print out the
    ## new values for each Weight and Bias.
    for name, param in model.named_parameters():
        print(name, torch.round(param.data, decimals=3))
    ## Create the different doses we want to run through the neural network.
    ## torch.linspace() creates the sequence of numbers between, and including, 0 and 1.
    input_doses = torch.linspace(start=0, end=1, steps=11)

    # now print out the doses to make sure they are what we expect...
    input_doses
    output_values = model(input_doses)
    torch.round(output_values, decimals=2)
    ## First, set the style for seaborn so that the graph looks cool.
    sns.set(style="whitegrid")

    ## First, draw the individual output points
    sns.scatterplot(
        x=input_doses, y=output_values.detach().numpy(), color="green", s=200
    )

    ## Now connect those points with a line
    sns.lineplot(
        x=input_doses,
        y=output_values.detach().numpy(),  ## NOTE: We call .detatch() because...
        color="green",
        linewidth=2.5,
    )

    ## Add the values in the training dataset
    sns.scatterplot(x=training_data, y=training_labels, color="orange", s=200)

    ## now label the y- and x-axes.
    plt.ylabel("Effectiveness")
    plt.xlabel("Dose")
    plt.show()
