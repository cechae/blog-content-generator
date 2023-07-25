# Blog Content Generator App

Live version of this app at [blog-content-generator.streamlit.app](https://blog-content-generator-6simuukxnb.streamlit.app/)


## Description

This Streamlit app generates realistic blog-post style text based on the user inputs. 

The text prompt form accepts a Tone as well as a Creativity parameter. The app then generates a prompt with an instruction to write a respective text and sends this request to the Cohere API which - using one of their LLM models that have been trained on a lot of publicly available text content - predicts the next likely to be used (word) tokens and generates the blog content.
