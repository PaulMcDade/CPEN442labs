
#alphabet_noJ = "QWERTYUIOPASDFGHKLZXCVBNM"
from itertools import permutations
encrypt_mappings = {"TH":"YG","ER":"RN"}
decrypt_mappings = {v: k for k, v in encrypt_mappings.items()}
text = 'MQWIDQWNSGYLKQYGRNTMARIEMRATGRZAIHXUTYYMMRIAGKQTUZCEBHBEIGVYCDXNWCULIOYGMAYGKWDMNRDNTVMVWIKFYIAXIZLAWZEAGKTKCPOVQGEDUNFUTYYMSGDUGSRNKGRNZWRNSYKRWZRCTAVYTNWTTNFUTYYMCEIRRILMFNYMYGKTGINRRDYZRKAZTCFHWUEXODATEIYGRNLMFNYMIZOQCEBPVOKWYGMAATATDLOXRIMDZAFHQYRCLAZAYGTSODZRAQZACKCBLAAMVSAZYGKWDMNRDNTVLMFNYMBYWLEXZMRDTDKFLMFNYMGKQTUZRIWYDQTEGYYBRTCUTYYMMRUQYVWIGHGZCDEMTAGKPYIZQYRCWNCPDOMWLICPIZEXYGMZYGKGQDAREDUNQUTATWKRWZKBDKYGCTLMFNYMPYGIWZNDTYYMMRCBLAZAYGTSYLICGLUNGUYCBORCWKYGCTLHMZGUVSNGIWTBTDCMTYYMSGDIKGITTLKRUBRNCEDOIHGUEXTNNBEDUOMAGUVYFETCHKOBLAMGYGNWQDYFGINRZMMERTZDSHTVZIIUQDRIVMKBRNRTWYGKTSRNNWQDYGRNRQUNLAMGYGRNIGRNNWIGRNPYYHKWMRCQIGRNQNLDMGAENGKWLMFNYMMRIAGKQMEAGKEAGKTSRKMGYGNTAZRIUWYMDORCOVKRVYTNYGNIYLEMKAGRDMTNLAAMMEMPMZYGKTQYAITVRXOAGKZAQAWUIRLMFNYMKRQDODTWOIRGZAYZLMFNYMMRCBLAZAYGOTGZKRUBRNRQHUIWMRIBTAYLYWTYRGNRQALAYWGKMVWNNRAQGLNIIWTAGKFUQDNIZAFITYYMHDYGRNNWYHRILAWTMYKRWZKBCKBEMUTYYMGKQYDCLMFNYMMRCDWTQYILUNOAGUEXDTFCTALMFNYMVMNAOYYLYGUWMZUOBOCEWICUTYYMMRCDWCHKYLICULAMPYIZCETWVYDUYLICRTMITYYMYGKWAETQDTYFYIXNWNIQTWGSYLICLMTNYLMITYYMMRIABYWGYLICVHTLIOGKHKOBZTXFSKRTCBLAAIAZTAKSQYQTATCMIWBYMGYGUWQTWYKDNITYYMVYHKZTZCMKALIRAQRCGIEMMZRTWTEXGKDRNRQALAMGWICPCOKWTYIWGUEXQRYLAOYLKQZIQMRCYGNIYLEMKAOTLUMYNWZAFMTYYMQYDCYGKWDMNRDNTVLMFNYMSGRKHKKGQAWCECHKRIGKDACEKRDATAVYHKIWVOUBCTODDOPAIYRYKFYQLMFNYMMRUBTVBEMOZWRNOAGUEXQTWYGKNRLMFNYMMRUBTVYGNIMUOVKRBYCUQDEDRIGKEATAGUVFIKRNDORCMVVLLAMGYGKWDMNRDNTVIDWYRKRIDMNRSCCPUOLMFNYMMRUQTDCUTYYMDUMRZMYIRCRNWYMRIQKSOTYHPYLIIQUWGYVORTWZYGUWGRYDWTSCIUYLEMKAMRIBAPMDEYTAGKADMUTYYMBEMOZOMDKTYLDMCPUZMRQYQUTAYGMAUWGRDMYHKTYLBYWZZMRDTDKFMRVQRNRIYGIEDEICTAZMYMMGWIKBTVADRTKAMRIBDQOTDKPYTNQYNRLMFNYMGIGZVZIZMVVCKWBYRCPDMPALVTLIADMAGKZDLWIWGKNRYGMRCEMROTYGRNLMCKAEMUTYYMGRTWZWRNVYGRYDWTSCICTAYGRNITFKVZDOINIDZRPYTNLAMGYGKWDMNRDNTVWUBPRILAATXMYLKQITDMCNZMYIRCRNWYMRCDMITYYMGKQYDCLAWTSMYLKBRTUQGINRWYCSWNIQTWKHAETQLMFNYMIDZRTCKRLMFNYMOTISYLICBZAPQRUOODCPIDWZCEYGRGRTIYCWLIZOMDKWLMFNYMMRIAGKKZMRQYVQYLICBYWZZMGZVZIZMAODICTATWUWVMEACKMANWAZRYKFYQYGMAOTYKOQRGDQCEQUTAVTEMOTIYZICORTWYAZMUTYYMSGDIIGRTNRNRWYCEBTHURIYGNIGUICLAMGYGKWDMNRDNTVOVYZRIMAGKNBNRBZTMUXSCCPUOLMFNYMMRAQKFGINRCAOUCWKGYQGRRKVYHKAZMGYGMADERTCPUOZKTVZMYGCEEGBYWIWZDATATGYQMZUOYMIRAQAHNWAZKTKWWIDAMOLAWGBYYGOBGZKRCDEMGKVTZDARNWAZIWBYMGWTTNUWODILKZZMFEATTNLAOILUEUUOLMFNYMSGRKYGNWQDTNNAQANTSKRTCUTYYMMZZTWMGKWCKQMGYGCEHWGKCDIQYQATBOCEAYTKQDFUTYYMVYYGMAUGRTDASGMAQTWHTLEXMZLAMGYGRNIGYQMRTAGKNACKUXEUEFTWPHGUFMTYYMMRIAGKWCKQMGYGCEETGKQDIQYQYGNWQDTNKQMOCEXITYYMPYQITOYLIDZRYGYVNGRTKQYGKTQDRKYWAETDBPMITYYMMRVQRNRIYGZTYGRNLAMEZWRNTCRCLMFNYMQYDCYGNWQDTNDATAYGKTQDNGRTKQDLWYYGKWMYNITYYMSGDUGSYQAEIKRKYLBPLAMETVDICOYRIWGKKTKWLMFNYMQYDCYGNWQDTNNB'

