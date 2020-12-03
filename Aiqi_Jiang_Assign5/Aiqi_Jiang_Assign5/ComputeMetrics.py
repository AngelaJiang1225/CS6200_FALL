
# After extract urls to files and mark every result's relevance, create dictionaries to
# mark value "1" as relevant, "0" as not relevant.
# "name" means for which information need and search engine.
# next are rank numbers and its marked results.

info_need_1_google_dic = {"name": "1_google", 0: 0, 1: 1, 2: 0, 3: 0, 4: 0,
                          5: 1, 6: 0, 7: 1, 8: 0,
                          9: 0, 10: 0, 11: 0, 12: 0,
                          13: 0, 14: 0, 15: 0}
info_need_1_bing_dic = {"name": "1_bing", 0: 0, 1: 1, 2: 1, 3: 1, 4: 0, 5: 1,
                        6: 1, 7: 1, 8: 0, 9: 0, 10: 0, 11: 0,
                        12: 0, 13: 0, 14: 0, 15: 0}
info_need_2_google_dic = {"name": "2_google", 0: 0, 1: 1, 2: 1, 3: 0, 4: 0, 5: 1,
                        6: 1, 7: 1, 8: 1, 9: 0, 10: 0, 11: 0,
                        12: 0, 13: 0, 14: 0, 15: 0}
info_need_2_bing_dic = {"name": "2_bing", 0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0,
                        6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
                        12: 0, 13: 0, 14: 0, 15: 0}
info_need_3_google_dic = {"name": "3_google", 0: 0, 1: 1, 2: 0, 3: 1, 4: 1, 5: 1,
                        6: 1, 7: 1, 8: 1, 9: 0, 10: 0, 11: 0,
                        12: 0, 13: 0, 14: 0, 15: 0}
info_need_3_bing_dic = {"name": "3_bing", 0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1,
                        6: 1, 7: 1, 8: 1, 9: 0, 10: 0, 11: 0,
                        12: 0, 13: 0, 14: 0, 15: 0}

# put all dictionaries into list for traversing operation.
dics_set = []
dics_set.append(info_need_1_google_dic)
dics_set.append(info_need_1_bing_dic)
dics_set.append(info_need_2_google_dic)
dics_set.append(info_need_2_bing_dic)
dics_set.append(info_need_3_google_dic)
dics_set.append(info_need_3_bing_dic)

# store precision results into output file.
PRECISION_INFO_FILE = "precision_info_file"

# detailed operation for calculating precision
def main():
    f = open(PRECISION_INFO_FILE, "w+")
    for dic in dics_set:
        avg_p_when_relevant_8 = 0
        # rel_num = 0
        f.write(dic["name"]+"\n")
        print(dic["name"])
        for i in range(1, 16):
            # rel_num += dic[i]
            if i <= 8 and dic[i] == 1:
                avg_p_when_relevant_8 += (dic[i-1]+1)/i
            dic[i] = dic[i-1]+dic[i]
        avg_p_8 = 0
        rel_num_8 = dic[8]
        for i in range(1, 16):
            dic[i] = dic[i]/i
            if i <= 8:
                avg_p_8 += dic[i]
        avg_p_8 = avg_p_8/rel_num_8
        avg_p_when_relevant_8 = avg_p_when_relevant_8/rel_num_8
        dic["avg_p_8"] = avg_p_8
        dic["avg_p_when_relevant_8"] = avg_p_when_relevant_8
        f.write(str(dic[5])+"\n")
        f.write(str(dic[8])+"\n")
        f.write(str(dic[12])+"\n")
        f.write(str(dic["avg_p_8"])+"\n")
        f.write(str(dic["avg_p_when_relevant_8"])+"\n")
        print(dic[5])
        print(dic[8])
        print(dic[12])
        print(dic["avg_p_8"])
        print(dic["avg_p_when_relevant_8"])
    f.close()

main()