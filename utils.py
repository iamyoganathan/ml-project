"""
Utility functions for ML project
"""
import pandas as pd

def load_data(filepath):
    """
    Load data from CSV file
    """
    print(f"Loading data from {filepath}")
    # Data loading logic here
    return pd.DataFrame()

def preprocess_data(data):
    """
    Preprocess the data for training
    """
    print("Preprocessing data...")
    # Preprocessing logic here
    return data

def evaluate_model(model, test_data):
    """
    Evaluate model performance
    """
    print("Evaluating model...")
    # Evaluation logic here
    return {"accuracy": 0.95}

def save_model(model, filepath):
    """
    Save trained model to disk
    """
    print(f"Saving model to {filepath}")
    # Model saving logic here
    return True

def load_model(filepath):
    """
    Load trained model from disk
    """
    print(f"Loading model from {filepath}")
    # Model loading logic here
    return "loaded_model"
