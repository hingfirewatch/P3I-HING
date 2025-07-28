<img src="https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Document%20Title.png" alt="Title" width="600" height="400">

### July 28, 2015

==============================================================


### TABLE OF CONTENTS

Introduction

Mission Objective	

Problem Statement	

Solution Compatibility	

Functional Requirements	

Interface Requirements	
  
  - User Interface	
  
    - Proposed Layout	
  
    - Finalized Dashboard
   
  - Map Interface

    - Map Filters

    - NASA FIRMS Data Points

    - Map Base Layers
   
      - Weather

      - ESRI

      - Google Satellite

      - Google Terrain

      - Google Flat Terrain
     
      - OpenStreetMap   

  - Map Alert Filters

    - View Filter
   
    - Legend
   
    - Point Forecast
   
    - AlertWest
   
    - Flight Tracker
  
  - Dashboard Interface
     
    - Alert Form	
    
    - Incident and News Page Section	
    
    - Active Alerts	
    
    - Login Page	

Planned Features	

API Framework	

Data Sources	

  - Weather, Air Quality, Drought, and Fires

Security, Maintenance, Reliability Overview	
  
  - Security	
  
  - Maintenance	
  
  - Reliability	

Lines of Effort	

Installation Guide	

Host Server Requirements	

Schedule For JOC HING Firewatch Project	

Proposed Budget

  - Tracking
  
  - Hosting  


==============================================================

\


# Introducion
This Joint Operations Center (JOC) Firewatch Project, under the Hawaii National Guard is a data-driven web application solution designed to support the mitigation efforts across the State of Hawaii, accounting for all counties. This platform consolidates key information from both state and federal sources, delivering real-time insights to emergency responders, policy makers, and strategic planners.

This project includes the federal and scientific communities to provide modern mapping with extensive insights into Hawaii's environmental threats.
Through this documentation, stakeholders and planners alike will find the use of this project for the deployment of resources to fighting fires, and coordinating with the County and State to gather and pinpoint areas of need. 

The project includes tools for pulling data, creating manual alerts, and tracking vital resources like emergency aerial support groups. Combined with other tools like NGB COP and WebEOC will ease the difficulties in responding to wildfire threats due to the number of systems currently being used.

Being a custom solution, there could be further developments on this platform for further expansions and extensions.

As a note this document will mix and match the terms: web solution, web application, and software solution.


This document was created under the Pacific Intelligence Innovation Imitative (P3I): VICEROY MAVEN HING group.
<img src="https://hawaiip3i.org/wp-content/uploads/2023/07/HawaiiP3I-logo.png" alt="" width="400" />


# Mission Objective
The mission objective of this project is to aggregate multiple open-source datasets into a single web-based software solution. By aggregating state and federal data, the platform will assist emergency response services, including the National Guard and the State to pull resources from available aerial units to combat wildfires across the counties in the State of Hawaii. Our team is developing multi-layer mapping capabilities to visualize current and potential wildfires. State entities provide information for reports, locations, first-response teams, and report times. The federal information flows consist of UV indexes, air quality, brightness mapping, drought, fires, and geographic scans.

# Problem Statement
Due to the limitations of the software solutions that will be the final result, we need information that is not locked away by requests-only access and/or is not locked by API access keys such as a higher-tier paid service requirement or services locked to enterprise environments. In addition, APIs need to have interoperability with one another to ensure that they can be used in the end product. This will require documentation of the software solution and APIs, access to those API keys and programming interface, and authorization as well. For the predictability of future events, this project will need access to a server, or hardware solutions that will make use of certain compute units that can process data fast enough for machine learning and possibly LLM usage. Similarly, the data pulled must follow a certain format, which can help mitigate further processing and delays in output processes.

# Solution Compatibility
As a web solution, this platform was intended to target a multitude of devices. Such as desktops, laptops, tablets, and mobile computing devices like smartphones. For the hosting aspect of this project, it will depend on the hardware and software package and/or libraries that will support the technologies and requirements later specified in this document. A multitude of APIs could be applied but due to time constraints and current implementation of technologies, there have been some limitations that could be addressed and more technologies added in the future.

