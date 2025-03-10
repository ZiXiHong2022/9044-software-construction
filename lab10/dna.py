

import re
import sys
import os





def read_dna(dna_file):
    dna_tuples = []
    with open(dna_file, 'r') as open_data_file:
        for line in open_data_file:
            parts = line.strip().split("<->")
            if len(parts) == 1:
                parts.append('')  
            # Append tuple directly
            dna_tuples.append((parts[0].strip() if parts[0] else '', parts[1].strip() if len(parts) > 1 else ''))
    return dna_tuples





def is_rna(dna):
    dna_bases = {'A', 'T', 'G', 'C'}
    rna_bases = {'A', 'U', 'G', 'C'}

    base_counts = {}
    total_bases = 0

    for pair in dna:
        for base in pair:
            if base and base != '':
                if base in base_counts:
                    base_counts[base] += 1
                else:
                    base_counts[base] = 1
            total_bases += 1

 


    dna_count = sum(base_counts.get(base, 0) for base in dna_bases)
    rna_count = sum(base_counts.get(base, 0) for base in rna_bases if base != 'T') + base_counts.get('U', 0)

    dna_percentage = dna_count / total_bases * 100
    rna_percentage = rna_count / total_bases * 100

    
    if dna_percentage >= 90:
        return "DNA"
    elif rna_percentage >= 90:
        return "RNA" 
    else:
        return "Invalid"




def clean_dna(dna):
    match_base = {
        'A': 'T',  
        'T': 'A',  
        'G': 'C',  
        'C': 'G',  
        'U': 'A'   
    }

    cleaned_dna = []
    
    for first, second in dna:
        if first == '' and second == '':
            continue  # Ignore empty pairs
        if first != '' and second == '':
            
            if first in match_base:
                second = match_base[first]
        elif second != '' and first == '':
            
            if second in match_base:
                first = match_base[second]
        
        
        if first in match_base and second == match_base[first]:
            cleaned_dna.append((first, second))

    return cleaned_dna

def mast_common_base(dna):
    base_counts = {}
    first = None
    
    for first, _ in dna:
        if first:  
            if first in base_counts:
                base_counts[first] += 1
            else:
                base_counts[first] = 1

    
    if base_counts:
        return max(base_counts, key=base_counts.get)
    else:
        return "No valid bases found"

def base_to_name(base):
    base_names = {
        'A': 'Adenine',
        'T': 'Thymine',
        'G': 'Guanine',
        'C': 'Cytosine',
        'U': 'Uracil'
    }

    
    return base_names.get(base, "Unknown")
