import os
import gymnasium as gym
from stable_baselines3 import SAC
import imageio

def record_video(model, env_id="Hopper-v4", video_length=1000, filename="sac_hopper_shaped"):
    env = gym.make(env_id, render_mode="rgb_array")
    obs, _ = env.reset()
    frames = []

    for _ in range(video_length):
        frames.append(env.render())
        action, _ = model.predict(obs, deterministic=True)
        obs, _, terminated, truncated, _ = env.step(action)
        if terminated or truncated:
            obs, _ = env.reset()

    env.close()

    os.makedirs("videos", exist_ok=True)
    video_path = os.path.join("videos", f"{filename}.mp4")
    imageio.mimsave(video_path, frames, fps=30)
    print(f"Video saved to: {video_path}")
    return video_path

# Load your saved SAC model 
model = SAC.load(r"C:\Users\user\Downloads\RL\model.zip")


# Record video
video_path = record_video(model)

