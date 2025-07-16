# Project Documentation
## HING JOC Wildfire Incident Project
### July 15, 2015

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
  
  - Alert Form	
  
  - Incident and News Page Section	
  
  - Active Alerts	
  
  - Login Page	

Planned Features	

API Framework	

Data Sources	

Security, Maintenance, Reliability Overview	
  
  - Security	
  
  - Maintenance	
  
  - Reliability	

Lines of Effort	

Installation Guide	

Host Server Requirements	

Schedule For JOC HING Firewatch Project	

Proposed Budget	

\
\

## Introducion
This Joint Operations Center (JOC) Firewatch Project, under the Hawaii National Guard is a data-driven web application solution designed to support the mitigation efforts across the State of Hawaii, accounting for all counties. This platform consolidates key information from both state and federal sources, delivering real-time insights to emergency responders, policy makers, and strategic planners.
This project includes the federal and scientific communities to provide modern mapping with extensive insights into Hawaii's environmental threats.
Through this documentation, stakeholders and planners alike will find the use of this project for the deployment of resources to fighting fires, and coordinating with the County and State to gather and pinpoint areas of need. 
The project includes tools for pulling data, creating manual alerts, and tracking vital resources like emergency aerial support groups. Combined with other tools like NGB COP and WebEOC will ease the difficulties in responding to wildfire threats due to the number of systems currently being used.
Being a custom solution, there could be further developments on this platform for further expansions and extensions.
As a note this document will mix and match the terms: web solution, web application, and software solution.


This document was created under the Pacific Intelligence Innovation Imitative (P3I): VICEROY MAVEN HING group.
![](https://hawaiip3i.org/wp-content/uploads/2023/07/HawaiiP3I-logo.png)


## Mission Objective
The mission objective of this project is to aggregate multiple open-source datasets into a single web-based software solution. By aggregating state and federal data, the platform will assist emergency response services, including the National Guard and the State to pull resources from available aerial units to combat wildfires across the counties in the State of Hawaii. Our team is developing multi-layer mapping capabilities to visualize current and potential wildfires. State entities provide information for reports, locations, first-response teams, and report times. The federal information flows consist of UV indexes, air quality, brightness mapping, drought, fires, and geographic scans.

## Problem Statement
Due to the limitations of the software solutions that will be the final result, we need information that is not locked away by requests-only access and/or is not locked by API access keys such as a higher-tier paid service requirement or services locked to enterprise environments. In addition, APIs need to have interoperability with one another to ensure that they can be used in the end product. This will require documentation of the software solution and APIs, access to those API keys and programming interface, and authorization as well. For the predictability of future events, this project will need access to a server, or hardware solutions that will make use of certain compute units that can process data fast enough for machine learning and possibly LLM usage. Similarly, the data pulled must follow a certain format, which can help mitigate further processing and delays in output processes.

## Solution Compatibility
As a web solution, this platform was intended to target a multitude of devices. Such as desktops, laptops, tablets, and mobile computing devices like smartphones. For the hosting aspect of this project, it will depend on the hardware and software package and/or libraries that will support the technologies and requirements later specified in this document. A multitude of APIs could be applied but due to time constraints and current implementation of technologies, there have been some limitations that could be addressed and more technologies added in the future.

\
\

## Functional Requirements
1.Data fed through the solution may require safeguarding such a weather data collected by federal systems. 
  1.Confidentiality: Medium
  2.Some data collected is restricted to project-only usage and is limited by fetch limitations.
2.These can involve API keys that will need to be hidden or obfuscated.
  1.NOTE: API keys or tokens are likened to an identifier used to authenticate requests to a service or database.
3.The web solution will require access to the internet (if hosted by a third-party cloud) or a system that will require security and access controls if self-hosted.
  1.Integrity: High, Availability: High
  2.For third-party hosting, there will be contractual agreements regarding the sensitivity of data and its handling of the data.
  3.Self-hosting will require controls over the network, system security, physical controls, and technical support.
4.Both will require communication with federal, state, and third parties with API key access and implementation of current and future technologies.
  1.Additional alerts and notifications in the system can be manipulated and created through the interactive alert form on the web solution.
  2.This feature can be locked to users registered within the software solution.

\
\

## Interface Requirements
### User Interface
The dashboard will be implemented to follow a three or four-quadrant section appearance. The biggest and main component will be the interactive map that will be at the top. Followed by a notification and alert section that will be on the side. The last section which could be considered is a notification section dedicated to the nearest aerial vehicles, filtered to each island.
The map will contain different layers. The two main views will be a flat and a satellite representation. There will also be multiple layers to track temperature/UV, points of interest (fires), wind direction, and air pressure.
These elements can viewed under the proposed layout section below.

**Proposed Layout**
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout.png)

**Figure 1**   Backup layout for custom-made website
Backup layout for custom-made website The layout will have a news report message slider on the top left. It will contain social media posts about fires limited to the islands in addition with posts made by state departments like the HPD (police) and HFD (fire). The lower left notification section will include major fires within the islands. The top left section contains the map and map buttons for layers, filters, and additional information. The navigation bar right below the map contains the toggle overlay for the FlightTracker24 viewer and a time slot bar for past events. On the bottom right we finally have the emergency transport vehicle notification section. This section can filter per island which has been revised in Figure 2 with per island button filters. 

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay4.png)

**Figure 2**  Layout from default map, Points are clustered until zoomed in as indicated by Figure 4.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay2.png)

**Figure 3**   Layout overlay with Satellite layer mode. 

This layout now shows a overlay for map layers using the layers button on the map page. In the image it shows Fire, Windy, Drought, and Air Index layer filters. If you click on the hamburger icon for additional map options it should show additional options to select between different map points such as fires with an estimated zone, different data sources, showing fire station locations, and other displayed map points/data.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay.png)

**Figure 4**   Layout overlay with flat layer mode.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay3.png)

**Figure 5**   Layout from selecting a point and the overlay for data

**Finalized Dashboard**
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Screenshot%202025-07-15%20102306.png)

**Figure 6**  Actual design layout for dashboard

**Alert Form**
![placeholder]()

**Figure 7**  Alert Creation Dashboard

**Incident and News Pages Section**
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Incident%20and%20News%20Page%20Section.png)

**Figure 8**  The bottom left section showcasing recent incidents from pulled reports.

**Active Alerts**

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Active%20Alerts.png)

Figure 9   Right-side alert page listing recently made notifications.

**Login Page**

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Login.png)

**Planned Features**

A popup bar for chatting, page for team/group assignment, shared resources, and assigned Microsoft Teams groups.

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Assignments-Page.png)

**Figure 11**   Assignment page for each assigned group following WebEOC format for group folder assignment, includes staff and contact details, a shared resource folder for each assigned group, a description for group mission objective or task, and an assigned Microsoft Teams link. Additionally, a chat pop-up for communications between members and buttons for web pages and organizational resources.

## Website Framework

![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Website%20Framework.png)

**Figure 12**   The diagram shows the respective programming languages, libraries, and packages that will be required in the front-end and back-end of the project.


/


## API Framework

***FIRMS API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/FIRMS%20API.png)

**Figure 13**   NASA FIRMS API diagram 

***Windy API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/Windy%20API.png)

**Figure 14**   Windy API diagram

***ADS-B Exchange API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/ADS-B%20Exchange%20API.png)

**Figure 15**   ADS-B Exchange API diagram 

***National Weather Service API***
![](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/pictures/National%20Weather%20Service%20(NWS).png)

**Figure 16**   NWS API diagram 


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
* ![AirNow](https://fire.airnow.gov/#8.89/21.3814/-157.6607)
  
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

