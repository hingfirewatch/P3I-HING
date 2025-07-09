# Schedule For JOC Firewatch Project

## Schedule For Weeks 1 - 7 

### Week 1: June 23 - 26

# **Framework Planning**

* Learn the programs NGB COP (WebEOC) & ARCGIS

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

## Week 2: June 30 – July 4

# **Sources Input Review**

* Review of sources

   * From NASA, State, and government entities

   * Review delayed update time frames, and currently updates sources

   * Access to State data (mostly that are by request only)

* Compatibility of information

   * Overlays

   * Filters

   * Website layout and design

## Week 3: July 7 - 11

# **Implementation and Design**

* Inter piecing the APIs to the desired selected software solution

* Determine which are compatible and tweak performance from pulled data

* Cycle and prototyping

   * Graphic Design Layout for expected outcome

## Week 4: July 14 - 17

# **Security, Delays, Problems, and Backup Plan**

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

## Week 5 & 6: July 21-  30

# **Finalize & Tweak**

* Make tweaks to coding structure

* Tweaks for graphical representation

* Prepare problem statement

## Week 6: July 28 - 31

# **Prepare Presentation**

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


# **Input Sources**

* Fire Guard

* FIRMS

* Windy

* WebEOC

* Fire Department (all counties)

* Police Data (all counties)

* County activity and indicators

* Flight Trackers

* Social Media
  

## Air Quality and Fires

