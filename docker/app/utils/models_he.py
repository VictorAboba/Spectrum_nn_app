from torch import nn
import torch


class ModelCNN(nn.Module):
    def __init__(self, p1, p2, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cnn = nn.Sequential(
            nn.Conv1d(1, 4, 3, padding="same"),
            nn.Conv1d(4, 16, 3, padding="same"),
            nn.MaxPool1d(2, 2),
            nn.Conv1d(16, 64, 3, padding="same"),
            nn.Conv1d(64, 256, 3, padding="same"),
            nn.MaxPool1d(2, 2),
            nn.BatchNorm1d(256),
            nn.Dropout(p1),
            nn.Flatten(),
        )
        self.output = nn.Sequential(
            nn.Linear(256 * 5, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(p2),
            nn.Linear(256, 26),
        )

    def forward(self, x):
        x = torch.reshape(x, shape=(-1, 1, 20))
        x = self.cnn(x)
        x = x.squeeze()
        x = self.output(x)

        return x


class ModelMLP(nn.Module):
    def __init__(self, num_layers, num_neurons_in_layer, dropout_p, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input = nn.Linear(20, num_neurons_in_layer)

        general_module = nn.Sequential(
            nn.Linear(num_neurons_in_layer, num_neurons_in_layer), nn.ReLU()
        )
        norm_drop_module = nn.Sequential(
            nn.Linear(num_neurons_in_layer, num_neurons_in_layer),
            nn.BatchNorm1d(num_neurons_in_layer),
            nn.ReLU(),
            nn.Dropout(p=dropout_p),
        )

        self.latent_layers = nn.ModuleList(
            [
                general_module if (i + 1) % 3 != 0 else norm_drop_module
                for i in range(num_layers)
            ]
        )

        self.output = nn.Linear(num_neurons_in_layer, 26)

    def forward(self, x):
        x = self.input(x)

        for layer in self.latent_layers:
            x = layer(x)

        output = self.output(x)

        return output


class ModelMLPpast(nn.Module):
    def __init__(self, num_layers, num_neurons_in_layer, dropout_p, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input = nn.Linear(17, num_neurons_in_layer)

        general_module = nn.Sequential(
            nn.Linear(num_neurons_in_layer, num_neurons_in_layer), nn.ReLU()
        )
        norm_drop_module = nn.Sequential(
            nn.Linear(num_neurons_in_layer, num_neurons_in_layer),
            nn.BatchNorm1d(num_neurons_in_layer),
            nn.ReLU(),
            nn.Dropout(p=dropout_p),
        )

        self.latent_layers = nn.ModuleList(
            [
                general_module if (i + 1) % 3 != 0 else norm_drop_module
                for i in range(num_layers)
            ]
        )

        self.output = nn.Linear(num_neurons_in_layer, 26)

    def forward(self, x):
        x = self.input(x)

        for layer in self.latent_layers:
            x = layer(x)

        output = self.output(x)

        return output


class ModelCNNpast(nn.Module):
    def __init__(self, p1, p2, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cnn = nn.Sequential(
            nn.Conv1d(1, 4, 3, padding="same"),
            nn.Conv1d(4, 16, 3, padding="same"),
            nn.MaxPool1d(2, 2),
            nn.Conv1d(16, 64, 3, padding="same"),
            nn.Conv1d(64, 256, 3, padding="same"),
            nn.MaxPool1d(2, 2),
            nn.BatchNorm1d(256),
            nn.Dropout(p1),
            nn.Flatten(),
        )
        self.output = nn.Sequential(
            nn.Linear(256 * 4, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(p2),
            nn.Linear(256, 26),
        )

    def forward(self, x):
        x = torch.reshape(x, shape=(-1, 1, 17))
        x = self.cnn(x)
        x = x.squeeze()
        x = self.output(x)

        return x
