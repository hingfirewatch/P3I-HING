import json
import numpy as np
from datetime import datetime, timedelta
import random

def generate_hawaii_viirs_fire_sample_json(start_date='2024-04-01', end_date='2024-06-30', num_fires=500):
    """
    Generate sample NASA VIIRS fire detection data specifically for Hawaiian Islands in JSON format
    
    Parameters:
    - start_date: Start date for the dataset (YYYY-MM-DD)
    - end_date: End date for the dataset (YYYY-MM-DD)
    - num_fires: Number of fire detection records to generate
    
    Returns:
    - List of dictionaries with VIIRS-like fire detection data for Hawaii
    """
    
    # Convert dates
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    date_range = (end - start).days
    
    # Hawaiian Islands with specific coordinates and fire characteristics
    hawaiian_islands = [
        {
            'name': 'Hawaii (Big Island)',
            'lat_min': 18.91, 'lat_max': 20.27,
            'lon_min': -156.07, 'lon_max': -154.81,
            'weight': 0.35,  # Highest fire activity due to size and lava zones
            'fire_intensity': 'high',  # Volcanic activity and dry leeward sides
            'elevation_factor': 1.2  # Higher elevation areas more fire-prone
        },
        {
            'name': 'Maui',
            'lat_min': 20.57, 'lat_max': 21.03,
            'lon_min': -156.69, 'lon_max': -155.99,
            'weight': 0.25,
            'fire_intensity': 'high',  # Recent devastating fires (Lahaina area)
            'elevation_factor': 1.15
        },
        {
            'name': 'Oahu',
            'lat_min': 21.25, 'lat_max': 21.71,
            'lon_min': -158.29, 'lon_max': -157.64,
            'weight': 0.20,
            'fire_intensity': 'medium',
            'elevation_factor': 1.1
        },
        {
            'name': 'Kauai',
            'lat_min': 21.87, 'lat_max': 22.23,
            'lon_min': -159.78, 'lon_max': -159.31,
            'weight': 0.10,
            'fire_intensity': 'medium',
            'elevation_factor': 1.05
        },
        {
            'name': 'Molokai',
            'lat_min': 21.13, 'lat_max': 21.21,
            'lon_min': -157.33, 'lon_max': -156.75,
            'weight': 0.05,
            'fire_intensity': 'low',
            'elevation_factor': 1.0
        },
        {
            'name': 'Lanai',
            'lat_min': 20.72, 'lat_max': 20.86,
            'lon_min': -157.07, 'lon_max': -156.86,
            'weight': 0.03,
            'fire_intensity': 'low',
            'elevation_factor': 1.0
        },
        {
            'name': 'Kahoolawe',
            'lat_min': 20.52, 'lat_max': 20.58,
            'lon_min': -156.69, 'lon_max': -156.54,
            'weight': 0.02,
            'fire_intensity': 'low',
            'elevation_factor': 0.9
        }
    ]
    
    data = []
    
    for i in range(num_fires):
        # Select island based on weights
        island = np.random.choice(hawaiian_islands, p=[isl['weight'] for isl in hawaiian_islands])
        
        # Generate coordinates within selected island
        # Add some clustering around fire-prone areas (leeward/dry sides)
        if np.random.random() < 0.7:  # 70% of fires on leeward (drier) sides
            # Bias towards western/southern parts of islands (leeward sides)
            lat_bias = 0.3  # Bias towards lower latitudes
            lon_bias = 0.3  # Bias towards western longitudes
            
            latitude = np.random.triangular(
                island['lat_min'], 
                island['lat_min'] + (island['lat_max'] - island['lat_min']) * lat_bias,
                island['lat_max']
            )
            longitude = np.random.triangular(
                island['lon_min'],
                island['lon_min'] + (island['lon_max'] - island['lon_min']) * lon_bias,
                island['lon_max']
            )
        else:
            # Random distribution for remaining fires
            latitude = np.random.uniform(island['lat_min'], island['lat_max'])
            longitude = np.random.uniform(island['lon_min'], island['lon_max'])
        
        # Generate random date and time with Hawaiian seasonality
        random_days = np.random.randint(0, date_range)
        fire_date = start + timedelta(days=random_days)
        month = fire_date.month
        
        # Hawaiian fire seasonality (dry season: April-October)
        seasonal_factor = 1.0
        if month in [4, 5, 6, 7, 8, 9, 10]:  # Dry season
            seasonal_factor = 2.0
        elif month in [11, 12, 1, 2, 3]:  # Wet season
            seasonal_factor = 0.3
            
        # Skip fires based on seasonal probability
        if np.random.random() > seasonal_factor / 2.5:
            continue
            
        # Generate time of day (Hawaii fires often in afternoon due to trade winds)
        # Trade winds typically die down in afternoon, increasing fire risk
        hour_weights = [0.01, 0.01, 0.01, 0.01, 0.02, 0.03, 0.04, 0.05,
                         0.06, 0.07, 0.08, 0.09, 0.11, 0.13, 0.15, 0.14,
                        0.12, 0.10, 0.08, 0.06, 0.04, 0.03, 0.02, 0.01]

        # Add this line to ensure exact sum of 1.0 (fixes floating-point precision issues)
        hour_weights = np.array(hour_weights) / np.sum(hour_weights)

        hour = np.random.choice(range(24), p=hour_weights)
        minute = np.random.randint(0, 60)
        second = np.random.randint(0, 60)

        acq_datetime = fire_date.replace(hour=hour, minute=minute, second=second)
        
        # Generate VIIRS-specific attributes based on island characteristics
        confidence_probs = {'l': 0.05, 'n': 0.55, 'h': 0.40}  # Changed to single letters
        if island['fire_intensity'] == 'high':
            confidence_probs = {'l': 0.02, 'n': 0.48, 'h': 0.50}
        
        confidence = np.random.choice(['l', 'n', 'h'], 
                                    p=list(confidence_probs.values()))
        
        # Fire Radiative Power influenced by island type and vegetation
        base_frp = 15.0 if island['fire_intensity'] == 'high' else 8.0
        frp = max(0.1, np.random.lognormal(mean=np.log(base_frp), sigma=1.0))
        
        # Higher FRP for Big Island due to volcanic activity and larger fires
        if island['name'] == 'Hawaii (Big Island)':
            if np.random.random() < 0.15:  # 15% chance of very high intensity fires
                frp *= np.random.uniform(2.0, 5.0)
        
        # Brightness temperature (Kelvin) - adjusted for tropical climate
        bright_t31 = np.random.uniform(280, 340) + (frp * 0.2)
        brightness = bright_t31 + np.random.uniform(15, 35)  # Brightness typically higher than T31
        
        # Satellite information (realistic for Hawaii coverage)
        satellite_options = ['N20', 'N21', 'NOAA-20', 'NOAA-21']
        satellite = np.random.choice(satellite_options)
        
        # Version
        version = '2.0NRT'
        
        # Acquisition date/time
        acq_date = acq_datetime.strftime('%Y-%m-%d')
        acq_time = acq_datetime.strftime('%H%M')
        
        # Scan and track (VIIRS I-band resolution)
        scan = round(np.random.uniform(0.3, 0.8), 2)
        track = round(np.random.uniform(0.3, 0.8), 2)
        
        # Day/Night flag (Hawaii is about 10 hours behind UTC)
        hawaii_hour = (hour - 10) % 24
        daynight = 'D' if 6 <= hawaii_hour <= 18 else 'N'
        
        # Create the record in the specified format
        record = {
            "latitude": round(latitude, 5),
            "longitude": round(longitude, 5),
            "acq_date": acq_date,
            "acq_time": acq_time,
            "confidence": confidence,
            "instrument": "VIIRS",
            "daynight": daynight,
            "scan": scan,
            "satellite": satellite,
            "bright_t31": round(bright_t31, 2),
            "version": version,
            "track": track,
            "brightness": round(brightness, 2),
            "frp": round(frp, 2)
        }
        
        data.append(record)
    
    # Sort by acquisition date and time
    data.sort(key=lambda x: (x['acq_date'], x['acq_time']))
    
    return data

