#!/usr/bin/env python3
"""
Wildfire JSON Filter Tool
Filters JSON files to keep only entries related to wildfires, fires, and fire reports.
"""

import json
import re
import argparse
import os
from typing import Dict, List, Any, Union
from pathlib import Path

class WildfireFilter:
    def __init__(self):
        # High-confidence fire incident keywords
        self.fire_incident_keywords = {
            'wildfire', 'wildland fire', 'forest fire', 'brush fire', 'grass fire',
            'blaze', 'inferno', 'conflagration', 'bushfire', 'prairie fire',
            'fire incident', 'fire emergency', 'fire alert', 'fire warning',
            'fire report', 'fire danger', 'fire risk', 'fire hazard',
            'fire outbreak', 'fire broke out', 'fire started', 'fire ignited',
            'red flag warning', 'fire weather', 'fire season',
            'fire suppression', 'fire containment', 'fire perimeter',
            'acres burned', 'hectares burned', 'fire size', 'fire spread',
            'fire behavior', 'vegetation fire', 'structure fire',
            'residential fire', 'commercial fire', 'building fire',
            'arson', 'prescribed burn', 'controlled burn',
            'fire break', 'firebreak', 'fire line', 'fire retardant',
            'air tanker', 'water drop', 'fire aircraft', 'fire bomber'
        }
        
        # Fire-related descriptive words (require context)
        self.fire_descriptors = {
            'smoke', 'ash', 'ember', 'flame', 'flames', 'burn', 'burning', 'burnt',
            'charred', 'scorched', 'ignition', 'ignited', 'combustion',
            'firefighter', 'fire crew', 'evacuation', 'evacuate', 'evacuated'
        }
        
        # False positive patterns to exclude
        self.exclusion_patterns = [
            r'\bfire\s*department\b(?!\s+(respond|fighting|battle|combat|suppress))',
            r'\bfire\s*station\b(?!\s+(respond|emergency))',
            r'\bfire\s*chief\b(?!\s+(said|report|warn|alert))',
            r'\bfire\s*marshal\b(?!\s+(said|report|warn|investigate))',
            r'\bfire\s*code\b',
            r'\bfire\s*safety\b(?!\s+(concern|violation|due\s+to))',
            r'\bfire\s*drill\b',
            r'\bfire\s*inspection\b',
            r'\bfire\s*permit\b',
            r'\bfire\s*prevention\b(?!\s+(due\s+to|because\s+of))',
            r'\bfire\s*training\b',
            r'\bunder\s+fire\b',
            r'\bopen\s+fire\b',
            r'\bceasefire\b',
            r'\bfire\s+(hiring|employment|job)\b',
            r'\bfireworks?\b(?!\s+(cause|start|ignit))',
            r'\bfire\s+alarm\b(?!\s+(due\s+to|because\s+of|caused\s+by))'
        ]
        
        # High-confidence fire incident patterns
        self.fire_incident_patterns = [
            r'\b\d+\s*acres?\s*(burned?|burnt|scorched|destroyed)\b',
            r'\b\d+\s*hectares?\s*(burned?|burnt|scorched|destroyed)\b',
            r'\b\d+%\s*contain(ed|ment)\b',
            r'\bfire\s*(started|began|ignited|broke\s*out|erupted)\b',
            r'\bevacuat(e|ion|ing|ed)\b.*\b(fire|wildfire|blaze)\b',
            r'\b(fire|wildfire|blaze)\b.*\bevacuat(e|ion|ing|ed)\b',
            r'\bred\s*flag\s*warning\b',
            r'\bfire\s*weather\s*(watch|warning)\b',
            r'\bextreme\s*fire\s*(danger|risk|conditions)\b',
            r'\bfire\s*ban\b',
            r'\bburn\s*ban\b',
            r'\bfire\s*season\b',
            r'\bsmoke\s*(plume|column|visible)\b',
            r'\bfire\s*perimeter\b',
            r'\bcontainment\s*line\b',
            r'\bfire\s*retardant\b',
            r'\bair\s*tanker\b.*\b(drop|attack)\b',
            r'\bwater\s*drop\b.*\bfire\b',
            r'\bfire\s*crew\b.*(respond|deploy|fight|battle)\b',
            r'\bfirefighter\b.*(respond|deploy|fight|battle)\b',
            r'\bfire\s*department\b.*(respond|fighting|battle|combat|suppress)\b',
            r'\b(flames?|smoke)\s*(visible|seen|spotted)\b',
            r'\b(burning|fire)\s*(building|home|house|structure)\b',
            r'\b(arson|intentional)\s*fire\b',
            r'\bcampfire\b.*(spread|escaped|caused)\b',
            r'\bcontrolled\s*burn\b',
            r'\bprescribed\s*(burn|fire)\b',
            r'\bfireworks?\b.*(cause|start|ignit|spark).*\bfire\b',
            r'\bfire\b.*(cause|start).*\bfireworks?\b'
        ]
        
        # Compile patterns for better performance
        self.compiled_incident_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.fire_incident_patterns]
        self.compiled_exclusion_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.exclusion_patterns]
    
    def is_fire_related(self, text: str) -> bool:
        """
        Check if text contains fire-related content using improved filtering logic.
        
        Args:
            text: Text to analyze
            
        Returns:
            bool: True if text contains fire-related content
        """
        if not isinstance(text, str):
            return False
            
        text_lower = text.lower()
        
        # First, check for exclusion patterns (false positives)
        for pattern in self.compiled_exclusion_patterns:
            if pattern.search(text):
                return False
        
        # Check for high-confidence fire incident keywords
        for keyword in self.fire_incident_keywords:
            if keyword in text_lower:
                return True
        
        # Check for fire incident patterns
        for pattern in self.compiled_incident_patterns:
            if pattern.search(text):
                return True
        
        # Check for fire descriptors only if they appear with context
        descriptor_found = False
        for descriptor in self.fire_descriptors:
            if descriptor in text_lower:
                descriptor_found = True
                break
        
        # If descriptor found, check for additional context
        if descriptor_found:
            context_indicators = [
                'emergency', 'disaster', 'damage', 'destroy', 'threat', 'danger',
                'evacuate', 'evacuation', 'warn', 'alert', 'respond', 'response',
                'incident', 'outbreak', 'spread', 'contain', 'suppress', 'extinguish',
                'helicopter', 'aircraft', 'tanker', 'crew', 'personnel'
            ]
            
            for indicator in context_indicators:
                if indicator in text_lower:
                    return True
        
        return False
    
    def extract_text_from_value(self, value: Any) -> str:
        """
        Extract text from various data types for analysis.
        
        Args:
            value: Value to extract text from
            
        Returns:
            str: Extracted text
        """
        if isinstance(value, str):
            return value
        elif isinstance(value, (int, float, bool)):
            return str(value)
        elif isinstance(value, dict):
            return ' '.join(str(v) for v in value.values() if v is not None)
        elif isinstance(value, list):
            return ' '.join(str(item) for item in value if item is not None)
        else:
            return str(value) if value is not None else ''
    
    def analyze_item(self, item: Dict[str, Any]) -> bool:
        """
        Analyze a single JSON item for fire-related content.
        
        Args:
            item: Dictionary item to analyze
            
        Returns:
            bool: True if item contains fire-related content
        """
        # Extract all text from the item
        combined_text = ''
        
        for key, value in item.items():
            # Include key names in analysis
            combined_text += f" {key} "
            # Include values
            combined_text += f" {self.extract_text_from_value(value)} "
        
        return self.is_fire_related(combined_text)
    
    def filter_json_data(self, data: Union[List, Dict]) -> Union[List, Dict]:
        """
        Filter JSON data to keep only fire-related entries.
        
        Args:
            data: JSON data to filter
            
        Returns:
            Filtered JSON data
        """
        if isinstance(data, list):
            # Filter list of items
            filtered_items = []
            for item in data:
                if isinstance(item, dict) and self.analyze_item(item):
                    filtered_items.append(item)
                elif isinstance(item, str) and self.is_fire_related(item):
                    filtered_items.append(item)
            return filtered_items
        
        elif isinstance(data, dict):
            # Handle dictionary structure
            filtered_dict = {}
            
            # Check if this is a wrapper object with data arrays
            for key, value in data.items():
                if isinstance(value, list):
                    # Filter the list
                    filtered_list = []
                    for item in value:
                        if isinstance(item, dict) and self.analyze_item(item):
                            filtered_list.append(item)
                        elif isinstance(item, str) and self.is_fire_related(item):
                            filtered_list.append(item)
                    
                    if filtered_list:  # Only include if there are fire-related items
                        filtered_dict[key] = filtered_list
                
                elif isinstance(value, dict) and self.analyze_item(value):
                    filtered_dict[key] = value
                
                elif isinstance(value, str) and self.is_fire_related(value):
                    filtered_dict[key] = value
            
            return filtered_dict
        
        else:
            # For other types, check if fire-related
            if self.is_fire_related(str(data)):
                return data
            else:
                return None
    
    def process_file(self, input_file: str, output_file: str = None) -> Dict[str, Any]:
        """
        Process a JSON file and filter for fire-related content.
        
        Args:
            input_file: Path to input JSON file
            output_file: Path to output JSON file (optional)
            
        Returns:
            Dictionary with statistics and results
        """
        try:
            # Read input file
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Count original items
            original_count = self.count_items(data)
            
            # Filter data
            filtered_data = self.filter_json_data(data)
            
            # Count filtered items
            filtered_count = self.count_items(filtered_data)
            
            # Save filtered data if output file specified
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(filtered_data, f, indent=2, ensure_ascii=False)
            
            return {
                'success': True,
                'original_count': original_count,
                'filtered_count': filtered_count,
                'removed_count': original_count - filtered_count,
                'filtered_data': filtered_data,
                'output_file': output_file
            }
            
        except FileNotFoundError:
            return {'success': False, 'error': f'File not found: {input_file}'}
        except json.JSONDecodeError as e:
            return {'success': False, 'error': f'Invalid JSON: {str(e)}'}
        except Exception as e:
            return {'success': False, 'error': f'Error processing file: {str(e)}'}
    
    def count_items(self, data: Union[List, Dict, Any]) -> int:
        """
        Count the number of items in the data structure.
        
        Args:
            data: Data to count
            
        Returns:
            int: Number of items
        """
        if isinstance(data, list):
            return len(data)
        elif isinstance(data, dict):
            # Count items in all lists within the dictionary
            total = 0
            for value in data.values():
                if isinstance(value, list):
                    total += len(value)
                elif isinstance(value, dict):
                    total += 1
            return total if total > 0 else 1
        else:
            return 1 if data is not None else 0

