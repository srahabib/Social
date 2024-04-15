import React from 'react'
import Metadata from './Metadata'
import Statistics from './Statistics'
import Try from './Try'
import Examples from './Examples'

function Story() {
  return (
    <div>
      <div className="max-w-4xl mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold text-center mb-8">Why Tweeter? : The Story Behind the Dataset</h2>
      <p className="text-lg leading-relaxed">
        In the vast realm of social media, Twitter stands out as a platform where voices from all walks of life converge,
        expressing opinions, sharing insights, and engaging in conversations that shape our digital landscape.
        Within this digital cacophony lies a treasure trove of data, each tweet a snapshot of human expression captured in 280 characters or less.
      </p>
      <p className="text-lg leading-relaxed mt-4">
        Our dataset is a collection of such tweets, meticulously curated and harvested from the Twitterverse. Spanning various topics,
        trends, and timestamps, these tweets offer a glimpse into the pulse of the online community, capturing moments of joy, outrage,
        curiosity, and everything in between.
      </p>
      <h2 className="text-3xl font-bold text-center mt-12 mb-8">The Project : Our goal </h2>
      <p className="text-lg leading-relaxed">
        Armed with this rich dataset, our project embarks on a journey to unravel the hidden insights buried within the sea of tweets.
        Leveraging the power of Textblob  and  predictive machine learning, we seek to decode the sentiments, trends, and narratives that permeate through Twitter's digital tapestry.
      </p>
      {/* Continue with the rest of the story */}
      <Metadata/>

      <h2 className="text-3xl font-bold text-center mt-12 mb-8">Overview of the analysis  </h2>
      <p className="text-lg leading-relaxed">
      In our dataset comprising 400 records and 6 features, we observed that 348 records had missing hashtags, while we encountered no duplicates. Leveraging predictive models, we achieved an impressive accuracy rate of 98%. This high accuracy underscores the robustness of our models in forecasting sentiment trends. With meticulous data preprocessing and effective model training, we were able to extract valuable insights from the dataset and generate reliable predictions.
      </p>

      <Statistics/>

      <h2 className="text-3xl font-bold text-center mt-12 mb-8"> Try our code  </h2>
      <p className="text-lg leading-relaxed">
      Experience the power of sentiment analysis with our intuitive text input feature. Simply enter your text, and our system will swiftly analyze its sentiment using advanced Natural Language Processing techniques. Whether it's a tweet, review, or any other text snippet, our tool provides instant feedback on the emotional tone conveyed. Try it now and gain valuable insights into the sentiment behind your text!
      </p>

     <Try/>

     <h2 className="text-3xl font-bold text-center mt-12 mb-8"> Example Sentiments  </h2>
      <p className="text-lg leading-relaxed">
      We successfully employed TextBlob to analyze a collection of tweets, accurately assigning sentiment scores to each. These scores reflect the underlying sentiment expressed in the tweets, capturing nuances of positivity, negativity, or neutrality. This approach enabled us to gain valuable insights into the sentiment landscape within the Twitter sphere, providing a deeper understanding of public opinion and sentiment trends. By leveraging TextBlob's natural language processing capabilities, we efficiently processed the textual content of tweets, empowering us to extract meaningful sentiment information and inform decision-making processes.
      </p>

      <Examples/>
      <img src="/pie.jpg" alt="Img" className="mx-auto mt-8" />

      <h2 className="text-3xl font-bold text-center mt-12 mb-8"> Prediction  </h2>
      <p className="text-lg leading-relaxed">
      In our modeling and prediction phase, we employed two powerful machine learning algorithms, Support Vector Machine (SVM) and Random Forest, to predict sentiment based on key features such as likes, retweets, polarity, and subjectivity. Our SVM model achieved an accuracy of 86.25%, demonstrating its effectiveness in discerning sentiment patterns in the data. On the other hand, our Random Forest classifier outperformed with an impressive accuracy of 98.75%, showcasing its robustness in handling complex relationships within the dataset. Furthermore, the detailed classification report for the Random Forest model reveals high precision, recall, and F1-score across all sentiment classes, underscoring its ability to accurately classify sentiments as negative, neutral, or positive. Through rigorous modeling and evaluation, we have established reliable predictive models capable of accurately categorizing sentiment, thereby providing valuable insights for sentiment analysis tasks.
      </p>
      <img src="/scatter.jpg" alt="Img" className="mx-auto mt-8" />
      



      <h2 className="text-3xl font-bold text-center mt-12 mb-8"> Evaluation  </h2>
      <p className="text-lg leading-relaxed">
      For the evaluation of our sentiment prediction model, we conducted a comparative analysis with real-world data, specifically focusing on the price movements of Bitcoin. After predicting sentiment for specific timestamps using our trained model, we juxtaposed these predictions with the corresponding Bitcoin prices at those timestamps. Remarkably, our model accurately predicted a negative sentiment for both timestamps, aligning with the observed price movements of Bitcoin during those periods. This validation process reinforces the reliability and efficacy of our sentiment prediction model, demonstrating its potential applicability in real-time market analysis and decision-making processes.
      </p>
      <img src="/vs.jpg" alt="Img" className="mx-auto mt-8" />



    </div>
    </div>
     



  )
}

export default Story
