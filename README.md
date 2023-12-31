# JSON Parser Project

## Project Overview
This JSON Parser project is an educational exercise in understanding the parsing of JSON (JavaScript Object Notation), a widely used data-interchange format. The parser is developed to handle increasingly complex JSON structures, starting from simple objects to more complex nested objects and arrays.

## Features
- Parse simple JSON objects with string keys and values.
- Handle JSON objects containing string, numeric, boolean, and null values.
- Interpret nested JSON objects and arrays.
- Robust error handling to differentiate between valid and invalid JSON structures.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Basic understanding of JSON format and Python programming.

### Installation
Clone the repository to your local machine:
```
git clone https://github.com/xj85770/json-parser
```
Navigate to the project directory:
```
cd json-parser
```

### Usage
Run the parser with a JSON file as an argument:
```
python json_parser.py path/to/jsonfile.json
```
The parser will output whether the JSON is valid and exit with an appropriate status code (0 for valid, 1 for invalid).

### Project Structure
- `json_parser.py`: The main Python script containing the lexer and parser logic.
- `tests/`: Directory containing test JSON files categorized by complexity:
  - `step1/`: Simple JSON objects (`{}`).
  - `step2/`: JSON objects with string keys and various value types.
  - `step3/`: JSON objects including boolean, null, and numeric values.
  - `step4/`: Complex JSON objects with nested structures.

## Development Steps
The parser was developed in incremental steps, each addressing a more complex aspect of JSON parsing:
1. **Step 1**: Handle empty JSON objects.
2. **Step 2**: Parse simple JSON objects with string values.
3. **Step 3**: Extend parsing capabilities to include various data types.
4. **Step 4**: Implement parsing of nested JSON objects and arrays.

## Testing
Each development step includes test files under the `tests/` directory. Run the parser against these files to validate its functionality.