* AIRNOW

   * [AirNow Fire and Smoke Map](https://fire.airnow.gov/#8.89/21.3814/-157.6607)

* NOAA MODAS, EOSDIS

   * [NASA | LANCE | FIRMS](https://firms.modaps.eosdis.nasa.gov/map/#d:24hrs;@-157.89,21.41,10.53z)
 
* NWS/NOAA
   * [NASA](https://api.weather.gov/)

* OpenMeteo
  * [OpenMeteo](https://open-meteo.com/en/docs)

* NOAA NIFC MODAS, EOSDIS

   * [NASA | LANCE | FIRMS US/Canada](https://firms.modaps.eosdis.nasa.gov/usfs/map/#d:24hrs;@-100.0,40.0,4.0z)

* Climatetrace

   * [Climate TRACE](https://climatetrace.org/)

* FEMA - national risk indicator

   * [Map | National Risk Index](https://hazards.fema.gov/nri/map)

## Drought

* Drought monitor

   * [Current Map | U.S. Drought Monitor](https://droughtmonitor.unl.edu/)

* Drought.gov

   * [The U.S. Drought Portal | Drought.gov](https://www.drought.gov/)
 
* NOAA CDO
  *[NOAA CDO](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)

* NWS/NOAA
   * [NASA](https://api.weather.gov/)

# **Other**

NOAA
weather.gov
* [api.weather.gov](https://api.weather.gov/)

Resourcewatch

* [Climate | Resource Watch](https://resourcewatch.org/dashboards/climate)

OpenData Hawaii Gov

* [Welcome - Hawaii Open Data](https://opendata.hawaii.gov/)

* [Hawaii Statewide GIS Program](https://geoportal.hawaii.gov/)

NASA worldview

* [NASA Worldview](https://worldview.earthdata.nasa.gov/?v=-161.58038707413584,18.074994085986518,-153.00129968484953,22.050120965315514&t=2025-06-21-T16%3A40%3A35Z)


# **Air Tracking**

Open Sky
  * [Open Sky](https://opensky-network.org/data/api)

ADS-B Exchange
  *  [ADS-B](https://api.adsb.lol/docs#/)

## Sources for Websscraping
Oahu
 * [Fire Department](https://fire.honolulu.gov/)
 * [Police](https://www.honolulupd.org/)
Maui, Lanai, and Kahoolawe
 * [Fire & Police Department](https://www.mauicounty.gov/)
Hawai'i
 * [Fire Department]([https://fire.honolulu.gov/](https://www.hawaiicounty.gov/departments/fire))
 * [Police](https://www.hawaiipolice.gov/)
Kauai
 * [Fire Department](https://www.kauai.gov/Government/Departments-Agencies/Fire-Department)
 * [Police](https://www.kauai.gov/Government/Departments-Agencies/Police-Department)
   

# **Mission Objective**

The mission objective of this project is to aggregate multiple open-source datasets into a single web-based software solution. By aggregating state and federal data, the platform will assist emergency response services, including the National Guard and the State to pull resources from available aerial units to combat wildfires across the counties in the State of Hawaii. Our team is developing multi-layer mapping capabilities to visualize current and potential wildfires. State entities provide information for reports, locations, first-response teams, and report times. The federal information flows consist of UV indexes, air quality, brightness mapping, drought, fires, and geographic scans.

# **Problem Statement**

Due to the limitations of the software solutions that will be the final result, we need information that is not locked away by requests-only access and/or is not locked by API access keys such as a higher-tier paid service requirement or services locked to enterprise environments. In addition, APIs need to have interoperability with one another to ensure that they can be used in the end product. This will require documentation of the software solution and APIs, access to those API keys and programming interface, and authorization as well. For the predictability of future events, this project will need access to a server, or hardware solutions that will make use of certain compute units that can process data fast enough for machine learning and possibly LLM usage. Similarly, the data pulled must follow a certain format, which can help mitigate further processing and delays in output processes.

**Problem Statement Resolution**
Access to a temporary government email address
o	This allowed us to make requestof information to government, commerical, and third-party entities to get data access


# **Security Concerns**

Depending on if the final project will contain sensitive data or will be privately used for government use, there will be some items that will be considered for this project.

Based on the CIA triad.

## **Confidentiality, Integrity, Availability**

This project will consider if the APIs and data pulled come from sources that will be sensitive.

This can include PII such as personal information from reports, camera correspondence, and ID for emergency and state employees.

Due to the mission object of this project, it is important that the reports and data are strictly untouched or unaltered. 

As with availability of this project. There could be threats due to DDoS, malware, etc. so it is imperative to keep this projects backed up, have alternative means of hosting, and is constantly managed for any changes to API structures or security concerns. 

<table>
  <tr>
   <td>

</td>
   <td>

LOW

</td>
   <td>

MEDUIM

</td>
   <td>

HIGH

</td>
  </tr>
  <tr>
   <td>

**Confidentiality**

</td>
   <td>

</td>
   <td>

X

</td>
   <td>

</td>
  </tr>
  <tr>
   <td>

**Integrity**

</td>
   <td>

</td>
   <td>

</td>
   <td>

X

</td>
  </tr>
  <tr>
   <td>

**Availability**

</td>
   <td>

</td>
   <td>

</td>
   <td>

X

</td>
  </tr>
</table>

\

# **Proposed Layout**
![Alt](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout.png)

**Figure 1**   Backup layout for custom-made website
The layout will have a news report message slider on the top left. It will contain social media posts about fires limited to the islands in addition with posts made by state departments like the HPD (police) and HFD (fire). The lower left notification section will include major fires within the islands. The top left section contains the map and map buttons for layers, filters, and additional information. The navigation bar right below the map contains the toggle overlay for the FlightTracker24 viewer and a time slot bar for past events. On the bottom right we finally have the emergency transport vehicle notification section. This section can filter per island which has been revised in Figure 2 with per island button filters.

![Alt](https://github.com/hingfirewatch/P3I-HING/blob/main/docs/concept/Backup-Template%20Layout%20Overlay2.png)

**Figure 2**   Backup layout overlay with Satellite layer mode. 
This layout now shows a overlay for map layers using the layers button on the map page. In the image it shows Fire, Windy, Drought, and Air Index layer filters. If you click on the hamburger icon for additional map options it should show additional options to select between different map points such as fires with an estimated zone, different data sources, showing fire station locations, and other displayed map points/data.

