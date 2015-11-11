from pymol import cmd, stored, math

def loadFitnessFactors (mol,startaa=1,source="/Users/student/Box Sync/PUBS/Pymol-practice.txt", visual="Y"):
        # adapted from http://www.pymolwiki.org/index.php/Load_new_B-factors
        """
        Replaces B-factors with a list of fitness factor values contained in a plain txt file
 
        usage: loadFitnessFactors mol, [startaa, [source, [visual]]]
 
        mol = any object selection (within one single object though)
        startaa = number of first amino acid in 'new Fitness-factors' file (default=1)
        source = name of the file containing new Fitness-factor values (default=newFitnessFactors.txt)
        visual = redraws structure as cartoon_putty and displays bar with min/max values (default=Y)
 
        example: loadFitnessFactors 1LVM and chain A
        """
        obj=cmd.get_object_list(mol)[0]
        cmd.alter(mol,"b=-1.0")
        inFile = open(source, 'r')
        counter=int(startaa)
        fitnessFacts=[]
        for line in inFile.readlines():
                fitnessFact=float(line)
                fitnessFacts.append(fitnessFact)
                cmd.alter("%s and resi %s and n. CA"%(mol,counter), "b=%s"%fitnessFact)
                counter=counter+1
        if visual=="Y":
                cmd.show_as("cartoon",mol)
                cmd.cartoon("putty", mol)
#                cmd.set("cartoon_putty_scale_min", min(fitnessFacts),obj)
#                cmd.set("cartoon_putty_scale_max", max(fitnessFacts),obj)
                cmd.set("cartoon_putty_transform", 0,obj)
                cmd.set("cartoon_putty_radius", 0.2,obj)
                cmd.spectrum("b","red_white_blue", "%s and n. CA " %mol)
                cmd.ramp_new("count", obj, [min(fitnessFacts), (min(fitnessFacts)+max(fitnessFacts))/2, max(fitnessFacts)], color = ["blue", "white", "red"])
                cmd.recolor()

cmd.extend("loadFitnessFactors", loadFitnessFactors);