def main():
    parser = argparse.ArgumentParser(description='Filter JSON files for wildfire/fire-related content')
    parser.add_argument('input_file', help='Input JSON file path')
    parser.add_argument('-o', '--output', help='Output JSON file path')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--stats-only', action='store_true', help='Show statistics only, no output file')
    
    args = parser.parse_args()
    
    # Initialize filter
    filter_tool = WildfireFilter()
    
    # Set output file
    if args.output:
        output_file = args.output
    elif not args.stats_only:
        input_path = Path(args.input_file)
        output_file = str(input_path.with_name(f"{input_path.stem}_fire_filtered{input_path.suffix}"))
    else:
        output_file = None
    
    # Process file
    result = filter_tool.process_file(args.input_file, output_file)
    
    if result['success']:
        print(f"✅ Processing completed successfully!")
        print(f"📊 Statistics:")
        print(f"   Original items: {result['original_count']}")
        print(f"   Fire-related items: {result['filtered_count']}")
        print(f"   Removed items: {result['removed_count']}")
        print(f"   Retention rate: {result['filtered_count']/result['original_count']*100:.1f}%")
        
        if result['output_file']:
            print(f"💾 Filtered data saved to: {result['output_file']}")
        
        if args.verbose and result['filtered_count'] > 0:
            print(f"\n🔍 Sample of filtered data:")
            sample_data = result['filtered_data']
            if isinstance(sample_data, list) and len(sample_data) > 0:
                print(json.dumps(sample_data[0], indent=2)[:500] + "...")
            elif isinstance(sample_data, dict):
                print(json.dumps(sample_data, indent=2)[:500] + "...")
    else:
        print(f"❌ Error: {result['error']}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())

# Example usage:
"""
# Basic usage
python wildfire_filter.py data.json

# Specify output file
python wildfire_filter.py data.json -o filtered_data.json

# Verbose mode
python wildfire_filter.py data.json -v

# Statistics only (no output file)
python wildfire_filter.py data.json --stats-only

# Example programmatic usage:
filter_tool = WildfireFilter()
result = filter_tool.process_file('emergency_reports.json', 'fire_reports.json')
if result['success']:
    print(f"Filtered {result['filtered_count']} fire-related entries")
"""