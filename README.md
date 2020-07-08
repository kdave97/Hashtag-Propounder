# Hashtag-Propounder

Hashtags (#) are prefixed keywords which are used to provide topical and contextual information about the tweets. Therefore, hashtags are frequently used as queries to search for tweets about a topic or specific event. Hashtags not only provide the right context to interpret and categorize the content but also serve as a medium to promote content to readers. Hashtags do not just give the correct setting to decipher the substance and to order substance yet additionally fill in as a medium to elevate substance to achieve more perusers. In this way use of proper hashtag benefit numerous applications, for example, content search, classification of content, and substance discovery.

## Problem Statement
Understanding the substance of the user's picture posts is an especially intriguing issue with regards to social networks and web settings. Numerous tweets are set apart with hashtags, which normally speak to gatherings or themes of tweets. Automating this process may increase the usage of Hashtags. Current models and applications made to generate hashtags depend on either using semantic analysis of the text or performing image processing to extract features from the image. These models have good accuracy but can be further improved if both these techniques are integrated together. Since the users upload both the image as well as a caption, integrating both would lead to an increase in the overall performance of the model.

## Proposed Solution
Captions are a useful description of the image. Apart from extracting useful features and objects from an image, using named entity recognition of text can help to focus on most relevant hashtags. The model we suggest is the coalescence of Image Annotation and Text Analysis.

The aim of the model is to generate the most appropriate hashtags based on the user’s input image and caption. The model takes these inputs and separately performs the operations on both the inputs. The Image analysis model performs functions like image processing and extracting objects from the image. Similarly, the text analysis model takes the caption as input and performs named entity recognition to identify the keywords. Based on the output of these models, the hashtag generator model will determine the hashtags. Later these hashtags are filtered out based on the trending hashtags. The final output to the user will be a set of most relevant hashtags.

![alt text](https://github.com/kdave97/Hashtag-Propounder/blob/master/images/Coalesce%20model.JPG)

