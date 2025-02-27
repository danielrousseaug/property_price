# Property Price Estimator

## Overview
This script analyzes property data to determine the closest property by distance, the most similar property based on characteristics, and an estimated property value based on comparable properties.

## Features
- **Find Closest Property**: Uses geographical coordinates to determine the nearest property.
- **Find Most Similar Property**: Compares numerical features to identify the most similar property.
- **Estimate Property Value**: Uses price per square meter from a similar property to estimate the target property’s value.

## File Structure
```
├── properties.csv        # Source file containing property data
├── with_coordinates.csv  # Property data including geographical coordinates
├── script.py             # Main script containing all functionality
└── README.md             # Project documentation
```

## Dependencies
- `geopy` (for distance calculations)
- `csv` (for reading property data)
- `numpy` (for numerical calculations)

## Installation
```bash
pip install geopy numpy
```

## Usage
Run the script with:
```bash
python script.py
```

## How It Works
1. **`get_closest(property)`**: Finds the nearest property based on geographical distance.
2. **`get_most_similair(property)`**: Identifies the most similar property using selected numerical attributes.
3. **`value_estimate(property)`**: Estimates the property value based on the most similar property’s price per square meter.

## Future Improvements
- Improve similarity scoring by considering more property attributes.
- Optimize data handling for large datasets.
- Add an interactive user interface.

## License
This project is licensed under the MIT License.
