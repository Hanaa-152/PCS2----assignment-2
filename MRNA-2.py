from Bio.Data import CodonTable

def rna_count(protein):
    codon_table = CodonTable.unambiguous_rna_by_name["Standard"].forward_table
    codon_count = {}
    
    for aa in codon_table.values():
        codon_count[aa] = codon_count.get(aa, 0) + 1
    
    total_count = 3  
    for aa in protein:
        total_count = (total_count * codon_count[aa]) % 1000000
    
    return total_count

protein = "MCDQAEPVYAVMQDSWDIGYDTRPMCARGPKPRADSNPHPNNDTSPINHCATNGMMQSWMRVQLRHGEDSIQIATWTPTHVTTNNGMTPAVNLNIPRHFNINLAIFFWWKVWGGFEPIKGPPTYWDICPNFYEVATAFGQDSYNTVFRRQCRICKVYSRQYRQVAFEGWIYRFQFKFWFPVRDIAIKKEWQMIMCCWSRISHPEPITFCQCGKHPSNTEEQSKVAFHVVQDQTVTMATLATPPKTVYKYEFKMRKSPMDKPYYMPIWMNMGPWRCNMCLSTHVQDKYRRYFGTILPNYFSFHQFHVTWETCVQRVGWSIHNLQLCGKNFPKWKSLKQGKESEMADLMRHYQKDLNYQASSMKDQYGGDCIIIECGMMAYICLRRLENATMETVHTNIMDWMNQTYMYEAHRQTGLSYGSGWHQTHPTPNRDTPKMFICAGYTNQDSNAGDANLHTLGEFSQCGNPSKVCDEMTNQCWVKRHMCLDMANGHYKQHKMCIDRTVNPTDMADFYPTSTAMREIHNNLERFCEMDCYKAVCGHESTNVMLMVCFDHTWEKKSFTVWDQKTQIAWINIRACMWFGVNALDMFLVLQWCDFAQLHVAPDPALPWWDNRICTKYTGICPHMKTHSMRFGDDTIQHGIYDCTAKKNTWRKQQECYGIQLTMQFMQASIMGVSFVECCPATSSKGNITPCYPPPVIMICFENNSFPAMQACTHDNIKLPILIQILIQYEHPINGASNYQNTVASDQAKVIHNAVNAKGMFHYGDPMKPNRIAEDLRFLMCYMVPMGYWDNYGQTRLRHWFYIHRFRLEKQEEKHCAFWYQIRSKPSNRYDQAYKWFYKCWTVPVNMSLFETMIPDGQCQIFLWKYQTPYYAAYRFVREQSWSNPSNWVWFVYRENRVVYLKYRHTSVGDHHESLECNGSTSDQGQISDQRNQGRANKIMSTQTDAMSPKKNDYSGGCLRVAARDVPMRMLVNVPHQVTGFGVKRYEIQYYQWLVSKT"
print(rna_count(protein)) 