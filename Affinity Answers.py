try:
    fh = open(r'C:\\Users\\HP\\Desktop\\2.txt','r')
    res = fh.readlines()
    ss=["crime","racial","parenting"]
    for i in range(len(ss)):
        c=0
        for j in range(len(res)):
            c+=res[j].count(ss[i])
        print("Count of"+ss[i]+" is : " ,c)
    fh.close()
    
except OSError :
    print('File Path incorrect')
    print('Error in opening File ')


##__Text file content__

##Dominant theoretical explanations of racial disparities in criminal offending overlook a key risk factor associated with race: interpersonal racial discrimination. Building on recent studies that analyze race and crime at the micro-level, we specify a social psychological model linking personal experiences with racial discrimination to an increased risk of offending.
## We add to this model a consideration of an adaptive facet of African American culture: ethnic-racial socialization, and explore whether two forms—cultural socialization and preparation for bias—provide resilience to the criminogenic effects of interpersonal racial discrimination. Using panel data from several hundred African American male youth from the Family and Community Health Study, we find that racial discrimination is positively associated with increased crime in large part by augmenting depression, hostile views of relationships, and disengagement from conventional norms. Results also indicate that preparation for bias significantly reduces the effects of discrimination on crime, primarily by reducing the effects of these social psychological mediators on offending. Cultural socialization has a less influential but beneficial effect. Finally, we show that the more general parenting context within which preparation for bias takes place influences its protective effects.
##
##The following is a list of ethnic slurs (ethnophaulisms) that are, or have been, used as insinuations or allegations about members of a given ethnicity or racial group or to refer to them in a derogatory (that is, critical or disrespectful), pejorative (disapproving or contemptuous), or otherwise insulting manner.
##
##Some of the terms listed below (such as "Gringo", "Yank", etc.) are usually used in casual speech without any intention of causing offence. The connotation of a term and prevalence of its use as a pejorative or neutral descriptor varies over time and by geography.
##
##For the purposes of this list, an ethnic slur is a term designed to insult others on the basis of race, ethnicity, or nationality. Each term is listed followed by its country or region of usage, a definition, and a reference to that term.
##
##Ethnic slurs may also be produced as a racial epithet by combining a general-purpose insult with the name of ethnicity, such as "dirty Jew", "Russian pig", etc. Other common insulting modifiers include "dog", "filthy", etc. However, such terms are not included in this list.
##
