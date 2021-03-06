# YourCRISPRguide
YourCRIPSRguide is a web-tool in progress developed for a new class II protein RbCpf1 and its PAM TTKGT. 

It is based on a trustworthy tool - on [CRISPOR](http://crispor.org) - as it has multiple features and high reliability (and includes DeepCpf1 data), so yourCRISPRguide uses its approach, but adds an opportunity to search for sgRNA for RbCpf1 and to predict the score for each of them. As RbCpf1 PAM is less extensively represented in the genomes ([see the notebook for the info about PAM_requency function](https://github.com/albinoknyaz/YourCRISPRguide/blob/frequency/frequency)) that the 'classical' PAMs, RbCpf1 might be a more precise nuclease for different types of experiments. Thus, the demand for sgRNA design for this protein is quite high. 

**What can you do via YourCRISPRguide right now? (you can find an example [here](example.ipynb); example resulta find [here](example_results.csv) )**
- upload your sequence (as fasta file or as a string) 
- find PAMs (avaliable for CRISPOR plus RbCpf1) 
- get sgRNA sequences 
- calculate the scores for each of the found sgRNAs (for RbCpf1) 
- range the sgRNA sequences according to the score (for RbCpf1) 

Even though our first priority was to fulfil all the criteria for RbCpf1, we will add multiple advanced features very soon (see notebook [development](development.ipynb) ). 
These features will include: 
- secondary gRNA structures prediction (it might result in poor cleavage efficiency, see the [article](https://academic.oup.com/nar/article/48/6/3228/5716457) for details)
Readiness: ready to be used in linear model. [RNAFold](http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi) was applied. 
- gRNA length variation ([article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6538514/)) 
- off-target effects prognosis for the phenotype (uses data from several databases of mutations) (this can be useful if there are several sequence candidates that have a small off-target effect and you need to choose more relevant at the phenotype level)
- the effect of a mismatch in dependence of the distance from PAM region ([article](https://www.pnas.org/content/pnas/early/2020/05/05/1918685117.full.pdf) ( the effect of a mismatch in dependence of the distance from PAM region )) 
And some more parameters for a linear model to get the optimized scores. 

Furthermore, everything will be avaliable via the link online and will not require any specific programs or modules to be installed locally. 




