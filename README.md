# hopperv4-SAC
solved hopper-v4 using SAC


# Soft Actor-Critic (SAC) on Hopper-v4 with Evaluation, Hyperparameter Sensitivity, and Reward Shaping

This project demonstrates the training, evaluation, and analysis of a Soft Actor-Critic (SAC) reinforcement learning agent on the `Hopper-v4` environment using `Stable-Baselines3`. It includes experiments with:
- Evaluation using saved models
- Plotting reward curves
- Hyperparameter sensitivity analysis (learning rate, gamma, entropy coefficient)
- Robustness testing with modified environment dynamics
- Custom reward shaping
- Comparison with a random agent baseline

---

## 🛠 Installation

To run the code in a Colab environment, ensure the following dependencies are installed:

```
!apt-get install -y swig
!pip install stable-baselines3[extra] seaborn
!pip install "gymnasium[mujoco]"
!pip install box2d-py
```

## 📊 Outputs
Plots for:
- Learning curves
- Reward distributions
- Hyperparameter sweep comparisons


Printout of evaluation results for:
- Default SAC model
- Random baseline
- Shaped reward model
- Modified gravity environment


## 📚 References
Stable-Baselines3 Docs


Gymnasium


MuJoCo Environments

## 📌 Disclaimer:
This project was developed as part of a personal learning journey in reinforcement learning. As such, it may include experimental implementations, non-optimized code, or areas for improvement. Feedback, suggestions, and contributions are always welcome!
