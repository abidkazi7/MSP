from Aj_new_function import read_dataset

crops_path = {1: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Rice.csv',
            2: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Maize.csv',
            3: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Groundnut.csv',
            4: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Moong.csv',
            5: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Urad.csv',
            6: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Soyabean.csv',
            7: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Jowar.csv',
            8: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Tur.csv',
            9: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Cotton.csv'
            }
for i in range(1,10):
    read_dataset(crops_path[i],i,i,i,i,i)
    print("------------------------------------------------------------------------------------")