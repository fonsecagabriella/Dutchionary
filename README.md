# DUTCHIONARY
Welcome to Dutchionary, a tool designed to make learning Dutch vocabulary easier and more enjoyable! 🇳🇱

#### Video Demo:  <https://youtu.be/rKdzWVigkXU

#### Description: Dutchionary is a Python tool designed to assist people learning the Dutch language. It functions as a dictionary with a focus on providing contextual understanding by presenting words in sentences. Additionally, it helps users practice newly learned words by allowing them to create sentences and receive feedback.

This project was developed as a conclusion for the course [CS50 - Python, by Harvard ](https://cs50.harvard.edu/python/2022/).
The web-version of DUTCHIONARY [can be found here](https://imgabi.com/dutchionary)

---

## Motivation
Learning Dutch can be a daunting task, particularly due to its complex vocabulary and the intricacies of idiomatic expressions. Often, simply knowing the meaning of a word is not enough to fully grasp its usage and nuances. It becomes crucial to see the word in a sentence to understand its context and how it is applied. Moreover, finding accurate and comprehensive information about idiomatic expressions can be a time-consuming process that involves searching through multiple websites. Dutchionary aims to simplify this process by providing a convenient tool for learners to access word meanings in sentences and receive immediate practice opportunities.

## Functionality
Dutchionary consists of several files, each with a specific purpose and functionality:

1. **project.py**: This is the main file of the program that should be executed to start Dutchionary. It handles the API calling, and interacts with the user.

2. **text_project.py**: As a requirement from the course assignment, this file contains tests for functions from project.py

3. **dutchonary.py**: This file contains the implementation of the dictionary functionality. It includes the calls to the API from OpenAI.


## Design Choices
During the development of Dutchionary, several design choices were made to ensure an effective and user-friendly tool for language learners.

- **Contextual sentences:** To provide a deeper understanding of word usage, Dutchionary includes example sentences alongside word meanings. By presenting words in context, users can better grasp their meaning and usage.

- **Immediate practice:**  Research suggests that [practicing newly learned vocabulary immediately after exposure helps with retention](https://knowingneurons.com/blog/2021/04/27/vocabulary-retention-in-adult-language-learners/). With this in mind, Dutchionary allows users to create sentences using the words they look up. This practice feature promotes active learning and provides a positive environment for language acquisition.

- **Integration with Large Language Models**: This choice was made in order to provide the user with a conversational tone. Additionally, generative AI has recently become a great interest of mine, and I want to practice more with it.


By considering these design choices, Dutchionary aims to enhance the learning experience for Dutch language learners and provide a valuable tool for their journey towards proficiency -- *or at least for myself* 🤓

## Getting Started
To get started with Dutchionary, follow these steps:

1. Clone the repository to your local machine or download the source code files.
2. Make sure you have Python3.10+ installed on your system. You will also need additional libraries as listed below.
3. Open a terminal or command prompt and navigate to the project directory.
4. Create an account in [OpenAI](https://platform.openai.com/account/api-keys) and generate a KEY. Update the file .env inside prompts, with your generated key. Your .env file will look something like this:
`
OPENAI_API_KEY=sk-randomSequence

`

5. Run the project.py file using the Python interpreter.
6. Follow the on-screen instructions to search for word meanings, create sentences, and receive feedback.
7. Enjoy exploring the Dutch language with Dutchionary and have fun practicing your skills!

### Libraries
You can install the necessary libraries by running each row in your terminal individually:

`pip install openai`
API for OpenAI, used in dutchonary.py

`pip install python-dovenv`
Used to manage/key API keys stored in your local environment

`pip install json`
Used in project to transform the returned string from API

`pip install re`
Used to ensure string follow a regular expression

`pip install pytest`
Used in test_project; Run `pytest project.py` in your terminal to test functions.

`pip install cowsay`
Fun way to return the feedback for the user.
After all, Dutch cows are kind of famous 🐮 *By the way, useless fun-fact, but Dutch cows say BOO instead of MOO - Ask any Dutch person!*


## Acknowledgments
I would like to express my gratitude to the whole team behind CS50, and especially to the professor David J. Malan.

## Contributing
Contributions to Dutchionary are welcome! If you would like to contribute to the project by adding new features, improving existing functionality, or enhancing the vocabulary database, please feel free to submit a pull request. Together, we can make Dutchionary even better for language learners.

## License
Dutchionary is licensed under the MIT License. Feel free to use, modify, and distribute the code in accordance with the terms of the license.

Thank you for taking the time to explore Dutchionary! I hope this tool proves to be a helpful companion in your Dutch language learning journey. If you have any feedback, suggestions, or issues, please don't hesitate to contact me at imgabi@imgabi.com . Happy learning! 