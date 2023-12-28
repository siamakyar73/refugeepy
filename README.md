<br> Classifying Sentiments and Uncovering Themes: A Deep Dive into YouTube and Reddit Texts on the UK Refugee Crisis <br>
<br> In this project, I tried to train three models that can classify the sentiments towards refugee issue in the UK on the comments of YouTube and discussions under different subreddits related to this issue. <br>
<br> I collected several texts from the aforementioned sources using their API and put them in a sheet that can be seen in "Bookf.csv" file. It is worth mentioning that the two target classes are refugee-supportive and non-supportive.<br>
<br>Regarding the model training phase, first, we decided to use a support vector machine for classification and then tried to feed RoBERTa embeddings to the SVM. The reason to do so was to see whether there would be any improvement.
Since there is an imbalance issue in our two target classes (supportive (1) and non-supportive (0)), it was predictable that these two models would have unsuitable performance in predicting supportive texts. 
The third model, which uses RoBERTa for text classification, appears to perform better than the other two models for our specific task.
It achieves a better balance between precision and recall for the Supportive class while maintaining good performance on the Non-Supportive class. 
The first (SVM) and second model (SVM-RoBERTa) both struggled with correctly classifying Supportive comments, which suggests that RoBERTa may be more suitable for our task than SVM for our specific task.
The limitation of the third model is that it has a time-consuming nature to be trained. <br>