\
\

# Functional Requirements

1. **Data Safeguarding Requirements**
    - Data fed through the solution may require safeguarding, such as weather data collected by federal systems.
    - **Confidentiality:** Medium  
    - Some data collected is restricted to project-only usage and may be subject to fetch limitations.

2. **API Key Security**
    - These systems may involve API keys that must be hidden or obfuscated.
    - **NOTE:** API keys or tokens act as identifiers used to authenticate requests to a service or database.

3. **Hosting Requirements and Access Control**
    - The web solution will require internet access:
        - If hosted via a third-party cloud provider  
        - Or hosted internally on a system requiring proper security and access controls
    - **Integrity:** High  
    - **Availability:** High  
    - For third-party hosting, contractual agreements will govern data sensitivity and handling procedures.

4. **Self-Hosting Considerations**
    - Self-hosted deployments will require:
        - Network and firewall configuration
        - System security and updates
        - Physical access control
        - Ongoing technical support

5. **Interagency Communication & Notifications**
    - Communication will involve federal, state, and third-party actors who use and manage API key access.
    - Additional alerts and notifications can be triggered through an interactive web form.
    - This alerting system can be restricted to registered users within the platform.

\
\

# Interface Requirements
## User Interface
The dashboard will be implemented to follow a three or four-quadrant section appearance. The biggest and main component will be the interactive map that will be at the top. Followed by a notification and alert section that will be on the side. The last section which could be considered is a notification section dedicated to the nearest aerial vehicles, filtered to each island.

The map will contain different layers. The two main views will be a flat and a satellite representation. There will also be multiple layers to track temperature/UV, points of interest (fires), wind direction, and air pressure.
These elements can be viewed under the proposed layout section below.

## **Proposed Layout**
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout.png)

**Figure 1** | Backup layout for custom-made website

The proposed layout will have a news report message slider on the top left. It will contain social media posts about fires limited to the islands in addition with posts made by state departments like the HPD (police) and HFD (fire) and surrounding counties. The lower left notification section will include major fires within the islands. The top left section contains the map and map buttons for layers, filters, and additional information. The navigation bar right below the map contains the toggle overlay for the FlightTracker24 viewer and a time slot bar for past events. On the bottom right we finally have the emergency transport vehicle notification section, additionally there will be a filter per island.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay4.png)

**Figure 2** | Layout from default map, Points are clustered until zoomed in as indicated by Figure 5.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay2.png)

**Figure 3** | Layout overlay with Satellite layer mode. 

This layout now shows a overlay for map layers using the layers button on the map page. In the image it shows Fire, Windy, Drought, and Air Index layer filters. If you click on the hamburger icon for additional map options it should show additional options to select between different map points such as fires with an estimated zone, different data sources, showing fire station locations, and other displayed map points/data.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay.png)

**Figure 4** | Layout overlay with flat layer mode.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay3.png)

**Figure 5** | Layout from selecting a point and the overlay for data

# Finalized Dashboard

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/THFIC.png)

**Figure 6** | Actual design layout for dashboard

# Map Interface

## Map Filters

Located at the top right of the Live Map View is the map filter section.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Map%20Filters.png)

**Figure 7** | Map filters for map. Features for different map base layers, filters for different user-created alerts, and a toggle for flight tracking extensions and other features like legend and the forecast for a set point.

## NASA FIRMs Data Points

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/FIRMs%20Points%20(close-up).png)

**Figure 8** | FIRMs API-supplied points.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Forecast%20Point.png)

**Figure 9** | Detailed overlay of points.

## Map Base Layers

### Weather

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Weather%20Base%20Layer.png)

**Figure 10** | Default overlay based on Windy.

### ESRI
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/ESRI.png)

