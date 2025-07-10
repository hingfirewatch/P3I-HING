**WEBOS Framework**

WEBEOS is a web-based software solution that encompasses emergency, state, military, and federal agencies + departments for emergency notifications, event tracking, and incident management systems.

WEBEOS contains multiple interlocking APIs that pull data from supported state and government agencies that feed that data into the system. Most of these data are locked behind request-only and government authorization. Due to time constraints from research and development and addition required datasets and feeds, it would be recommended to develop a system under WEBEOS. Some example of the supported APIs are ARCGIS, NASA’s FIRMs. Which are either limited my a threshold usage count or limited by enterprise request.



**Overview**

Data from the inputs are validated before being posted to the “board.”

![alt text](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Screenshot%202025-06-24%20145447.png)

**Figure 1** Shared information streams between different departments federal, state, and military.

![alt text](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Framework_Graph.png)

**Figure 2**  API and managed information streams into WebEOS.

# Proposed APIs to Use
**BreezoMeter**
![alt text](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/BreezoMeter%20API.png)

**NASA FIRMS**
![alt text](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/FIRMS%20API.png)

**FlightRadar24**
![alt text](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/FlightRadar24%20API.png)

**Windy**
![alt text](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Windy%20API.png)

**ADS-B Exchange**
![alt text](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/ADS-B%20Exchange%20API.png)


**Backup Framework**
The backup solution was considered due to the time constraints experienced throughout the planning process of the WebEOC route. After having access to Juvare’s WebEOC and the lack of integration with third-party APIs by default, we considered making the backup the main solution of consideration. While we did weeks-long research on input sources, we worked on a backup implementation on the side. When the team finally got access to WebEOC, many things did not work out. First off, there is the lack of integration for third-party APIs and uploading datasets from files. Many of the functions on the WebEOC solution required tedious time for data log entries. With no option to read from uploaded files, that process could be inefficient for the mission's objective and response time.

The backup solution is a web-based software page that allows access to a dashboard, login system, and user accounts. This solution would be mostly hosted on either federal computer systems or by the State. It is more likely the latter due to authorization followed by procedures and policies in place. The equipment must be able to host the web page, possibly store weather data, reports, and possibly contain sensitive data such as PII. If the web service is maintained such as renewing API tokens then the solution would not need much user training.
Upon loading the site, users will navigate to the login page which will require a username and password stored on a SQL database. The program used will encrypt user credentials. Users can navigate to the dashboard through an option at the top of the website banner. The dashboard will contain a map with filters and a time selection slider, Additionally, there will be one section containing scraped data from each of the county's fire and police departments. Another section will be a color-coded alert for fires. If implemented another section will be for nearby emergency aerial vehicles. The map will be interactive and will at first, show a cluster of points in a single point which will slowly divide once you zoom in. Each point is interactable and upon clicking will have an overlay for details such as fire coordinates, brightness mapping for fires, and location of the fire. Map filters and layers will contain other elements such as UV and Heat maps, wind speeds, satellite scans, and drought spots. One of the other layers important to the mission objective is the use of flight tracking. 
Flight tracking will include all the aerial vehicles near the islands including helicopters, Each point includes details of its flight path, call sign, coordinates, and type of vehicle.



Process
Determine what data sources are openly available to the public. Determine which needs government or federal access and which will need subscription or paid access.
Determine the file format of the data and if it can be incorporated during the analysis process before integration into code or programming.
See if the API issues tokens for access. In addition, the documentation for the API is easy to understand and implement.
From a cybersecurity standpoint consider the abuse of the website and API keys if someone were to cause a denial of service (DoS) by spamming the services used. This is part of the consideration for the State to host the website and make it private rather than open to the public. Also for user credential storage, encryption, and the use of salts to hashes.
 
Leaflet
See whether the data can be important and understood depending on what attributes each data point has.
Decide on the default presentation. Zoom in, filtered points (not global), clustered points, and information display on overlay. Decide if the map starts in flat mode or satellite mode.

