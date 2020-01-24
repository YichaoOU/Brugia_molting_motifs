# Get started

This repository provides raw data for Brugia molting motif analysis. Please see our pre-print:

Grote Alexandra, Yichao Li, Canhui Liu, Denis Voronin, Adam Geber, Sara Lustigman, Thomas Unnasch, Lonnie Welch, and Elodie Ghedin. ***Prediction pipeline for discovery of regulatory motifs associated with Brugia malayi molting.*** bioRxiv (2019): 781930.

# Directories

Raw motif discovery results were provided in folders such as `L3D6_L3`, which means up-regulated genes in L3D6 comparing to L3. Each folder also contains the fasta sequences (i.e., `fore.fa` and `back.fa`) used to perform motif analysis. Motif analysis was done using [Emotif_alpha](https://github.com/YichaoOU/Emotif_Alpha)

Genome features and orthologs info were provided in `genome_data`.

There were 395 motifs passed our statistical tests, shown in `Brugia_molting_motifs.merged.pwm`.

There were 12 motifs out of those 395 motifs that were conserved in either *C. elegans* or *O. volvulus*, shown in `Supp_File_motif_PWM.meme`
