import pandas as pd

val_df=pd.read_csv(r'C:\Users\Saranga\Desktop\COVID cough\DiCOVA_Train_Val_Data_Release\EVALUATION\Submission10\LSTM_audiomentations_val_set_results.csv')
writePath='val_scores.txt'

with open(writePath, 'a') as f:
    f.write(
        val_df.to_string(header = False, index = False)
    )


test_df=pd.read_csv(r'C:\Users\Saranga\Desktop\COVID cough\DiCOVA_Train_Val_Data_Release\EVALUATION\Submission10\LSTM_audiomentation_Blind_Set_results.csv')
writePath2='test_scores.txt'

with open(writePath2, 'a') as f2:
    f2.write(
        test_df.to_string(header = False, index = False)
    )