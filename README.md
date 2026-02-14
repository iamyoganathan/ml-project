# ML Project - Git & GitHub Assignment

A Python machine learning project demonstrating version control with Git and GitHub.

## Project Structure

```
ml-project/
├── train.py              # Model training script
├── predict.py            # Prediction script  
├── utils.py              # Helper functions (data loading, preprocessing, model persistence)
├── config.py             # Configuration parameters
├── README.md             # This file
└── ASSIGNMENT_SOLUTION.md # Complete assignment solutions and explanations
```

## Files Description

- **train.py**: Contains functions for training machine learning models
- **predict.py**: Script for making predictions using trained models
- **utils.py**: Utility functions including:
  - `load_data()` - Load data from CSV files
  - `preprocess_data()` - Data preprocessing
  - `evaluate_model()` - Model evaluation
  - `save_model()` - Save trained models
  - `load_model()` - Load trained models
- **config.py**: Configuration settings for model parameters, data paths, and training settings
- **ASSIGNMENT_SOLUTION.md**: Complete solutions for all three stages of the assignment

## Usage

### Training a Model
```bash
python train.py
```

### Making Predictions
```bash
python predict.py
```

## Git Repository

This project demonstrates:
- ✅ Git initialization and basic setup
- ✅ Selective staging and committing
- ✅ Remote repository connection
- ✅ Collaborative workflow (fetch, pull, push)
- ✅ Best practices for version control

## Assignment Stages Completed

### Stage 1: Basic Setup ✓
- Created project directory structure
- Initialized Git repository
- Created all required files
- Checked repository status

### Stage 2: Version Control Workflow ✓
- Staged specific files (train.py, utils.py)
- Committed with descriptive message
- Connected to GitHub remote
- Set up main branch

### Stage 3: Collaborative Workflow ✓
- Demonstrated fetch and pull operations
- Managed local and remote changes
- Documented conflict resolution strategies
- Provided best practices guide

## Documentation

For complete assignment solutions, commands, explanations, and best practices, see [ASSIGNMENT_SOLUTION.md](ASSIGNMENT_SOLUTION.md).

## Author

Created for AML Git & GitHub Version Control Assignment

## Date

February 14, 2026
