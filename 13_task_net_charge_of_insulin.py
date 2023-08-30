#In the Flow Control module, you learned about if-else statements, while loops, lists, and for loops. Now you will apply what you have learned to the real-world application of human insulin.

# Here, you will use lists, for and while loops, and basic math to calculate the net charge of insulin from pH 0 to pH 14.

# In this lab, you will:

# Create a dictionary of pKa values (which indicate the strength of an acid) that will be used in the net charge calculations
# Use the count() method to get a count of amino acids
# Use a while loop to calculate the net charge of insulin from pH 0 to pH 14
# ---------------------------------------------------------------------------
# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {
    'y': 10.07,
    'c': 8.18,
'k': 10.53,
'h': 6.00,
'r': 12.48,
'd': 3.65,
'e': 4.25,    
}


seqCount = (
    {
    z: float(insulin.count(z)) 
    for z in ['y','c','k','h','r','d','e']
    }
    )
print(seqCount)

pH = 0 
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1
    
    # print(['k'])