**Figure 11** | Base layer based on ArcGIS.

### Google Satellite

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Google%20Satellite.png)

**Figure 12** | Base layer based on Google Satellite Map view.

### Google Terrain
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Google%20Terrain.png)

**Figure 13** | Base layer based on Google Terrian Map view.

### Google Flat Terrain
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Google%20Terrain.png)

**Figure 14** | A flatter view, which does not include terrain shadows from Figure 11.

### OpenStreetMap
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/OSM.png)

**Figure 15** | Another flat map view based on OpenStreetMap (OSM).

## Map Alert Filters

Map alert filter for specific statuses based on severity rating, type of fire, and tags based on current alert conditions like fires that are active, being investigated, resolved, or were a false alarm

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Map%20Alert%20Filters.png)

**Figure 16** | Alert filters on the map interface.

### View Filter

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/View%20Filters.png)

**Figure 16** | Toggle-able filter menu for map legend (heat map, satellite sources, and fire detection confidence), forecast for selected points, AlertWest panel (landscape fire cameras), and a backup Flight Tracker.

### Legend

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Legend.png)

**Figure 18** | Map legend showcasing heat map (Windy), satellite sources from NASA FIRMs, fire detection confidence from NASA VIIRS and MODIS satellite mapping, and also a brief metric explanation of Fire Radiative Power (FRP).

### Point Forecast

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Forecast%20Point.png)

**Figure 19** | A select point showing NASA FIRMs data and a forecast at the current time.

### AlertWest

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/AlertWest.png)

**Figure 20** | A toggle-able and readjust-able panel for AlertWest that focuses on current and possible alerts using AI detection with landscape camera views.

### Flight Tracker

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Flight%20Tracker.png)

**Figure** | 21 A toggle-able and readjust-able panel for flight tracking based on ADS-B Exchange. The service detects military, public, and private aerial vehicles. Addition information consists of vehicle callsign, flight path, altitude, signal source, and squawk code channels.

# Dashboard Interface

## Alert Form

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Alert%20Form.png)

**Figure** | 22 Alert Creation Dashboard

## Active Alerts

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Active%20Alerts.png)

**Figure 23** | Right-side alert page listing recently made notifications.

## Incident and News Page Section

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Incident%20and%20News%20Page%20Section.png)

**Figure 24** | The bottom left section showcasing recent incidents from pulled reports.

## Login Page**

Users will require to make an account to access mission essential features like alert notifications.

<img src="https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Login.png" alt="" width="400" />

**Figure 25** | Login Portal

**Planned Features**

A popup bar for chatting, page for team/group assignment, shared resources, and assigned Microsoft Teams groups.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Assignments-Page.png)

**Figure 26** | Assignment page for each assigned group following WebEOC format for group folder assignment, includes staff and contact details, a shared resource folder for each assigned group, a description for group mission objective or task, and an assigned Microsoft Teams link. Additionally, a chat pop-up for communications between members and buttons for web pages and organizational resources.

An export function to Alerts Form to allow HING JOC faulty to allow easy input for other third-party forms such as NGP COP, WebEOC, and other forms following the standard operation procedures (SOP).

## Website Framework

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Website%20Framework.png)

**Figure 12** | The diagram shows the respective programming languages, libraries, and packages that will be required in the front-end and back-end of the project.


/


## API Framework

***FIRMS API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/FIRMS%20API.png)

**Figure 13** | NASA FIRMS API diagram 

***Windy API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Windy%20API.png)

**Figure 14** | Windy API diagram

***ADS-B Exchange API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/ADS-B%20Exchange%20API.png)

**Figure 15** | ADS-B Exchange API diagram 

***National Weather Service API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/National%20Weather%20Service%20(NWS).png)

**Figure 16** | NWS API diagram 


/


## Data Sources
* Fire Guard
* WebEOC
* Fire Department (all counties)
* Police Data (all counties)
* County activity and indicators
* Flight Trackers
* Social Media
* Weather, Air Quality, and Fires
  
