# graphical-vne-analyser

A GitHub repository for comparing various Virtual Network Embedding (VNE) algorithms and illustrating VNE and physical substrate graphs.

## Table of Contents
- [graphical-vne-analyser](#graphical-vne-analyser)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running Tests](#running-tests)
    - [Generating Images (with Dot File)](#generating-images-with-dot-file)

## Getting Started

These instructions will help you get started with running tests and setting up the environment for this project.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.x
- pip

### Installation

To set up the environment, run the following command:

```bash
pip install -r requirements.txt
```
### Running Tests
To run tests, execute the following commands:

```bash
chmod +x batch.sh
./batch.sh

```

### Generating Images (with Dot File)

To generate images for the allocation of node and link resources with dot files, execute:

```bash
python toDot.py

```