separator = "#"*len(text)

pairs_frequencies = [('YG', 56), ('YM', 49), ('GK', 30), ('MR', 29), ('RN', 27), ('TY', 26), ('LM', 24), ('YL', 22), ('LA', 22), ('FN', 22), ('NR', 20), ('TA', 18), ('RT', 17), ('CE', 16), ('KW', 16), ('QD', 15), ('MG', 15), ('TN', 14), ('RI', 14), ('TV', 13), ('QY', 13), ('MA', 12), ('RC', 12), ('NW', 12), ('DM', 11), ('KR', 11), ('WY', 11), ('IC', 11), ('ZA', 10), ('VY', 10), ('WZ', 10), ('BY', 10), ('GU', 10), ('CP', 9), ('AZ', 9), ('EX', 9), ('ZM', 9), ('IW', 9), ('WI', 8), ('SG', 8), ('KQ', 8), ('AT', 8), ('WT', 8), ('KT', 8), ('RK', 8), ('PY', 8), ('MZ', 8), ('TW', 8), ('UO', 8), ('HK', 8), ('UW', 8), ('NI', 8), ('OT', 8), ('YQ', 8), ('GR', 7), ('CD', 7), ('IZ', 7), ('GI', 7), ('OD', 7), ('EM', 7), ('QT', 6), ('IG', 6), ('DN', 6), ('KF', 6), ('DO', 6), ('AE', 6), ('IQ', 6), ('DA', 6), ('WN', 5), ('IA', 5), ('WC', 5), ('EA', 5), ('UN', 5), ('KG', 5), ('AQ', 5), ('CK', 5), ('TD', 5), ('CU', 5), ('GZ', 5), ('KB', 5), ('UB', 5), ('QA', 5), ('MU', 5), ('DC', 5), ('ID', 5), ('DQ', 4), ('BE', 4), ('MV', 4), ('YI', 4), ('OV', 4), ('ED', 4), ('FU', 4), ('DU', 4), ('ZW', 4), ('IR', 4), ('TC', 4), ('BP', 4), ('MD', 4), ('TS', 4), ('ZR', 4), ('CB', 4), ('LI', 4), ('NG', 4), ('ME', 4), ('YH', 4), ('KA', 4), ('RG', 4), ('MI', 4), ('ZT', 4), ('MO', 4), ('SC', 4), ('AR', 3), ('UZ', 3), ('GS', 3), ('RD', 3), ('YZ', 3), ('WU', 3), ('VO', 3), ('AM', 3), ('UQ', 3), ('QU', 3), ('CT', 3), ('BO', 3), ('DI', 3), ('IT', 3), ('TL', 3), ('NB', 3), ('OB', 3), ('ZD', 3), ('ZI', 3), ('VM', 3), ('OA', 3), ('IB', 3), ('YW', 3), ('MY', 3), ('NA', 3), ('CO', 3), ('IY', 3), ('AD', 3), ('VQ', 3), ('VZ', 3), ('VT', 3), ('TM', 2), ('IE', 2), ('IH', 2), ('XN', 2), ('UL', 2), ('IO', 2), ('TK', 2), ('FH', 2), ('OQ', 2), ('DL', 2), ('VS', 2), ('GY', 2), ('YV', 2), ('DK', 2), ('GL', 2), ('CM', 2), ('FE', 2), ('YF', 2), ('IU', 2), ('RQ', 2), ('QM', 2), ('NT', 2), ('MP', 2), ('AI', 2), ('OI', 2), ('HU', 2), ('IL', 2), ('DT', 2), ('TQ', 2), ('WG', 2), ('SK', 2), ('KS', 2), ('AL', 2), ('QR', 2), ('LU', 2), ('FM', 2), ('RY', 2), ('IK', 2), ('YD', 2), ('AP', 2), ('ZO', 2), ('DE', 2), ('BZ', 2), ('CW', 2), ('KZ', 2), ('UX', 2), ('EU', 2), ('MQ', 1), ('XU', 1), ('BH', 1), ('AX', 1), ('QG', 1), ('SY', 1), ('EI', 1), ('OX', 1), ('WL', 1), ('TE', 1), ('YB', 1), ('GH', 1), ('MW', 1), ('ND', 1), ('YC', 1), ('WK', 1), ('LH', 1), ('TB', 1), ('SH', 1), ('CQ', 1), ('QN', 1), ('LD', 1), ('RX', 1), ('FI', 1), ('HD', 1), ('FC', 1), ('OY', 1), ('VH', 1), ('XF', 1), ('KD', 1), ('ZC', 1), ('MK', 1), ('DR', 1), ('AO', 1), ('EC', 1), ('PA', 1), ('VF', 1), ('VL', 1), ('EY', 1), ('VC', 1), ('PD', 1), ('LW', 1), ('FK', 1), ('IN', 1), ('XM', 1), ('CN', 1), ('SM', 1), ('CS', 1), ('KH', 1), ('IS', 1), ('YK', 1), ('BT', 1), ('CA', 1), ('OU', 1), ('ZK', 1), ('EG', 1), ('TG', 1), ('AH', 1), ('WM', 1), ('HW', 1), ('AY', 1), ('UG', 1), ('WH', 1), ('EF', 1), ('PH', 1), ('ET', 1), ('XI', 1), ('QI', 1), ('TO', 1), ('YR', 1)]
en_most_frequent = ["th","he","in","er","an","re","nd","at","on"] #["th","er","on","an","re","he","in", "ed","nd","ha","at","en","es","of","or","nt","ea","ti","to","it","st","io","le","is","ou","ar","as","de","rt","ve"]
max_combs = 6
all_pot_encrypt_maps = []

