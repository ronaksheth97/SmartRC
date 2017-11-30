Adapted from https://github.com/Sentdex/pygta5

Currently, to use the latest version of this AI, you will need to run first "create_training_data.py," then balance this data with "balance_Data.py."

When creating training data, this works when you have the stream in windowed mode, 800x600 resolution, at the top left of your screen. You need this for both training and testing.

Do this for as many files/training samples as you wish. I suggest 100K+ after balancing, but the more the merrier.

Next, Train the model with train_model.py.

Finally, use the model with test_model.py. 
