
# Trading Platform - OOP-CLI Project

![Database Diagram](https://github.com/user-attachments/assets/d366f8e0-b01b-4d41-809f-9a0fbc6e557a)

## Trading Platform

Are you a trader looking to manage your portfolios and transactions seamlessly? Or maybe you're someone interested in tracking stock purchases and investments across multiple portfolios? Well, look no further! The Trading Platform CLI is a user-friendly application designed to help you manage **traders**, **portfolios**, and **transactions** efficiently. With a simple command-line interface (CLI), you can easily track portfolios, log stock transactions, and manage trader accounts.

## Core Features

- **Manage Traders**: Create, update, delete, and list traders on the platform.
- **Manage Portfolios**: Create and manage multiple portfolios for each trader. A trader can have more than one portfolio.
- **Manage Transactions**: Log transactions for different portfolios, track stock indices, and calculate total values.
- **View Data**: Retrieve all traders, portfolios, or transactions from the database with ease.
- **CRUD Operations**: Full functionality for creating, updating, deleting, and viewing traders, portfolios, and transactions.

## Set-Up

To access the Trading Platform, follow these steps to install dependencies and enter the virtual environment:

1. **Install required packages**:
    ```bash
    pipenv install
    ```

2. **Activate the virtual environment**:
    ```bash
    pipenv shell
    ```

3. **Run the CLI application**:
    Once all packages are installed and you’ve activated the virtual environment, start the CLI application with:
    ```bash
    python lib/cli.py
    ```

## How to Use

Once the application is running, you will be greeted with a main menu. Here, you can browse and interact with the database using the following options:

- **Manage Traders**: Add a new trader, update or delete an existing trader, and view all the portfolios managed by a trader.
- **Manage Portfolios**: Create portfolios under specific traders, update or delete portfolios, and view all transactions within a portfolio.
- **Manage Transactions**: Log new transactions for a portfolio, update or delete existing transactions, and view all transactions.

### Database Structure

The database consists of three core entities: **Traders**, **Portfolios**, and **Transactions**. The relationships between these entities are represented in the diagram below:

![Database Diagram](https://github.com/user-attachments/assets/d366f8e0-b01b-4d41-809f-9a0fbc6e557a)

- **Traders**: Manage multiple portfolios.
- **Portfolios**: Contain multiple stock transactions.
- **Transactions**: Record stock index, quantity, price, and the total amount (quantity * price).

### Entity Relationships

- Each **Trader** can have multiple **Portfolios**.
- Each **Portfolio** can contain multiple **Transactions**.
- Each **Transaction** logs details of a specific stock trade.

---
