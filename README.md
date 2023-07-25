# Blog Content Generator App

Blog content generator using Cohere API, hosted on streamlit.
Live version of this app at [blog-content-generator.streamlit.app](https://blog-content-generator-6simuukxnb.streamlit.app/)

## Description

This Streamlit mini-app generates realistic blog-post style text based on the user inputs. 

The text prompt creation form accepts a Tone as well as Creativity parameter. The app then generates a prompt with an instruction to write a respective text and sends this to the Cohere API which - using one of their Generative AI models that have been trained on a lot of publicly available text content - predicts the next likely to be used (word) tokens and generates the blog content.
