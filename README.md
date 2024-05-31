# Openai Webpage Conclusions

This project autonomously collects ai generated insights for optimizing and building a company website by utililizing industry leader's design strategies. This python program takes a list of websites as input, uses webscraping techniques to extract the text data from each website, collects the information in a text file, and feeds this information through openai's api to generate reccomendations and analysis for important information to build your website around.

## Inputs

As an example test run, the [Input](Input/) folder contains two txt files, one for the [Consulting](Input/ConsultingWebsites.txt) industry with 5 provided webites and one for the [Software Development](Input/SoftwareDevWebsites.txt) industry with 4 provided websites. This program can accept as many Input files as neccessary, but as openai limits the size of chat requests to about ~16,384 characters, the number of websites in each input file should be limited.

### Formatting Input Files

Each input file should begin with the name of the industry on the first line, and all websites on their own line below the industry name with no spaces or blank lines.

## Webscraping Output

Take a look at the [Output](Output/) folder to see the collected data from all of the provided websites. Notice, the data is messy and difficult to follow, one of the pitfalls of webscraping that makes openai extremely useful in this program.

## Results

Take a look at openai's [conclusions](Conclusions.txt) for the consulting and software development industries.

## Running the Program on Your Own

### Requirements

-  Python >= 3.7
-  [Open AI keys](https://platform.openai.com/account/api-keys)
    - Unfortunately, Openai api keys are not free to use, so payment is required for your api key to function.
If you are curious to run this program but are not interested in paying openai for a key, feel free to email me at [seantsullivan04@gmail.com](mailto) and I will be happy to collaborate with you to hopefully find the results you are looking for.

### Steps

1.  Clone this repository and delete all txt files in the Output folder, conclusions.txt, as well as the Input txt files if you wish to use your own.
&emsp;&emsp;&emsp;&emsp;If you have your own input file(s), make sure you save it in the Input folder and it is correctly formatted.

2.  Open a terminal window and save your openai key to the OPENAI_API_KEY environment variable by running  
&emsp;&emsp;`export OPENAI_API_KEY=YourSecretKey` for macOS  
&emsp;&emsp;OR  
&emsp;&emsp;`set OPENAI_API_KEY=YourSecretKey` for Windows

3.  Then in the same terminal window, start the program by running  
&emsp;&emsp;`python3 multiurl_webscrape.py` for macOS  
&emsp;&emsp;OR  
&emsp;&emsp;`python multiurl_webscrape.py` for Windows

4. Wait for approximately 10 seconds (depends on the amount and size of the input file(s)) and open the newly created Conclusions.txt file in the root of the directory
