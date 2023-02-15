import fbdata
import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import torch.nn as nn
import torch.optim as optim

data = fbdata.data

data['FieldPos'] = data['Distance'].str.extract('(\d+)$', expand=False).astype(int)

data["Team_3chars"] = data["Team"].str[:3].str.upper()
data["Distance_3chars"] = data["Distance"].str[:3]

data["tf"] = data["Team_3chars"] == data["Distance_3chars"]

data.loc[data.iloc[:, -1], "FieldPos"] = 100 - data.loc[data.iloc[:, -1], "FieldPos"]


# if data["tf"] == False:
#     data["YardsToGo"] = data["YardsToGo"] + 50

# if data["Team_3chars"].str[:3] == data["Distance_3chars"].str[:3]:
#     data["YardsToGo"] = data["YardsToGo"] + 50

data["Yards"] = data["Yards"].str.split().str[-1].astype(int)


data = data.drop('Distance', axis=1)
# data = data.drop('Team', axis=1)
data = data.drop('Team_3chars', axis=1)
data = data.drop('Distance_3chars', axis=1)
data = data.drop('tf', axis=1)



# print(data.head(10))
print(data.dtypes)
input("p")

#TODO: Map team to a int so it can be used in the model, Result has already done this?



le = LabelEncoder()
data['Result'] = le.fit_transform(data['Result'])

train_data, test_data = train_test_split(data, test_size=0.2)

class FootballDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.X = data.iloc[:, :-1].values
        self.y = data.iloc[:, -1].values
        
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return torch.tensor(self.X[idx], dtype=torch.float), torch.tensor(self.y[idx], dtype=torch.float)

train_dataset = FootballDataset(train_data)
test_dataset = FootballDataset(test_data)


train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=32, shuffle=False)


class BinaryClassifier(nn.Module):
    def __init__(self, input_dim):
        super(BinaryClassifier, self).__init__()
        self.fc1 = nn.Linear(input_dim, 1)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.sigmoid(x)
        return x



model = BinaryClassifier(input_dim=3)

# Define the loss function
criterion = nn.BCELoss()

# Define the optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Train the model
num_epochs = 10
for epoch in range(num_epochs):
    running_loss = 0.0
    for i, data in enumerate(train_dataloader, 0):
        inputs, labels = data

        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward + backward + optimize
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # Print statistics
        running_loss += loss.item()
        if i % 100 == 99:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 100))
            running_loss = 0.0

# Evaluation
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for data in test_dataloader:
        inputs, labels = data
        outputs = model(inputs)
        predicted = (outputs >= 0.5).float()
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy on test set: %d %%' % (100 * correct / total))