AirNow Fire and Smoke Map

* [AirNow](https://fire.airnow.gov/#8.89/21.3814/-157.6607)
  
NASA | LANCE | FIRMS

* [FIRMS](https://firms.modaps.eosdis.nasa.gov/map/#d:24hrs;@-157.89,21.41,10.53z)
  
NASA Worldview

* [NASA](https://worldview.earthdata.nasa.gov/)
  
NASA | LANCE | FIRMS US/Canada

*  [LANCE](https://firms.modaps.eosdis.nasa.gov/usfs/map/#d:24hrs;@-100.0,40.0,4.1z)

Climate TRACE

*  [Climate Trace](https://climatetrace.org/)

FEMA - national risk indicator
* [FEMA](https://hazards.fema.gov/nri/map)

Windy: Waves

*  [Windy](https://hazards.fema.gov/nri/map)

ALERTWest

* [ALERTWest](https://alertwest.live/)

### Aerial Tracking
ADS-B Exchange

* [ADS-B Exchange](https://www.adsbexchange.com/data/rest-api-samples/)

OpenSky Network

* [OpenSky](https://openskynetwork.github.io/opensky-api/)

FlightRadar24

* [FlightRadar24](https://www.flightradar24.com/51.47,0.46/6)

### Drought
Drought monitor
*  [Drought Monitor](https://droughtmonitor.unl.edu/)

Drought.gov

*  [Drought](https://www.drought.gov/)

### Other
NOAA	
*  [Weather Gov](https://www.weather.gov/)

Resourcewatch
*  [Resourewatch](https://resourcewatch.org/dashboards/climate)

OpenData Hawaii Gov
*  [Opendata](https://opendata.hawaii.gov/)
*  [Geoportal](https://geoportal.hawaii.gov/)

NASA worldview
*  [Worldview](https://worldview.earthdata.nasa.gov/?v=-161.58038707413584,16.861705037718462,-153.00129968484953,23.26341001358357&t=2025-06-21-T16%3A40%3A35Z)


### Scraped Sources
Oahu

 * [Fire Department](https://fire.honolulu.gov/)

 * [Police Department](https://www.honolulupd.org/)

**Maui, Lanai, and Kahoolawe**

 * [Fire & Police Department](https://www.mauicounty.gov/)
   
Hawai'i / Big Island

 * [Fire Department](https://www.hawaiicounty.gov/departments/fire)
  
 * [Police](https://www.hawaiipolice.gov/)
   
Kauai

 * [Fire Department](https://www.kauai.gov/Government/Departments-Agencies/Fire-Department)
   
 * [Police Department](https://www.kauai.gov/Government/Departments-Agencies/Police-Department)

Hawaii News Now

* [Hawaii News Now](https://www.hawaiinewsnow.com/news/)

KITV - Island News

* [KITV](https://www.kitv.com/news/)

KHON2

* [KHON2](https://www.khon2.com/local-news/)

  
/
/


## Security
Depending on data storage decisions, this project will contain sensitive data or will be used privately for government use, there will be some items that will be considered for this project.

Sensitive data such as PII will contain personal information from reports, camera correspondence, and contact for emergency, state, federal, and military purposes. Additional information flow will also contain weather and scientific data locked to third parties locked to certain use cases. 

Based on the CIA triad, Confidentiality, Integrity, and Availability will explain information 
security principles for business operations and risk.

Due to the mission objective of this project, it is important that the reports and data are strictly untouched or unaltered. 
As with the availability of this project. There could be threats due to DDoS, malware, etc. so it is imperative to keep this project backed up, have alternative means of hosting, and constantly manage for any changes to API structures or security concerns. 

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Mission_Heat%20map.png)

**Figure 17**   CIA Triad - securiy heat map.

## Maintenance
This project will require maintenance (at minimal) for API key access upon expiration and due to technical errors such as revoked tokens. In addition to adding new API keys for new API and services added in the future.
 There might be additional efforts in filtering for alert notifications and clearing or correcting past manually added alerts.

## Reliability
The map for this project will pull from three to four sources of data from both federal and community and scientific-driven sources. If one of the sources is down the project will include other resources to related services. The majority of these sources of data are real-time and are frequently updated.

## Recommended Hardware Specificaitions
The web application may require the lists hardware requirements to ensure that operation of the software is run smoothly.

***Minimum Requirements:***

| **Component** | **Specifications**                            |
|---------------|-----------------------------------------------|
| **CPU**       | Intel Core i3 (8th gen) **OR** AMD Ryzen 3 (3000 series) |
| **RAM**       | 4 GB                                           |
| **Storage**   | 60 GB HDD or SSD                               |
| **GPU**       | Integrated Intel or AMD                        |
| **OS**        | Windows 10, macOS 10.13+, or Ubuntu 20.04+     |
| **Browser**   | Latest version of Chrome, Firefox, or Edge     |
| **Network**   | 10 Mbps broadband                              |

Recommended Requirements:

| **Component** | **Specifications** |
|---------------|--------------------|
| **CPU**       | Intel Core i5 (10th gen) **OR** AMD Ryzen 5 (3000 series) |
| **RAM**       | 16 GB |
| **Storage**   | 256 GB SSD |
| **GPU**       | Integrated Intel or AMD **OR** Dedicated AMD Radeon or NVIDIA GeForce |
| **OS**        | Windows 10, macOS 10.13+, or Ubuntu 20.04+ |
| **Browser**   | Latest version of Chrome, Firefox, or Edge |
| **Network**   | 25+ Mbps broadband |


/


## Lines of Effort
* Determine API compatibility
* Determine Data Sources
* Access to Data Sources
* Authentication and Authorization
* API Keys
* Database
  
***Line 1: Access + Data***
* Way points (RAPIDS, FIRMS, 911/State, WebEOC, ARCGIS, NGB COP)
***Line 2: Clarity of data points***
* Waypoint placement (amount)
* Dashboard information
***Line 3: API Inter-compatibility***
* Leaflet, Windy, FlightRadar24, BreezoMeter
* Layers, Filters, Toggles
***Line 4:  Security***
* API Keys (encryption)
* Data security
* SQL database for login
***Line 5: Systems + Equipment***
* PAAS/Hosting, Domain
  * Equipment handling (Specifications)
* Security: DDoS, API-key provider, encryption
* Regulations with sensitive data storage
* Update Delays
> [!Note]
> Due to time limitations and scope, Line 6 may not be implemented
> 
***Line 6: Data for ML & Waypoints based on high/possible risk***
* Importing multiple datasets
* Learning time for multiple cycles
* Multiple iterations/models for data output
* LLM and ML methods for consideration
* Integrate into a API for dashboard as chatbot

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Lines%20of%20Effort.png)

**Figure 15**   Lines of Effort - reference to military approach to milestones.

## Installation Guide

***Recommended Tools:*** <br>
Integrated Development Environment (IDE) like Microsoft VS Code  <br>

***Website***

Prerequisites: <br>
Python 3.8+ <br>
Node.js + npm <br>
PostgreSQL <br>

Bootstrap <br>
`npm install bootstrap` <br>
Next.js <br>
`npx create-next-app@latest my-app` <br>
`cd my-app`
React.js <br>
`npm install react react-dom next` <br>

***Map***

Flask <br>
`python -m venv venv` <br>
`source venv/bin/activate` <br>
`pip install Flask Flask-Cors Flask-SQLAlchemy psycopg2-binary` <br>
Leaflet <br>
`npm install leaflet react-leaflet` <br>

***Web Scraper Notification***

Python: BeautifulSoup + requests <br>
`pip install beautifulsoup4` <br>
`pip install requests` <br>


/


## Host Server Requirements
***Component	Specifications***
## Server Specifications

| **Component**     | **Specifications** |
|-------------------|--------------------|
| **CPU**           | 8–16 Core Intel Xeon Silver **OR** AMD EPYC |
| **RAM**           | 64–128 GB |
| **Storage**       | 1–2 TB NVMe SSD |
| **Bandwidth**     | 1 Gbps dedicated uplink |
| **OS**            | Windows Server 2022 **OR** Ubuntu 22.04 LTS |
| **Database**      | PostgreSQL with SSD-backend |
| **Security**      | Hardware firewall, DDoS protection, SSL, intrusion detection |
| **Backup**        | Daily automated backups with offsite redundancy |
| **Virtualization**| Docker or Kubernetes support |
| **Compliance**    | FedRAMP or NIST 800-53 |


/


## Schedule For JOC HING Firewatch Project
***Schedule For Weeks 1 - 7***

***Week 1: June 23 - 26***

**Framework Planning**
* Learn the programs NGB COP , WebEOC & ARCGIS
* API access and learning
* API compatibility
* Access to State Databases
  * Police Reports
  * Fire Department Reports
  * Access to data from all counties in Hawaii
* Base map planning
  * Filters
    * Air Traffic (Helicopters) – identifiers, response type
  * Air Quality, drought, and current fires
  * Possible ETA for emergency services
***Week 2: June 30 – July 4***
**Sources Input Review**
* Review of sources
  * From NASA, State, and government entities
  * Review delayed update time frames, and currently updates sources
  * Access to State data (mostly that are by request only)
* Compatibility of information
  * Overlays
  * Filters
  * Website layout and design
***Week 3: July 7 - 11***

**Implementation and Design**
* Inter piecing the APIs to the desired selected software solution
*  Determine which are compatible and tweak performance from pulled data
* Cycle and prototyping
  * Graphic Design Layout for expected outcome
***Week 4: July 14 - 17***

**Security, Delays, Problems, and Backup Plan**
* Determine Security gaps
  * APIs, DDoS, Service Delays, Server load-balancing
* Delays
  * Timed delays due to data pulls
* Problems
  * Create a problem statement
    * Delays in coding
    * Problems in API keys
    * Problems in API compatibility
    * Complications from the proposed software solutions for end-product
* Backup plan
  * Find development need to work on the second proposed software solution if the first does not meet expectations
  * Proposed time frame for development on this system
***Week 5 & 6: July 21-  30***

**Finalize & Tweak**
* Make tweaks to coding structure
* Tweaks for graphical representation
* Prepare problem statement
***Week 6: July 28 - 31***
**Prepare Presentation**
* Make slideshows
* Snapshot final-end solution
* Prepare showcase for prototype
* Relate to other projects and current solutions in the market or currently being used
* Showcase how project improves

Address:
* Mission Objective
* Input Sources, Output Sources
* Scope of Project
* Organization
* Supporting Members

## Proposed Budget

###Tracking
#### FlightRadar24 - $900 / month | $10,800 / year
Cancel anytime
Need: Due to limitations of other flight tracking APIs, this API would give results of not only public but private and military based aerial vehicles that are easy to implement with this API.
* In addition FlightRadar24 provides instant API Key access instead of requesting which may takes days or weeks to arrive.

#### Windy - $2.08 / month | $24.99 / year
Cancel anytime
Need: This API has multiple elements that can feed through data such as satellite, radar, wind, temperature, clouds, air and UV, and drought.
AeroAPI - $ 1000 / month | $12,000 / year

### Hosting
#### DigitalOcean - $24 / month | $288 / year
Need: A place to host the web application. Bypass the process and procedures from hosting on-premise.

| Solution Name   | Cost Per Month | Cost Per Year |
|----------------|----------------|----------------|
| FlightRadar24  | $900.00        | $10,800.00     |
| Windy          | $2.08          | $24.99         |
| AeroAPI        | $1,000.00      | $12,000.00     |
| DigitalOcean   | $24.00         | $288.00        |