def save_hawaii_dataset_json(data, filename='hawaii_viirs_fire_sample.json'):
    """Save the Hawaii dataset to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Hawaii fire dataset saved to {filename}")
    print(f"Total Hawaiian fire detections: {len(data)}")
    if data:
        dates = [record['acq_date'] for record in data]
        print(f"Date range: {min(dates)} to {max(dates)}")

def generate_hawaii_statistics(data):
    """Generate and display statistics for the Hawaii fire data"""
    if not data:
        print("No data to analyze")
        return
    
    # Island distribution (approximate based on coordinates)
    def classify_island(lat, lon):
        if 18.91 <= lat <= 20.27 and -156.07 <= lon <= -154.81:
            return 'Hawaii (Big Island)'
        elif 20.57 <= lat <= 21.03 and -156.69 <= lon <= -155.99:
            return 'Maui'
        elif 21.25 <= lat <= 21.71 and -158.29 <= lon <= -157.64:
            return 'Oahu'
        elif 21.87 <= lat <= 22.23 and -159.78 <= lon <= -159.31:
            return 'Kauai'
        elif 21.13 <= lat <= 21.21 and -157.33 <= lon <= -156.75:
            return 'Molokai'
        elif 20.72 <= lat <= 20.86 and -157.07 <= lon <= -156.86:
            return 'Lanai'
        elif 20.52 <= lat <= 20.58 and -156.69 <= lon <= -156.54:
            return 'Kahoolawe'
        else:
            return 'Unknown'
    
    # Add island classification to data for analysis
    for record in data:
        record['island'] = classify_island(record['latitude'], record['longitude'])
    
    print("\n=== Hawaii Fire Dataset Summary ===")
    print(f"Total fire detections: {len(data)}")
    
    dates = [record['acq_date'] for record in data]
    print(f"Date range: {min(dates)} to {max(dates)}")
    
    # Island distribution
    island_counts = {}
    for record in data:
        island = record['island']
        island_counts[island] = island_counts.get(island, 0) + 1
    
    print("\n=== Distribution by Hawaiian Island ===")
    for island, count in sorted(island_counts.items()):
        percentage = (count / len(data)) * 100
        print(f"  {island}: {count} fires ({percentage:.1f}%)")
    
    # Confidence distribution
    confidence_counts = {}
    for record in data:
        conf = record['confidence']
        confidence_counts[conf] = confidence_counts.get(conf, 0) + 1
    
    print("\n=== Confidence Distribution ===")
    conf_labels = {'l': 'Low', 'n': 'Nominal', 'h': 'High'}
    for conf, count in sorted(confidence_counts.items()):
        label = conf_labels.get(conf, conf)
        percentage = (count / len(data)) * 100
        print(f"  {label}: {count} detections ({percentage:.1f}%)")
    
    # FRP statistics
    frp_values = [record['frp'] for record in data]
    print(f"\n=== Fire Radiative Power Statistics ===")
    print(f"Average FRP: {np.mean(frp_values):.2f} MW")
    print(f"Median FRP: {np.median(frp_values):.2f} MW")
    print(f"Max FRP: {max(frp_values):.2f} MW")
    print(f"Min FRP: {min(frp_values):.2f} MW")
    
    # Day/Night distribution
    daynight_counts = {}
    for record in data:
        dn = record['daynight']
        daynight_counts[dn] = daynight_counts.get(dn, 0) + 1
    
    print("\n=== Day/Night Distribution ===")
    dn_labels = {'D': 'Day', 'N': 'Night'}
    for dn, count in sorted(daynight_counts.items()):
        label = dn_labels.get(dn, dn)
        percentage = (count / len(data)) * 100
        print(f"  {label}: {count} detections ({percentage:.1f}%)")
    
    # Sample records
    print("\n=== Sample Records ===")
    for i, record in enumerate(data[:5]):
        print(f"Record {i+1}:")
        print(f"  Date: {record['acq_date']} {record['acq_time']}")
        print(f"  Location: {record['latitude']}, {record['longitude']} ({record['island']})")
        print(f"  FRP: {record['frp']} MW, Confidence: {record['confidence']}")
        print()

# Generate the Hawaii-specific sample dataset
if __name__ == "__main__":
    print("Generating NASA VIIRS sample fire dataset for Hawaiian Islands (JSON format)...")
    
    # Generate 3 months of Hawaii fire data
    hawaii_fire_data = generate_hawaii_viirs_fire_sample_json(
        start_date='2024-04-01',
        end_date='2024-06-30',
        num_fires=500  # Adjust based on realistic Hawaii fire frequency
    )
    
    # Display Hawaii-specific statistics
    generate_hawaii_statistics(hawaii_fire_data)
    
    # Save the dataset
    save_hawaii_dataset_json(hawaii_fire_data, 'hawaii_viirs_fire_3months.json')
    
    print("\n=== JSON Format Example ===")
    if hawaii_fire_data:
        print("Sample record structure:")
        print(json.dumps(hawaii_fire_data[0], indent=2))
    
    print(f"\n=== Geographic Bounds ===")
    if hawaii_fire_data:
        lats = [record['latitude'] for record in hawaii_fire_data]
        lons = [record['longitude'] for record in hawaii_fire_data]
        print(f"Latitude range: {min(lats):.4f}° to {max(lats):.4f}°")
        print(f"Longitude range: {min(lons):.4f}° to {max(lons):.4f}°")