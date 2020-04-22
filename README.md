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

## Installation and requirements

Plese, visit the Deep Reinforcement Learning [repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) maintained by Udacity in order to install all dependencies to work with the code used here. All the steps presented there can be break down into the steps in file requirements.txt:

```console
youruse@yourcomputer:~$ conda env create -f environment.yml
youruse@yourcomputer:~$ python -m ipykernel install --user --name drlnd --display-name "drlnd"
```

Finally we should download and extract the banana environment in the same folder of your project. Please, refer to the list below to download it:

- Linux: [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Linux.zip)
- Mac OSX: [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana.app.zip)
- Windows (32-bit): [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Windows_x86.zip)
- Windows (64-bit): [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Windows_x86_64.zip)

## The agent

Our agent uses the Deep Q-Network scheme presented in the paper [Human-level control through deep reinforcement learning](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf) to improve its performance on the environment and collect the highest reward during every episode.

### Training

Our agent is trained in the Navigation.ipynb notebook running the cells presented in its training section. A typical training routine yields a result as the one below in which the agent with the parameters given in the parameters_dict variable in the notebook is capable of reaching an average score of 15 at the end of the last 100 episodes. 

![The rewards obtained at the end of each episode as well as the average of the last 100 episodes and a moving average with step size equal to 3.][images/scores_all.png]

## Report file

The report.pdf file is a more detailed document in which the detailed information of the agent and the neural networks used are presented. We also discuss further the results found and what improvements can be performed. 