additional_mappings = {}


if __name__ == '__main__':
    #generate top X potential mappings
    truncated_CT_freqs = [a_tuple[0] for a_tuple in pairs_frequencies][0:max_combs]
    print(truncated_CT_freqs)
    truncated_EN_freqs = en_most_frequent[0:max_combs]
    all_permutations = [ i for i in permutations(truncated_CT_freqs)]
    print(all_permutations)
    print(len(all_permutations))
    for perm_tuple in all_permutations:
        map={}
        for i,two_letters in enumerate(perm_tuple):
            map[two_letters] = truncated_EN_freqs[i]
        all_pot_encrypt_maps.append(map)

    print(all_pot_encrypt_maps)
    print(len(all_pot_encrypt_maps))
    with open("out.txt",'w') as f:
         for dict in all_pot_encrypt_maps:
            plaintext = ""
            replaced = 0
            flag = False
            two_in_a_row = 0
            dict.update(additional_mappings)
            for i in range(0,len(text),2):
                alreadyReplaced = False
                for k,v in dict.items():
                    ct = text[i]+text[i+1]
                    if ct == k:
                        plaintext+=v
                        replaced += 1
                        two_in_a_row += 1
                        alreadyReplaced = True
                        break
                    elif ct == k[::-1]:
                        plaintext += v[::-1]
                        replaced += 1
                        two_in_a_row += 1
                        alreadyReplaced = True
                        break
                if(two_in_a_row >= 2) :
                    flag = True
                if not alreadyReplaced:
                    plaintext+=".."
                    two_in_a_row = 0
            tern = " HAVETWO!!!" if flag else " NOPAIR:("
            o = plaintext+'\n'+ "Replaced: " + str(replaced)  + ", using mapping: " + str(dict) +tern + separator+'\n'
            #print(o)
            f.write(o)