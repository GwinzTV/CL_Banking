# Welcome to the Bank Management Application! 🏦

### Contents
- [Introduction](#introduction)
- [About the Project](#about-the-project)
- [How to Run Application](#how-to-run-application)

## Introduction
Welcome to my Bank Management Application! This application allows you to create a user bank account, securely login, and perform various banking operations - such as depositing, withdrawing, and viewing your balance.

## About the Project
The Bank Management Application is built with a focus on security, modularity, and user-friendliness. It employs a custom authentication method that utilises SHA1 encryption for secure user logins. The application follows the principles of Separation of Concerns (SoC) and utilises the Model-View-Controller (MVC) architecture to ensure clear separation of business logic, presentation, and user interaction. Object-oriented programming principles are at the heart of the application's design, allowing for extensibility and maintainability.

## Features 🌟
- 👤 **User Account Creation**: Create your personalised bank account with ease.
- 🔒 **Secure Authentication**: Log in securely using a custom authentication method with SHA1 encryption.
- 💸 **Banking Operations**: Deposit, withdraw, and view your balance effortlessly.
- 🧱 **Modular Structure**: Follows the SoC principle and MVC architecture for clear separation of concerns, increasing Maintainability and Scalability.

## Technologies Used 🛠️
- **Programming Language**: Python
- **Database**: SQLite
- **Encryption**: SHA1
- **Design Pattern**: Model-View-Controller (MVC)

## Getting Started 🚀

### How to Run Application
**Disclaimer:** You must install Git and Python(v3.12 or newer) on your computer before proceeding with these instructions.
If you have these installed already, go ahead with the steps below.

Open your terminal and do the following:
1. **Installation**:
First of all, clone this repository
   ```bash
   git clone https://github.com/GwinzTV/CL_Banking.git
   cd CL_Banking

2. **Create Database**:
Next, create the database using the setup script
   ```bash
   cd data
   python databaseCreation.py
You should see a file called "bank.db" in the data folder

3. **Run Application**:
Assuming you are still in the data in the terminal, run the terminal commands:
   ```bash
   cd ../src
   python main.py
You should see the Application start view.

## Feedback
I'm constantly striving to improve the Bank Management Application. If you have any feedback, suggestions, or bug reports, please feel free to [open an issue](https://github.com/GwinzTV/CL_Banking/issues) on GitHub.

### Developer
- Joshua Iyinkanmi

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
I'd like to thank the Python community, SQLite developers, and all contributors to open-source projects that made this project possible.

#### Enjoy your banking experience with my Bank Management Application! 🚀🏦✨
