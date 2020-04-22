# Project 1 - Navigation in the Banana Collection World

<center>
	<img src="https://video.udacity-data.com/topher/2018/June/5b1ab4b0_banana/banana.gif" alt="drawing" width="480"/>
</center>

## Introduction

This project aims to train a banana collector agent capable of navigating in the Banana collector environment and getting as many rewards as possible during its navigation. In this environment, the agent can achieve 2 types of rewards: yellow banana (+1) and blue banana (-1). The states of the agent are specified by a ray tracing
based approach that measures the income light produced by the objects at sight (whatever object that can be seen in the viewing cone of the agent inside the environment at each time step). A more detailed description is provided in the report.pdf file. 

## Files in project

|  File | Description | 
|-------|-------------|
| Navigation.ipynb  | A notebook where we visualize the environment, train the agent and assess its performance. | 
| dqn_agent.py  | A python script where we define the DQN agentk. | 
| model.py  | A python script where we define the neural network used by the agent to estimate the action-value function. |
| report.pdf  | A more complete report of the environment, data and results |
| checkpoint.pth | Saved weights of the agent neural network | 