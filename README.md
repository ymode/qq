# qq
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ymode/qq/pylint.yml)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ymode/qq) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/ymode/qq) ![GitHub watchers](https://img.shields.io/github/watchers/ymode/qq)



Quick Question - LLM in the terminal.




<img src="https://github.com/user-attachments/assets/60dce499-561a-4ad0-b98a-67adaaf48e3a" width="150"/>

___
qq is a markdown rich terminal based LLM interface - so you never have to leave the terminal!


🎨 Markdown support in your terminal

🧠 gpt-4o-mini (default LLM)

⌨️ Prompt engineering layer to ensure terminal/linux based responses

💻 Stay in terminal

# Use
```qq how do I list files in terminal by size?```

<img width="983" alt="image" src="https://github.com/user-attachments/assets/1af2beb7-bb82-4fbe-a47f-8f11a32998af">




# Setup

🔑 Ensure your [OpenAI](https://openai.com/api/) API Key is exported in the following format: ```export OPENAI_API_KEY=your openai key```

💻 Automatic Setup: In your Term, paste the following

```export OPENAI_API_KEY=your OpenAI API key
git clone https://github.com/ymode/qq.git
cd qq
pip install -r requirements.txt
chmod +x qq
sudo mv qq /usr/local/bin/
```

If you prefer manually setting up

💾 Manual Setup: install [dotenv](https://github.com/motdotla/dotenv) and [openai](https://github.com/openai/openai-python) on your system


# Support
The best way to support this project is to contribute! But if you would like to buy me a coffee, there is a link below.

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ymode)

# Credits

[OpenAI gpt-4o-mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)

[dotenv](https://github.com/motdotla/dotenv)

[rich terminal markdown](https://github.com/Textualize/rich)
