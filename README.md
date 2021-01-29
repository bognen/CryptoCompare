# CryptoCompare

## General Description
The Web application, which compares cloud mining contracts offered by range of different mining companies. The application also offers the list of digital coins with their current prices, brief description, hash rates, current supply, etc.There is also list of companies that provide shotr information on mining companies and contracts they offer. All contracts listed within a company are shown in terms of coins. User also can see a full list of contracts and details of each contract.

A user can pick up two contracts and compare their daily, weekly and monthly returns as well as total profit and profitability.

The comparison is made using not only current prices of offered digital coins, but using AI backed prediction. In order to calculate future prices rates in the application, we use Long Short Term Memory neural recurrent neural network

## Techologies
FRONTEND is all done using mostly Vue.js with some JQuery. It is using Axios https client library to consume REST APIs.

BACKEND. For backend techology Python Django was chosen. It queries a database, processes data and retuns it as JSON objects.

DATABASE. As the database we chose MongoDB as NoSQL cross-platform document-oriented database program.

## External resources
The HTML template of the website is designed by **ColorLib**.
The website along with utilizing REST API from the website's backend it also consumes third party APIs:
* **coingecko.com**  to obtain information on coin market indicators
* **rapidapi.com** to obtain techical information on coins
